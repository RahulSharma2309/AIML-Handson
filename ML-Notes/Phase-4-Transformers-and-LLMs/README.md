# Phase 4 — Transformers & LLMs (Month 8)

## Phase Overview

**This is where modern AI lives.** Transformers are the architecture behind GPT, BERT, Claude, Gemini, and every major AI breakthrough since 2017. As a distributed systems architect, you already think in pipelines, scaling, and APIs—here you learn the *model* that powers the endpoints your systems will serve.

| Attribute | Value |
|-----------|--------|
| **Timeline** | Month 8 |
| **Prerequisites** | Phase 3 (Deep Learning), especially attention basics from sequence models |
| **Target outcome** | Understand and fine-tune transformer models; ship a classifier and sentiment API |

---

## Folder Structure

```
Phase-4-Transformers-and-LLMs/
├── README.md                    ← You are here
├── 01-Attention-Mechanism/      # Why attention, scaled dot-product, multi-head
├── 02-Transformer-Architecture/ # Encoder-decoder, positional encoding, layer norm
├── 03-BERT-and-GPT/             # Encoder-only vs decoder-only, when to use which
└── 04-Fine-Tuning/              # HuggingFace Trainer, tokenizers, LoRA/QLoRA
```

---

## Courses & Resources

| Resource | Type | Notes |
|----------|------|--------|
| [Natural Language Processing with Transformers](https://www.oreilly.com/library/view/natural-language-processing/9781098136789/) | Book (HuggingFace/O'Reilly) | Reference for implementation and best practices |
| [HuggingFace NLP Course](https://huggingface.co/learn/nlp-course) | Free course | Hands-on with `transformers`, tokenizers, pipelines |
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | Paper | The original transformer paper—read after Week 1 |
| [Andrej Karpathy — Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) | YouTube | Build a small GPT from scratch; solid intuition |
| [Jay Alammar — The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | Blog | Visual walkthrough of the architecture |

---

## Week-by-Week Plan

| Week | Focus | Topics |
|------|--------|--------|
| **1** | **Attention mechanism deep dive** | Why RNNs failed at long sequences; scaled dot-product attention; multi-head attention; query/key/value intuition |
| **2** | **Full transformer architecture** | Encoder-decoder stack; positional encoding (sinusoidal and learned); layer normalization; residual connections; feed-forward blocks |
| **3** | **BERT vs GPT** | Encoder-only vs decoder-only; masked LM vs causal LM; when to use which (classification, generation, retrieval) |
| **4** | **Fine-tuning & transfer learning** | HuggingFace Trainer; tokenizers (BPE, WordPiece); dataset preparation; LoRA/QLoRA for efficient fine-tuning |

---

## Key Deliverables

| Deliverable | Description |
|-------------|-------------|
| **Fine-tuned product classifier** | Train a small BERT (e.g. DistilBERT) on FreshHarvest product categories |
| **Sentiment analyzer API** | Expose a sentiment model via REST (e.g. FastAPI); integrate with review pipeline |
| **Hosted model on FastAPI** | One deployable service: load model, tokenize, infer, return JSON; think “microservice contract” |

---

## Architecture Connection: How Transformers Power Production Systems

| Use case | Role of transformers |
|----------|------------------------|
| **Semantic search** | Encoder models (e.g. sentence-transformers) produce embeddings for retrieval—foundation for Phase 5 RAG |
| **Chatbots & assistants** | Decoder/decoder-only models (GPT-style) for generation; you’ll serve these behind your APIs |
| **Content generation** | Product descriptions, recommendations, marketing copy—all decoder-based |
| **Code assistants** | Same architecture; different training data and tool use (Phase 5) |

Think of this phase as learning the *engine*; Phase 5 is where you wire it into *systems* (RAG, agents).

---

## Key Concepts to Master

| Concept | Why it matters |
|---------|----------------|
| **Self-attention** | Lets each token attend to all others; no fixed context window like RNNs |
| **Cross-attention** | Encoder→decoder attention in seq2seq; critical for translation, summarization |
| **Positional encoding** | Injects sequence order (transformers are otherwise permutation-invariant) |
| **Tokenization (BPE, WordPiece)** | Subword units; affects vocab size, sequence length, and inference cost |
| **Transfer learning** | Start from pretrained; fine-tune on your domain (e.g. FreshHarvest catalog) |
| **LoRA/QLoRA** | Efficient fine-tuning with fewer parameters; essential for shipping updated models without full retrains |

---

## Navigation

- **Previous:** [Phase 3 — Deep Learning](../Phase-3-Deep-Learning/README.md)
- **Next:** [Phase 5 — RAG & Agentic AI](../Phase-5-RAG-and-Agents/README.md)
- **Root:** [ML-Notes](../README.md)
