# Chunking and Embedding in Layman Terms

## Real-world analogy

Imagine a huge textbook.

- **Chunking** = tearing that textbook into small sticky notes, each note containing one clear idea.
- **Embedding** = giving each sticky note a location on a meaning map, so similar notes sit near each other.
- **Vector search** = asking a question and finding sticky notes closest in meaning (not just keyword match).

## Why chunking matters

If chunks are bad, retrieval is bad.

- Too small: answers lose context.
- Too large: chunks become generic and retrieval gets noisy.
- Mixed topics in one chunk: embedding is confused.

Goal: one chunk should answer one question clearly.

## Why embeddings matter

Embeddings convert text into numbers so machines can compare meaning.

Example:
- Query: "How does CI/CD release trigger work?"
- System finds chunks about triggers/release even if exact words differ.

## Why metadata matters

Metadata is like labels on folders:

- source file
- doc family/profile
- section title

It helps:
- explainability (show citation source)
- filtering (only operations docs)
- better debugging and trust

## What you used in this project

- Free local embedding model: `sentence-transformers/all-MiniLM-L6-v2`
- Chunk storage format: JSONL (one chunk per line)
- Vector DB/search: FAISS

## Significance of this setup

- No paid API needed to learn the core RAG mechanics.
- Fast iteration on your own docs.
- Enterprise-like pattern: profile-based chunking + metadata filters.
