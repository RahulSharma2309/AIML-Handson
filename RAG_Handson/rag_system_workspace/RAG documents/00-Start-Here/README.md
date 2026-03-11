# Start Here - RAG Workspace

If you are opening this project fresh, start from this file.

## What this project is

You built a practical RAG playground from real docs.

In simple words:
- You have many markdown knowledge files (your "library")
- You split them into meaningful chunks (your "index cards")
- You convert chunks into vectors/embeddings (your "GPS coordinates for meaning")
- You store them in FAISS to search semantically (your "smart lookup engine")

## What is already done

- Structured source docs kept in `../../rag/input_docs/`
- All docs chunked into JSONL in `../../rag_artifacts/chunks/`
- Local free embeddings generated for all chunks
- FAISS index created in `../../rag_artifacts/vectorstore/minilm_l6/`
- Semantic search script with metadata filtering is ready

## Where to run from

Run all commands from project root:

`C:\Users\Lenovo\source\repos\AIML\RAG_Handson`

## Quick command list

1) Rebuild chunks:

```powershell
.\.venv\Scripts\python.exe rag_system_workspace/scripts/chunk_markdown_docs.py
```

2) Build local embeddings (free model):

```powershell
.\.venv\Scripts\python.exe rag_system_workspace/scripts/build_local_embeddings.py --model-name sentence-transformers/all-MiniLM-L6-v2 --batch-size 128 --normalize --output-name minilm_l6
```

3) Search with metadata filters:

```powershell
.\.venv\Scripts\python.exe rag_system_workspace/scripts/search_local_embeddings.py --query "how deployment trigger works" --index-name minilm_l6 --model-name sentence-transformers/all-MiniLM-L6-v2 --normalize --profile operations_docs --source-contains 6-ci-cd --top-k 5
```

## Best next read

- `../01-Foundations/chunking-and-embedding-in-layman-terms.md`
- `../02-Implementation-Guide/files-created-and-why-they-matter.md`
- `../04-Roadmap/rag-hands-on-roadmap.md`
