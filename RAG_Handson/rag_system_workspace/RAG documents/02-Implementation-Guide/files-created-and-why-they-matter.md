# Files Created and Why They Matter

This is the practical map of what was created in your RAG workspace.

## Source knowledge base

- `../../rag/input_docs/`
  - all markdown docs that act as your knowledge source
  - this is the "raw library"

## Chunking layer outputs

- `../../rag_artifacts/chunks/**/*.chunks.jsonl`
  - chunked text + metadata records
  - these are your "searchable index cards"

- `../../rag_artifacts/chunks/chunking_run_summary.json`
- `../../rag_artifacts/chunks/chunking_run_summary.md`
  - stats by profile/folder (coverage, chunk counts, avg size)
  - useful to track changes after tuning chunk strategy

## Embedding/vector layer outputs

- `../../rag_artifacts/vectorstore/minilm_l6/faiss_index.bin`
  - FAISS index used for semantic nearest-neighbor search

- `../../rag_artifacts/vectorstore/minilm_l6/metadata.jsonl`
  - metadata aligned by row/index with FAISS vectors

- `../../rag_artifacts/vectorstore/minilm_l6/embeddings.npy`
  - raw embedding matrix (numpy array)
  - useful for analysis/debugging

- `../../rag_artifacts/vectorstore/minilm_l6/build_summary.json`
  - build settings and summary (model, vector dim, total chunks)

## Scripts and purpose

- `../../scripts/chunk_markdown_docs.py`
  - reads source markdown docs
  - applies profile-based chunking
  - writes JSONL chunk artifacts

- `../../scripts/build_local_embeddings.py`
  - reads chunk JSONL
  - creates local embeddings with free model
  - builds FAISS index + metadata outputs

- `../../scripts/search_local_embeddings.py`
  - semantic retrieval from FAISS
  - supports metadata filters (`profile`, `source-contains`, `section-contains`)

## Why this architecture is significant

- clean separation of stages:
  - source -> chunk -> embed -> retrieve
- easy to rerun any stage independently
- easy to compare strategies (by regenerating and rebuilding)
- better maintainability for future production migration
