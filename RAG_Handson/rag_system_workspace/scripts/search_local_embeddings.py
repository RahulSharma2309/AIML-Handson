from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import faiss
from sentence_transformers import SentenceTransformer


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
SYSTEM_ROOT = WORKSPACE_ROOT / "rag_system_workspace"
VECTORSTORE_DIR = SYSTEM_ROOT / "rag_artifacts" / "vectorstore"
CHUNKS_DIR = SYSTEM_ROOT / "rag_artifacts" / "chunks"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search local FAISS embeddings.")
    parser.add_argument("--query", default="", help="Search query text.")
    parser.add_argument(
        "--model-name",
        default="sentence-transformers/all-MiniLM-L6-v2",
        help="SentenceTransformer model name (must match build model).",
    )
    parser.add_argument("--index-name", default="minilm_l6", help="Vectorstore subfolder name.")
    parser.add_argument("--top-k", type=int, default=5, help="Top-k results.")
    parser.add_argument(
        "--pool-size",
        type=int,
        default=200,
        help="Candidate pool size from FAISS before metadata filtering.",
    )
    parser.add_argument("--normalize", action="store_true", help="Normalize query embedding.")
    parser.add_argument(
        "--profile",
        default="",
        help="Optional folder_profile filter, e.g. operations_docs.",
    )
    parser.add_argument(
        "--source-contains",
        default="",
        help="Optional case-insensitive substring filter on source_file.",
    )
    parser.add_argument(
        "--section-contains",
        default="",
        help="Optional case-insensitive substring filter on section_title.",
    )
    parser.add_argument(
        "--list-profiles",
        action="store_true",
        help="List available profiles in metadata and exit.",
    )
    return parser.parse_args()


def load_metadata(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def load_chunk_text_map(chunks_dir: Path) -> dict[str, str]:
    text_map: dict[str, str] = {}
    for jsonl_path in sorted(chunks_dir.rglob("*.chunks.jsonl")):
        with jsonl_path.open("r", encoding="utf-8") as f:
            for line in f:
                raw = json.loads(line)
                text_map[raw["chunk_id"]] = raw["text"]
    return text_map


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    args = parse_args()
    index_dir = VECTORSTORE_DIR / args.index_name
    index_path = index_dir / "faiss_index.bin"
    metadata_path = index_dir / "metadata.jsonl"
    if not index_path.exists() or not metadata_path.exists():
        raise SystemExit(f"Missing index files in: {index_dir}")

    index = faiss.read_index(str(index_path))
    metadata = load_metadata(metadata_path)
    text_map = load_chunk_text_map(CHUNKS_DIR)
    if not metadata:
        raise SystemExit("Metadata is empty.")
    if args.list_profiles:
        profiles = sorted({m.get("folder_profile", "") for m in metadata if m.get("folder_profile", "")})
        print("Available profiles:")
        for p in profiles:
            print(f"- {p}")
        return
    if not args.query.strip():
        raise SystemExit("Provide --query, or use --list-profiles.")

    model = SentenceTransformer(args.model_name)
    qv = model.encode(
        [args.query],
        normalize_embeddings=args.normalize,
        convert_to_numpy=True,
    ).astype("float32")

    k_pool = min(max(args.pool_size, args.top_k), len(metadata))
    scores, indices = index.search(qv, k_pool)
    print(f"Query: {args.query}\n")
    profile_filter = args.profile.strip().lower()
    source_filter = args.source_contains.strip().lower()
    section_filter = args.section_contains.strip().lower()

    shown = 0
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0 or idx >= len(metadata):
            continue
        m = metadata[idx]
        if profile_filter and m.get("folder_profile", "").lower() != profile_filter:
            continue
        if source_filter and source_filter not in m.get("source_file", "").lower():
            continue
        if section_filter and section_filter not in m.get("section_title", "").lower():
            continue

        shown += 1
        text_preview = text_map.get(m["chunk_id"], "")[:280].replace("\n", " ")
        print(f"[{shown}] score={score:.4f}")
        print(f"    chunk_id: {m['chunk_id']}")
        print(f"    source:   {m['source_file']}")
        print(f"    profile:  {m['folder_profile']}")
        print(f"    section:  {m['section_title']}")
        print(f"    preview:  {text_preview}...\n")
        if shown >= args.top_k:
            break

    if shown == 0:
        print("No results matched the provided metadata filters.")


if __name__ == "__main__":
    main()
