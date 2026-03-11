from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
SYSTEM_ROOT = WORKSPACE_ROOT / "rag_system_workspace"
DOCS_DIR = WORKSPACE_ROOT / "docs"
OUTPUT_DIR = SYSTEM_ROOT / "rag_artifacts" / "chunks"


@dataclass(frozen=True)
class ChunkProfile:
    name: str
    target_tokens: int
    max_tokens: int
    overlap_tokens: int
    split_levels: tuple[int, ...]


PRODUCT_PROFILE = ChunkProfile(
    name="product_owner_docs",
    target_tokens=450,
    max_tokens=600,
    overlap_tokens=60,
    split_levels=(2,),
)

TECHNICAL_PROFILE = ChunkProfile(
    name="technical_docs",
    target_tokens=360,
    max_tokens=520,
    overlap_tokens=70,
    split_levels=(2,),
)

OPS_PROFILE = ChunkProfile(
    name="operations_docs",
    target_tokens=320,
    max_tokens=450,
    overlap_tokens=50,
    split_levels=(2,),
)

DEFAULT_PROFILE = ChunkProfile(
    name="general_docs",
    target_tokens=380,
    max_tokens=520,
    overlap_tokens=60,
    split_levels=(2,),
)


TOKEN_RE = re.compile(r"\S+")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


def token_count(text: str) -> int:
    return len(TOKEN_RE.findall(text))


def split_markdown_sections(text: str, allowed_levels: Iterable[int]) -> list[tuple[str, str]]:
    levels = set(allowed_levels)
    matches = [m for m in HEADING_RE.finditer(text) if len(m.group(1)) in levels]

    if not matches:
        return [("Document", text.strip())] if text.strip() else []

    sections: list[tuple[str, str]] = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunk = text[start:end].strip()
        heading = match.group(2).strip()
        if chunk:
            sections.append((heading, chunk))
    return sections


def split_section_into_chunks(section_text: str, profile: ChunkProfile) -> list[str]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", section_text) if p.strip()]
    if not paragraphs:
        return []

    chunks: list[str] = []
    current = ""

    for para in paragraphs:
        candidate = f"{current}\n\n{para}".strip() if current else para
        if token_count(candidate) <= profile.target_tokens or not current:
            current = candidate
            continue
        chunks.append(current)
        current = para

    if current:
        chunks.append(current)

    final_chunks: list[str] = []
    for chunk in chunks:
        if token_count(chunk) <= profile.max_tokens:
            final_chunks.append(chunk)
            continue
        final_chunks.extend(window_split(chunk, profile.max_tokens, profile.overlap_tokens))

    return final_chunks


def window_split(text: str, max_tokens: int, overlap_tokens: int) -> list[str]:
    words = TOKEN_RE.findall(text)
    if len(words) <= max_tokens:
        return [text]

    step = max(1, max_tokens - overlap_tokens)
    windows: list[str] = []
    start = 0
    while start < len(words):
        end = min(len(words), start + max_tokens)
        windows.append(" ".join(words[start:end]))
        if end == len(words):
            break
        start += step
    return windows


def chunk_file(file_path: Path, profile: ChunkProfile) -> list[dict]:
    text = file_path.read_text(encoding="utf-8")
    sections = split_markdown_sections(text, profile.split_levels)
    if not sections:
        return []

    all_chunks: list[dict] = []
    chunk_num = 1

    for section_title, section_text in sections:
        section_chunks = split_section_into_chunks(section_text, profile)
        for idx, chunk_text in enumerate(section_chunks, start=1):
            all_chunks.append(
                {
                    "chunk_id": f"{file_path.stem}-c{chunk_num:03d}",
                    "source_file": str(file_path.relative_to(WORKSPACE_ROOT)).replace("\\", "/"),
                    "folder_profile": profile.name,
                    "section_title": section_title,
                    "section_chunk_index": idx,
                    "token_count": token_count(chunk_text),
                    "text": chunk_text,
                }
            )
            chunk_num += 1
    return all_chunks


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")


def pick_profile(md_file: Path) -> ChunkProfile:
    rel_parts = [p.lower() for p in md_file.relative_to(DOCS_DIR).parts]
    rel_path = "/".join(rel_parts)

    if "0-product-owner-onboarding" in rel_parts or "3-product-owner" in rel_parts:
        return PRODUCT_PROFILE
    if "6-ci-cd" in rel_parts or "11-kubernetes" in rel_parts or "8-kubernetes-local-deployment" in rel_parts:
        return OPS_PROFILE
    if "6-architecture" in rel_parts or "7-services" in rel_parts:
        return TECHNICAL_PROFILE
    if "epic_" in rel_path or "4-epics-and-pbis" in rel_parts or "9-roadmap-and-tracking" in rel_parts:
        return PRODUCT_PROFILE
    return DEFAULT_PROFILE


def main() -> None:
    if not DOCS_DIR.exists():
        raise SystemExit(f"Docs directory not found: {DOCS_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    md_files = sorted(p for p in DOCS_DIR.rglob("*.md") if "chunks" not in [x.lower() for x in p.parts])
    profile_stats: dict[str, dict] = {}
    folder_stats: dict[str, dict] = {}

    for md_file in md_files:
        rel = md_file.relative_to(DOCS_DIR)
        top_folder = rel.parts[0] if len(rel.parts) > 1 else "_root_docs"
        profile = pick_profile(md_file)
        chunks = chunk_file(md_file, profile)

        out_file = OUTPUT_DIR / rel.parent / f"{md_file.stem}.chunks.jsonl"
        write_jsonl(out_file, chunks)
        print(f"[OK] {rel.as_posix()}: {len(chunks)} chunks -> {out_file.relative_to(WORKSPACE_ROOT)}")

        profile_stats.setdefault(
            profile.name,
            {
                "profile": profile.name,
                "md_files": 0,
                "total_chunks": 0,
                "total_tokens": 0,
                "settings": {
                    "target_tokens": profile.target_tokens,
                    "max_tokens": profile.max_tokens,
                    "overlap_tokens": profile.overlap_tokens,
                    "split_levels": list(profile.split_levels),
                },
            },
        )
        profile_stats[profile.name]["md_files"] += 1
        profile_stats[profile.name]["total_chunks"] += len(chunks)
        profile_stats[profile.name]["total_tokens"] += sum(c["token_count"] for c in chunks)

        folder_stats.setdefault(top_folder, {"folder": top_folder, "md_files": 0, "total_chunks": 0})
        folder_stats[top_folder]["md_files"] += 1
        folder_stats[top_folder]["total_chunks"] += len(chunks)

    run_summary: list[dict] = []
    for row in profile_stats.values():
        row["avg_chunk_tokens"] = round(row["total_tokens"] / row["total_chunks"], 2) if row["total_chunks"] else 0
        run_summary.append(row)
    run_summary = sorted(run_summary, key=lambda x: x["profile"])

    summary_path = OUTPUT_DIR / "chunking_run_summary.json"
    summary_path.write_text(json.dumps(run_summary, indent=2), encoding="utf-8")
    print(f"\nSummary written to: {summary_path.relative_to(WORKSPACE_ROOT)}")

    markdown_lines = [
        "# Chunking Run Summary",
        "",
        f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Profile Summary",
        "",
        "| Profile | MD Files | Chunks | Avg Chunk Tokens |",
        "|---|---:|---:|---:|",
    ]
    for row in run_summary:
        markdown_lines.append(
            f"| `{row['profile']}` | {row['md_files']} | {row['total_chunks']} | {row['avg_chunk_tokens']} |"
        )
    markdown_lines.extend(
        [
            "",
            "## Folder Coverage",
            "",
            "| Top Folder | MD Files | Chunks |",
            "|---|---:|---:|",
        ]
    )
    for row in sorted(folder_stats.values(), key=lambda x: x["folder"]):
        markdown_lines.append(f"| `{row['folder']}` | {row['md_files']} | {row['total_chunks']} |")
    (OUTPUT_DIR / "chunking_run_summary.md").write_text("\n".join(markdown_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
