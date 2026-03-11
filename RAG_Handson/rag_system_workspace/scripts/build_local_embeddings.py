from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
SYSTEM_ROOT = WORKSPACE_ROOT / "rag_system_workspace"
CHUNKS_DIR = SYSTEM_ROOT / "rag_artifacts" / "chunks"
VECTORSTORE_DIR = SYSTEM_ROOT / "rag_artifacts" / "vectorstore"


@dataclass
class ChunkRecord:
    chunk_id: str
    source_file: str
    folder_profile: str
    section_title: str
    section_chunk_index: int
    token_count: int
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build local FAISS index from JSONL chunks.")
    parser.add_argument(
        "--model-name",
        default="sentence-transformers/all-MiniLM-L6-v2",
        help="SentenceTransformer model name.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=128,
        help="Embedding batch size (reduce if RAM is constrained).",
    )
    parser.add_argument(
        "--normalize",
        action="store_true",
        help="Normalize vectors for cosine similarity via inner product.",
    )
    parser.add_argument(
        "--output-name",
        default="minilm_l6",
        help="Output subfolder name under rag_artifacts/vectorstore.",
    )
    return parser.parse_args()


def load_chunks(chunks_dir: Path) -> list[ChunkRecord]:
    records: list[ChunkRecord] = []
    for jsonl_path in sorted(chunks_dir.rglob("*.chunks.jsonl")):
        with jsonl_path.open("r", encoding="utf-8") as f:
            for line in f:
                raw: dict[str, Any] = json.loads(line)
                if not raw.get("text"):
                    continue
                records.append(
                    ChunkRecord(
                        chunk_id=raw["chunk_id"],
                        source_file=raw["source_file"],
                        folder_profile=raw["folder_profile"],
                        section_title=raw["section_title"],
                        section_chunk_index=int(raw["section_chunk_index"]),
                        token_count=int(raw["token_count"]),
                        text=raw["text"],
                    )
                )
    return records


def build_index(vectors: np.ndarray) -> faiss.IndexFlat:
    dim = vectors.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(vectors)
    return index


def save_metadata(path: Path, records: list[ChunkRecord]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(
                json.dumps(
                    {
                        "chunk_id": rec.chunk_id,
                        "source_file": rec.source_file,
                        "folder_profile": rec.folder_profile,
                        "section_title": rec.section_title,
                        "section_chunk_index": rec.section_chunk_index,
                        "token_count": rec.token_count,
                    },
                    ensure_ascii=True,
                )
                + "\n"
            )


def main() -> None:
    args = parse_args()
    if not CHUNKS_DIR.exists():
        raise SystemExit(f"Chunks directory not found: {CHUNKS_DIR}")

    output_dir = VECTORSTORE_DIR / args.output_name
    output_dir.mkdir(parents=True, exist_ok=True)

    records = load_chunks(CHUNKS_DIR)
    if not records:
        raise SystemExit("No chunk records found. Run chunking first.")

    texts = [r.text for r in records]
    print(f"Loaded {len(texts)} chunks")
    print(f"Model: {args.model_name}")

    model = SentenceTransformer(args.model_name)
    vectors = model.encode(
        texts,
        batch_size=args.batch_size,
        show_progress_bar=True,
        normalize_embeddings=args.normalize,
        convert_to_numpy=True,
    ).astype("float32")

    index = build_index(vectors)
    faiss.write_index(index, str(output_dir / "faiss_index.bin"))
    np.save(output_dir / "embeddings.npy", vectors)
    save_metadata(output_dir / "metadata.jsonl", records)

    summary = {
        "model_name": args.model_name,
        "batch_size": args.batch_size,
        "normalize_embeddings": args.normalize,
        "chunks": len(records),
        "vector_dim": int(vectors.shape[1]),
        "index_path": str((output_dir / "faiss_index.bin").relative_to(WORKSPACE_ROOT)).replace("\\", "/"),
    }
    (output_dir / "build_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"Saved index and metadata to: {output_dir}")


if __name__ == "__main__":
    main()
