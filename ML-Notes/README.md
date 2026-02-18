# AIML-Handson — AI/ML Learning Repository

> A 12-month structured journey from **Distributed Systems Architect** to **AI-Native Cloud Architect**, with comprehensive notes, hands-on projects, and production-grade deliverables.

---

## Target Identity (12 Months)

```
AI-Native Distributed Systems Architect
GenAI Platform Engineer
LLM Systems Designer
```

---

## Repository Structure

```
ML-Notes/
│
├── 00-Roadmap/
│   ├── 12-month-roadmap.md            ← Detailed month-by-month plan with weekly milestones
│   ├── progress-tracker.md            ← Notion-style tracking (courses, artifacts, reflections)
│   └── skill-maturity-framework.md    ← 1-10 scoring across 30+ skills with quarterly checkpoints
│
├── Phase-1-Mathematical-Foundations/   ← Months 1–3
│   ├── README.md                       ← Phase overview & course list
│   ├── Month-01-Linear-Algebra/        ← Vectors, matrices, eigenvalues, SVD
│   ├── Month-02-Probability-and-Statistics/  ← Bayes, distributions, MLE, bias-variance
│   └── Month-03-Calculus-for-ML/       ← Gradient descent, chain rule, optimization
│
├── Phase-2-Classical-ML/               ← Months 4–5
│   ├── README.md                       ← Phase overview & existing notes index
│   ├── 00-Key-Terms/                   ← ML, AI, Data Science, LLMs, GenAI, Agentic AI
│   ├── 01-Supervised-Learning/         ← Labeled data, train/test split, ML process
│   ├── 02-Evaluation-Metrics/          ← Accuracy, Precision, Recall, F1, Confusion Matrix, MAE/MSE/RMSE
│   ├── 03-ML-with-Python/              ← Scikit-learn workflow & code patterns
│   ├── 04-Linear-Regression/           ← (placeholder — notes to be added)
│   ├── 05-Logistic-Regression/         ← (placeholder)
│   ├── 06-KNN/                         ← (placeholder)
│   ├── 07-Decision-Trees-and-Random-Forests/  ← (placeholder)
│   ├── 08-SVM/                         ← (placeholder)
│   └── 09-Ensemble-Methods/            ← (placeholder)
│
├── Phase-3-Deep-Learning/              ← Months 6–7
│   ├── README.md                       ← Phase overview & Andrew Ng specialization guide
│   ├── 01-Neural-Network-Fundamentals/ ← Neurons, activation, backpropagation
│   ├── 02-CNNs/                        ← Convolutional neural networks
│   ├── 03-RNNs-and-Sequence-Models/    ← Recurrent networks, LSTMs
│   └── 04-Regularization-and-Optimization/  ← Dropout, batch norm, Adam
│
├── Phase-4-Transformers-and-LLMs/      ← Month 8
│   ├── README.md                       ← Phase overview & HuggingFace course guide
│   ├── 01-Attention-Mechanism/         ← Self-attention, multi-head attention
│   ├── 02-Transformer-Architecture/    ← Encoder-decoder, positional encoding
│   ├── 03-BERT-and-GPT/               ← Encoder-only vs decoder-only
│   └── 04-Fine-Tuning/                ← Transfer learning, LoRA, QLoRA
│
├── Phase-5-RAG-and-Agents/             ← Months 9–10
│   ├── README.md                       ← Phase overview & LangChain/Vector DB guide
│   ├── 01-Embeddings-and-Vector-DBs/   ← Embeddings, Pinecone, Qdrant, ChromaDB
│   ├── 02-RAG-Architecture/            ← Chunking, retrieval, reranking, generation
│   ├── 03-LangChain-and-Orchestration/ ← Chains, prompts, memory
│   └── 04-Agentic-AI/                 ← Tool calling, planning, autonomous agents
│
├── Phase-6-MLOps-and-AI-Architecture/  ← Months 11–12
│   ├── README.md                       ← Phase overview & production AI platform design
│   ├── 01-Model-Lifecycle/             ← MLflow, experiment tracking, versioning
│   ├── 02-Model-Serving-and-Scaling/   ← FastAPI, TorchServe, BentoML, autoscaling
│   ├── 03-AI-Infrastructure-on-K8s/    ← GPU scheduling, vLLM, KServe
│   └── 04-Observability-and-Cost/      ← Monitoring, drift detection, cost optimization
│
└── images/                             ← Shared diagrams and screenshots
    ├── confusion-matrix-diagram.png
    └── ml-process-diagram.png
```

---

## 12-Month Overview

| Month | Phase | Focus | Course | Deliverable |
|-------|-------|-------|--------|-------------|
| 1 | Mathematical Foundations | Linear Algebra | Imperial College (Coursera) | Vector Similarity Search Engine |
| 2 | Mathematical Foundations | Probability & Statistics | Imperial College (Coursera) | Customer Churn Predictor |
| 3 | Mathematical Foundations | Calculus & Optimization | 3Blue1Brown + Imperial (Coursera) | Gradient Descent Visualizer |
| 4 | Classical ML | Core Algorithms | Andrew Ng (Coursera) + Udemy | Product Recommendation Engine |
| 5 | Classical ML | Pipelines & Deployment | Géron Book + Scikit-learn | Demand Prediction Microservice (K8s) |
| 6 | Deep Learning | Neural Networks & Optimization | Deep Learning Specialization (Coursera) | Neural Network from Scratch |
| 7 | Deep Learning | CNNs & RNNs | Deep Learning Specialization (Coursera) | Product Image Classifier + Sentiment API |
| 8 | Transformers & LLMs | Attention, BERT, GPT, Fine-tuning | HuggingFace NLP Course | Fine-tuned Product Classifier |
| 9 | RAG & Agents | Embeddings, Vector DBs, RAG | DeepLearning.AI | AI Shopping Assistant (RAG) |
| 10 | RAG & Agents | Agentic AI | DeepLearning.AI | Inventory Management Agent |
| 11 | MLOps | Model Lifecycle & CI/CD | MLOps Specialization (Coursera) | ML Pipeline on K8s |
| 12 | AI Architecture | GPU Scheduling, Scaling, Observability | Self-directed + Docs | LLM Microservice with Autoscaling |

---

## Quick Navigation

### Roadmap & Tracking

| Document | Description |
|----------|-------------|
| [12-Month Roadmap](./00-Roadmap/12-month-roadmap.md) | Detailed month-by-month plan with weekly milestones |
| [Progress Tracker](./00-Roadmap/progress-tracker.md) | Course tracker, artifact checklist, weekly logs, reflections |
| [Skill Maturity Framework](./00-Roadmap/skill-maturity-framework.md) | 1-10 scoring across 30+ skills with quarterly checkpoints |

### Phase Landing Pages

| Phase | Months | Link |
|-------|--------|------|
| Phase 1: Mathematical Foundations | 1–3 | [README](./Phase-1-Mathematical-Foundations/README.md) |
| Phase 2: Classical ML | 4–5 | [README](./Phase-2-Classical-ML/README.md) |
| Phase 3: Deep Learning | 6–7 | [README](./Phase-3-Deep-Learning/README.md) |
| Phase 4: Transformers & LLMs | 8 | [README](./Phase-4-Transformers-and-LLMs/README.md) |
| Phase 5: RAG & Agents | 9–10 | [README](./Phase-5-RAG-and-Agents/README.md) |
| Phase 6: MLOps & AI Architecture | 11–12 | [README](./Phase-6-MLOps-and-AI-Architecture/README.md) |

### Existing Notes (Phase 2 — Currently In Progress)

| Topic | File |
|-------|------|
| Key Terms & Definitions | [ML, AI, Data Science, LLMs, GenAI, Agentic AI](./Phase-2-Classical-ML/00-Key-Terms/01-key-terms-and-definitions.md) |
| Supervised Learning | [Labeled data, training process, data splitting](./Phase-2-Classical-ML/01-Supervised-Learning/01-what-is-supervised-learning.md) |
| Classification Metrics | [Accuracy, Precision, Recall, F1-Score, TP/FP/TN/FN](./Phase-2-Classical-ML/02-Evaluation-Metrics/01-classification-metrics.md) |
| Confusion Matrix | [Deep dive with all 13 formulas + worked examples](./Phase-2-Classical-ML/02-Evaluation-Metrics/02-confusion-matrix.md) |
| Regression Metrics | [MAE, MSE, RMSE with examples](./Phase-2-Classical-ML/02-Evaluation-Metrics/03-regression-metrics.md) |
| Scikit-Learn Overview | [Workflow, fit/predict/score, complete code example](./Phase-2-Classical-ML/03-ML-with-Python/01-scikit-learn-overview.md) |

---

## All Courses in Order

| # | Course | Platform | Phase | Cost |
|---|--------|----------|-------|------|
| 1 | Mathematics for ML: Linear Algebra | Coursera (Imperial College) | 1 | Paid / Audit free |
| 2 | Mathematics for ML: Probability & Statistics | Coursera (Imperial College) | 1 | Paid / Audit free |
| 3 | Essence of Calculus | YouTube (3Blue1Brown) | 1 | Free |
| 4 | Mathematics for ML: Multivariate Calculus | Coursera (Imperial College) | 1 | Paid / Audit free |
| 5 | Machine Learning | Coursera (Andrew Ng / Stanford) | 2 | Paid / Audit free |
| 6 | ML with Python | Udemy | 2 | Paid (enrolled) |
| 7 | Hands-On ML with Scikit-Learn, Keras & TF | Book (Aurélien Géron) | 2 | Book purchase |
| 8 | Deep Learning Specialization (5 courses) | Coursera (Andrew Ng) | 3 | Paid / Audit free |
| 9 | NLP with Transformers | HuggingFace (free course + book) | 4 | Free / Book purchase |
| 10 | LangChain & Vector DBs in Production | DeepLearning.AI | 5 | Free |
| 11 | Building Autonomous AI Agents | DeepLearning.AI (short courses) | 5 | Free |
| 12 | MLOps Specialization | Coursera (DeepLearning.AI) | 6 | Paid / Audit free |
| 13 | Designing Machine Learning Systems | Book (Chip Huyen) | 6 | Book purchase |

---

## GitHub Portfolio Artifacts (Build Over 12 Months)

| # | Artifact | Phase | Tech Stack |
|---|----------|-------|------------|
| 1 | Vector Similarity Search Engine | 1 | Python, NumPy |
| 2 | Customer Churn Predictor | 1 | Python, logistic regression from scratch |
| 3 | Gradient Descent Visualizer | 1 | Python, Matplotlib |
| 4 | Product Recommendation Engine | 2 | Scikit-learn, collaborative filtering |
| 5 | Demand Prediction Microservice | 2 | Scikit-learn, FastAPI, Docker, K8s |
| 6 | Neural Network from Scratch | 3 | Python, NumPy |
| 7 | Product Image Classifier | 3 | PyTorch/TensorFlow, CNN |
| 8 | Review Sentiment Analyzer | 3-4 | HuggingFace Transformers, FastAPI |
| 9 | Fine-tuned Product Classifier | 4 | HuggingFace, LoRA |
| 10 | RAG-Powered AI Shopping Assistant | 5 | LangChain, Qdrant/Pinecone, OpenAI |
| 11 | Inventory Management AI Agent | 5 | LangChain Agents, tool calling |
| 12 | ML Pipeline on Kubernetes | 6 | MLflow, KServe, GitHub Actions |
| 13 | LLM Microservice with Autoscaling | 6 | vLLM, K8s HPA, Prometheus/Grafana |

---

## How to Use This Repository

1. **Start with the [12-Month Roadmap](./00-Roadmap/12-month-roadmap.md)** — understand the full journey
2. **Set up your [Progress Tracker](./00-Roadmap/progress-tracker.md)** — fill in start dates
3. **Take the [Skill Maturity Assessment](./00-Roadmap/skill-maturity-framework.md)** — score yourself today as a baseline
4. **Follow each Phase README** — they contain course links, weekly plans, and project specs
5. **Add your notes** — each topic folder has space for your own learning notes
6. **Build the portfolio artifacts** — commit them to this repo as you go
7. **Reassess quarterly** — update skill scores and reflect on progress

---

*This repository grows with your learning. Every lecture transcript, every code exercise, every project gets a home here.*
