# AI/ML Skill Maturity Framework

> **1–10 scale** · Self-assessment · Production alignment · Last updated: _fill in_

---

## 1. Scoring Rubric (1–10)

| Level | Band | Meaning |
|-------|------|--------|
| **1–2** | **Awareness** | Heard of it; can describe at a high level. Knows when/where it’s used. Cannot implement without heavy guidance. |
| **3–4** | **Beginner** | Can follow tutorials and docs. Basic usage in familiar setups. Needs examples to extend or debug. |
| **5–6** | **Intermediate** | Can apply independently in new problems. Debugs issues and reads error messages. Can combine concepts with some design. |
| **7–8** | **Advanced** | Can architect solutions, choose trade-offs, and teach others. Comfortable with edge cases and production concerns. |
| **9–10** | **Expert** | Can innovate, contribute to the field or OSS, and set best practices. Deep intuition and rare bugs. |

---

## 2. Self-Assessment Table

_Score 1–10 for **Current** and **Target (12-month)**. **Phase** = roadmap month/phase where the skill is primarily learned._

### Math

| Skill | Current Score | Target Score (12-mo) | Phase Where Learned |
|-------|----------------|----------------------|----------------------|
| Linear Algebra | | | Month 1 |
| Probability & Statistics | | | Month 2 |
| Calculus & Optimization | | | Month 3 |

### Classical ML

| Skill | Current Score | Target Score (12-mo) | Phase Where Learned |
|-------|----------------|----------------------|----------------------|
| Supervised Learning Theory | | | Month 4–5 |
| Regression Models | | | Month 4–5 |
| Classification Models | | | Month 4–5 |
| Model Evaluation & Metrics | | | Month 4–5 |
| Feature Engineering | | | Month 4–5 |
| Scikit-Learn Proficiency | | | Month 4–5 |
| Data Preprocessing with Pandas | | | Month 4–5 |

### Deep Learning

| Skill | Current Score | Target Score (12-mo) | Phase Where Learned |
|-------|----------------|----------------------|----------------------|
| Neural Network Fundamentals | | | Month 6–7 |
| Backpropagation & Optimization | | | Month 6–7 |
| CNNs | | | Month 7 |
| RNNs & Sequence Models | | | Month 7 |
| PyTorch / TensorFlow | | | Month 6–7 |

### Transformers / LLMs

| Skill | Current Score | Target Score (12-mo) | Phase Where Learned |
|-------|----------------|----------------------|----------------------|
| Attention & Self-Attention | | | Month 8 |
| Transformer Architecture | | | Month 8 |
| Tokenization & Embeddings | | | Month 8–9 |
| Fine-Tuning & Transfer Learning | | | Month 8–9 |
| Prompt Engineering | | | Month 8–9 |

### RAG & Agents

| Skill | Current Score | Target Score (12-mo) | Phase Where Learned |
|-------|----------------|----------------------|----------------------|
| Vector Databases | | | Month 9 |
| RAG Pipeline Design | | | Month 9 |
| LangChain / LlamaIndex | | | Month 9 |
| Agent Architecture | | | Month 10 |
| Tool Calling & Planning | | | Month 10 |

### MLOps & Infrastructure

| Skill | Current Score | Target Score (12-mo) | Phase Where Learned |
|-------|----------------|----------------------|----------------------|
| Model Serving & APIs | | | Month 5, 11 |
| CI/CD for ML | | | Month 11 |
| Model Monitoring & Drift | | | Month 11 |
| Kubernetes for ML | | | Month 12 |
| GPU Scheduling & Scaling | | | Month 12 |
| Cost Optimization | | | Month 12 |

### Cross-Cutting

| Skill | Current Score | Target Score (12-mo) | Phase Where Learned |
|-------|----------------|----------------------|----------------------|
| Python for ML | | | Ongoing |
| Git & Version Control | | | Ongoing |
| System Design for AI | | | Month 10–12 |
| Technical Writing & Documentation | | | Ongoing |

---

## 3. Architecture Application Matrix

_How each skill area maps to production systems, with a **FreshHarvest E-commerce Platform** example._

| Skill Area | Production Application | Example: FreshHarvest E-commerce |
|------------|------------------------|----------------------------------|
| **Linear Algebra** | Embeddings, dimensionality reduction, similarity in vector spaces | Product embeddings for “similar items”; reduced-dim features for search. |
| **Probability & Statistics** | A/B tests, uncertainty estimates, anomaly detection | A/B tests for recommendations; confidence intervals for demand forecasts. |
| **Calculus & Optimization** | Training loops, hyperparameter tuning, gradient-based methods | Optimizing loss for demand model; tuning learning rates. |
| **Supervised Learning Theory** | Choosing model class, bias–variance, generalization | Picking regression vs classification for churn vs demand. |
| **Regression / Classification** | Demand forecasting, churn, propensity scores | Demand prediction; churn predictor; “buy again” classifier. |
| **Model Evaluation & Metrics** | Offline metrics, thresholds, business alignment | Precision/recall for recommendations; MAE/RMSE for demand. |
| **Feature Engineering** | Inputs that drive model performance | Time features, aggregates, user/product history for models. |
| **Scikit-Learn / Pandas** | End-to-end training and data pipelines | Preprocessing, training, and evaluation pipelines in Python. |
| **Neural Network Fundamentals** | Non-linear patterns, representation learning | Dense nets for tabular demand/churn; embeddings. |
| **Backpropagation & Optimization** | Stable training, convergence | Training product classifiers and demand models. |
| **CNNs** | Image and signal understanding | Product image classifier; visual search. |
| **RNNs / Sequence Models** | Time series and sequences | Demand over time; session-based recommendations. |
| **PyTorch / TensorFlow** | Custom models and deployment | Custom layers, export for serving. |
| **Attention & Transformers** | Long-context, sequence-to-sequence | Search relevance; query–product matching. |
| **Tokenization & Embeddings** | Text and multimodal inputs | Product titles/descriptions; semantic search. |
| **Fine-Tuning & Transfer Learning** | Domain-specific LLMs and models | Fine-tuned model for FreshHarvest product taxonomy. |
| **Prompt Engineering** | Reliable LLM behavior in apps | Product descriptions, FAQs, support chatbots. |
| **Vector Databases** | Semantic search, retrieval | “Find similar products”; RAG over catalog and docs. |
| **RAG Pipeline Design** | Grounded Q&A and search | Shopping assistant over catalog + policies. |
| **LangChain / LlamaIndex** | Orchestration of retrieval and LLMs | RAG flows; tool use for cart/checkout. |
| **Agent Architecture** | Multi-step reasoning and actions | Agent that browses, compares, suggests, and checks stock. |
| **Tool Calling & Planning** | APIs, DB, external services | Agent calling inventory API, cart API, search. |
| **Model Serving & APIs** | Real-time and batch inference | REST/gRPC endpoints for recommendations and demand. |
| **CI/CD for ML** | Reproducible, auditable model releases | Train → test → deploy pipeline; versioned models. |
| **Model Monitoring & Drift** | Reliability and data quality | Monitoring input drift and performance for demand/churn. |
| **Kubernetes for ML** | Scalable, resilient serving | ML services and batch jobs on K8s. |
| **GPU Scheduling & Scaling** | Cost-effective GPU use | Scaling inference and training on GPU nodes. |
| **Cost Optimization** | Budget and efficiency | Right-sizing instances; spot/preemptible; caching. |
| **Python for ML** | Scripts, notebooks, services | All training and serving code. |
| **Git & Version Control** | Code and config history | Repos for models, pipelines, and infra. |
| **System Design for AI** | End-to-end AI systems | Designing FreshHarvest ML stack (data → train → serve). |
| **Technical Writing & Documentation** | Runbooks, design docs, READMEs | Runbooks for pipelines; READMEs for repos. |

---

## 4. Quarterly Assessment Checkpoints

_Expected score bands by end of each quarter (assuming ~3 months per quarter)._

| Checkpoint | Months | Expected Focus | Typical Score Ranges |
|------------|--------|----------------|----------------------|
| **Q1** | 1–3 | Math foundations (Linear Algebra, Probability & Statistics, Calculus) | Math: 4–6; rest: 1–3 (awareness/beginner). |
| **Q2** | 4–6 | Classical ML + first Deep Learning | Classical ML: 4–6; DL fundamentals: 3–5; Math: 5–7. |
| **Q3** | 7–9 | Deep Learning (CNNs/RNNs), Transformers, RAG | DL: 5–6; Transformers/RAG: 4–6; Classical ML: 5–7. |
| **Q4** | 10–12 | Agents, MLOps, K8s/Infrastructure | Agents: 4–6; MLOps/Infra: 4–6; End-to-end system design: 5–6. |

**How to use:** At the end of each quarter, re-run the self-assessment and compare to these bands. Adjust study plan if you’re ahead or behind.

---

_End of Skill Maturity Framework_
