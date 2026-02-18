# Phase 6 — MLOps & AI Systems Architecture (Months 11–12)

## Phase Overview

**This is your differentiation zone.** Any developer can call an API. Very few can architect, deploy, monitor, and scale AI systems in production. Your distributed systems background—K8s, microservices, observability, SLOs—makes this your superpower. Here you close the loop: from data and training to serving, monitoring, and feedback.

| Attribute | Value |
|-----------|--------|
| **Timeline** | Months 11–12 |
| **Prerequisites** | All previous phases + existing K8s and distributed systems experience |
| **Target outcome** | Production AI platform on K8s: lifecycle, serving, scaling, observability, cost |

---

## Folder Structure

```
Phase-6-MLOps-and-AI-Architecture/
├── README.md                        ← You are here
├── 01-Model-Lifecycle/              # Experiment tracking, versioning, registry
├── 02-Model-Serving-and-Scaling/   # FastAPI, TorchServe, BentoML, autoscaling
├── 03-AI-Infrastructure-on-K8s/    # GPU scheduling, vLLM, TGI, KServe
└── 04-Observability-and-Cost/      # Metrics, token usage, drift, cost dashboards
```

---

## Courses & Resources

| Resource | Type | Notes |
|----------|------|--------|
| [MLOps Specialization](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops) | Coursera (DeepLearning.AI, Andrew Ng) | End-to-end MLOps concepts |
| [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) | Book (Chip Huyen) | Systems design for ML at scale |
| [MLflow Documentation](https://mlflow.org/docs/latest/index.html) | Docs | Experiment tracking, model registry, projects |
| [Kubeflow Documentation](https://www.kubeflow.org/docs/) | Docs | ML pipelines and training on K8s |
| [Made With ML](https://madewithml.com/) | Free MLOps course | Practical MLOps from training to deployment |
| [Seldon Core](https://docs.seldon.io/projects/seldon-core/) / [KServe](https://kserve.github.io/website/) | Docs | Model serving on Kubernetes |

---

## Month 11 — MLOps

| Week | Focus | Topics |
|------|--------|--------|
| **1** | **ML lifecycle & experiment tracking** | MLflow, Weights & Biases—runs, metrics, artifacts; model registry and stage promotion |
| **2** | **Data versioning & feature stores** | DVC for data and model versioning; Feast (or similar) for feature store concepts; train/serve consistency |
| **3** | **Model serving** | FastAPI, TorchServe, TF Serving, BentoML—contracts, batching, versioned endpoints |
| **4** | **CI/CD for ML** | GitHub Actions (or similar): trigger training on data/config changes; model tests; deploy to staging/prod |

---

## Month 12 — AI Infrastructure

| Week | Focus | Topics |
|------|--------|--------|
| **1** | **GPU scheduling in Kubernetes** | NVIDIA GPU Operator; node selectors; resource quotas; multi-tenant GPU sharing |
| **2** | **Model scaling** | Horizontal Pod Autoscaler; batch vs real-time inference; model sharding and multi-replica |
| **3** | **LLM-specific infrastructure** | vLLM, TGI; KV-cache; speculative decoding; LLM caching (e.g. GPTCache) for cost and latency |
| **4** | **Observability & cost** | Prometheus/Grafana for ML metrics; token usage and cost tracking; evaluation dashboards; alerts on drift and errors |

---

## Key Deliverables

| Deliverable | Description |
|-------------|-------------|
| **ML pipeline on K8s** | Training job (or pipeline) that runs on K8s, logs to MLflow, and registers the model |
| **LLM microservice with autoscaling** | One LLM endpoint (e.g. vLLM or TGI) on K8s with HPA and GPU scheduling |
| **Evaluation dashboard** | Dashboard (e.g. Grafana) for accuracy, latency, token usage, and business metrics |
| **Cost monitoring** | Track cost per model, per endpoint, per tenant; set budgets and alerts |

---

## Architecture: Production AI Platform on K8s

This phase *is* the architecture. Below is a high-level flow you will implement or align with.

```
                    ┌─────────────────────────────────────────────────────────────────────────┐
                    │                    PRODUCTION AI PLATFORM (Kubernetes)                    │
                    └─────────────────────────────────────────────────────────────────────────┘

  ┌──────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────────┐
  │   INGESTION  │────▶│  FEATURE STORE  │────▶│    TRAINING     │────▶│   MODEL REGISTRY     │
  │ (events,     │     │ (Feast / custom)│     │ (Kubeflow /     │     │ (MLflow / custom)   │
  │  batch)     │     │ versioned feats │     │  GPU jobs)      │     │ version + stage      │
  └──────────────┘     └─────────────────┘     └────────┬────────┘     └──────────┬───────────┘
        │                         │                         │                         │
        │                         │                         │                         ▼
        │                         │                         │              ┌─────────────────────┐
        │                         │                         │              │      SERVING        │
        │                         │                         │              │ (KServe / Seldon /   │
        │                         │                         │              │  vLLM / TGI)        │
        │                         │                         │              │ autoscale, GPU       │
        │                         │                         │              └──────────┬───────────┘
        │                         │                         │                         │
        │                         │                         │                         ▼
        │                         │                         │              ┌─────────────────────┐
        │                         │                         └─────────────▶│    MONITORING       │
        │                         │                                        │ (Prometheus,        │
        │                         │                                        │  latency, drift,     │
        │                         │                                        │  token cost)        │
        │                         │                                        └──────────┬───────────┘
        │                         │                                                   │
        │                         │                         ┌──────────────────────────┘
        │                         │                         │
        │                         ▼                         ▼
        │              ┌─────────────────────┐     ┌─────────────────────┐
        └─────────────▶│   FEEDBACK LOOP    │◀────│  EVALUATION &       │
                       │ (labels, outcomes, │     │  A/B TESTING        │
                       │  corrections)      │     │ (canary, shadow)    │
                       └─────────────────────┘     └─────────────────────┘
```

**Design principles you already know:** stateless serving where possible, versioned contracts, feature consistency between train and serve, and observability at every stage.

---

## Key Concepts to Master

| Concept | Why it matters |
|---------|----------------|
| **Model drift** | Performance degrades as the world changes; detect via ongoing evaluation and trigger retrains |
| **Data drift** | Input distribution shifts; monitor feature stats and alert; can invalidate model assumptions |
| **Shadow deployment** | Run new model in parallel, log predictions, compare with current model before switch |
| **Canary releases for models** | Route a small % of traffic to new model; compare latency and quality before full rollout |
| **A/B testing models** | Same idea as product A/B tests: measure business metrics per model variant |
| **Model versioning** | Every deployable model = immutable artifact + config; trace from data and code for reproducibility |

---

## Navigation

- **Previous:** [Phase 5 — RAG & Agentic AI](../Phase-5-RAG-and-Agents/README.md)
- **Root:** [ML-Notes](../README.md)
- **Back to roadmap:** [ML-Notes](../README.md)
