# Phase 5 — RAG & Agentic AI (Months 9–10)

## Phase Overview

**This is where your career multiplies.** You go from understanding AI to building AI-powered products. RAG and Agents are the two most in-demand skills in 2025–2026. Your distributed systems background—APIs, state, orchestration, failure handling—maps directly onto RAG pipelines and agent loops.

| Attribute | Value |
|-----------|--------|
| **Timeline** | Months 9–10 |
| **Prerequisites** | Phase 4 (Transformers & LLMs); comfort with embeddings and LLM APIs |
| **Target outcome** | Ship RAG apps and agentic workflows; connect them to FreshHarvest-Market |

---

## Folder Structure

```
Phase-5-RAG-and-Agents/
├── README.md                      ← You are here
├── 01-Embeddings-and-Vector-DBs/ # Embedding models, indexing, similarity search
├── 02-RAG-Architecture/           # Chunking, retrieval, reranking, generation
├── 03-LangChain-and-Orchestration/ # Chains, LCEL, tool integration
└── 04-Agentic-AI/                # ReAct, planning, memory, tool schemas
```

---

## Courses & Resources

| Resource | Type | Notes |
|----------|------|--------|
| [LangChain & Vector Databases in Production](https://www.deeplearning.ai/short-courses/) | DeepLearning.AI short course | Production patterns for RAG and vector DBs |
| [Building Autonomous AI Agents](https://www.deeplearning.ai/short-courses/) | DeepLearning.AI short course | Agent design and tool use |
| [LangChain Documentation](https://python.langchain.com/docs/) | Docs | Chains, agents, retrievers, integrations |
| [LlamaIndex Documentation](https://docs.llamaindex.ai/) | Docs | Alternative RAG/retrieval framework; compare with LangChain |
| [Building RAG Applications](https://www.deeplearning.ai/short-courses/) | DeepLearning.AI short courses | End-to-end RAG design |
| [Pinecone Learning Center](https://www.pinecone.io/learn/) | Tutorials | Vector DB concepts and Pinecone usage |
| [Qdrant Documentation](https://qdrant.tech/documentation/) | Docs | Vector DB with filtering and hybrid search |

---

## Month 9 — RAG & LLM Apps

| Week | Focus | Topics |
|------|--------|--------|
| **1** | **Embeddings deep dive** | What are embeddings; embedding models (OpenAI, sentence-transformers, Cohere); dimensions and normalization |
| **2** | **Vector databases** | Pinecone, Qdrant, ChromaDB—indexing, similarity search (cosine, dot-product), metadata filtering, hybrid search |
| **3** | **RAG architecture** | Chunking strategies (semantic, recursive, fixed); retrieval; reranking; generation; evaluation (faithfulness, relevance) |
| **4** | **Build AI Shopping Assistant** | End-to-end RAG for FreshHarvest: catalog + FAQs + policies; conversation memory; deploy as a service |

---

## Month 10 — Agentic AI

| Week | Focus | Topics |
|------|--------|--------|
| **1** | **Agent fundamentals** | ReAct pattern (reason + act); tool calling / function calling; agent loops and error handling |
| **2** | **Planning & reasoning** | Chain-of-thought; tree-of-thought; multi-step workflows; when to use agents vs fixed pipelines |
| **3** | **Memory systems** | Short-term (conversation buffer); long-term (vector store); episodic memory for agents |
| **4** | **Build Inventory Management AI Agent** | Agent that can query stock, suggest reorders, and (simulated) trigger workflows for FreshHarvest |

---

## Key Deliverables

| Deliverable | Description |
|-------------|-------------|
| **RAG-powered search** | Semantic search over product catalog and docs; compare with keyword search |
| **AI Shopping Assistant** | RAG + conversation memory; answers product and policy questions for FreshHarvest |
| **Inventory Management AI Agent** | Agent with tools (inventory API, reorder logic); multi-step reasoning |
| **Pricing Analyzer** | Tool or agent that uses internal data + LLM to support pricing decisions |

---

## Architecture Connection: How RAG & Agents Power Production Systems

| Use case | RAG / Agent role |
|----------|-------------------|
| **Customer support bots** | RAG over KB + ticket history; agent for escalation and tool use (create ticket, check order) |
| **Internal knowledge bases** | RAG over docs, runbooks, Slack; agents for summarization and action (e.g. Jira, PagerDuty) |
| **Autonomous operations** | Agents that monitor, reason, and act (e.g. inventory reorder, anomaly response) |

Design these like microservices: clear boundaries, idempotency, observability, and fallbacks when the model is uncertain.

---

## Key Concepts to Master

| Concept | Why it matters |
|---------|----------------|
| **Chunking strategies** | Size and overlap affect recall and cost; semantic chunking vs fixed blocks |
| **Hybrid search** | Combine vector similarity with keyword/BM25; better for product IDs and exact terms |
| **Hallucination detection** | Confidence, citations, NLI-based faithfulness checks |
| **Guardrails** | Input/output validation; PII redaction; topic boundaries; use NeMo Guardrails or similar |
| **Agent loops** | Observe → reason → act → observe; design for timeouts and max steps |
| **Tool schemas** | OpenAPI/JSON Schema for tools; LLMs use these for function calling—same idea as API contracts |

---

## Navigation

- **Previous:** [Phase 4 — Transformers & LLMs](../Phase-4-Transformers-and-LLMs/README.md)
- **Next:** [Phase 6 — MLOps & AI Systems Architecture](../Phase-6-MLOps-and-AI-Architecture/README.md)
- **Root:** [ML-Notes](../README.md)
