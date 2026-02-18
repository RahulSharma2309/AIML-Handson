# Phase 2 — Classical Machine Learning (Months 4–5)

**Timeline:** Months 4–5  
**Audience:** Distributed systems architect (C#/.NET, K8s, microservices) transitioning into AI — **FreshHarvest-Market** and production ML.

---

## Phase Overview

This phase builds **classical machine learning** foundations—supervised learning, evaluation metrics, and production-ready pipelines—using the same rigor you apply to microservice design. You move from "ML as black box" to **model selection, feature engineering, and deployment as a K8s service**. The goal is to ship ML that fits your distributed systems mindset: versioned, observable, and scalable.

**In short:** Classical ML gives you **immediate business value** (recommendations, demand forecasting, fraud detection) and the **vocabulary** (loss, regularization, cross-validation) that carries into deep learning and MLOps.

---

## Timeline: Months 4–5

| Month | Focus | Main idea |
|-------|--------|-----------|
| **4** | Core algorithms | Linear Regression, Logistic Regression, KNN, Decision Trees, SVM |
| **5** | Ensemble methods, tuning, deployment | Random forests, pipelines, model versioning, K8s microservice |

---

## Folder Structure

```
Phase-2-Classical-ML/
├── README.md                                    ← You are here
├── 00-Key-Terms/
├── 01-Supervised-Learning/
├── 02-Evaluation-Metrics/
├── 03-ML-with-Python/
├── 04-Linear-Regression/
├── 05-Logistic-Regression/
├── 06-KNN/
├── 07-Decision-Trees-and-Random-Forests/
├── 08-SVM/
└── 09-Ensemble-Methods/
```

---

## Courses

| Course | Platform | Duration | Link |
|--------|----------|----------|------|
| Machine Learning | Andrew Ng, Coursera | ~60 hrs | [Coursera — Machine Learning](https://www.coursera.org/learn/machine-learning) |
| ML with Python | Udemy (currently enrolled) | — | Your current course |
| Hands-On ML with Scikit-Learn, Keras & TensorFlow | Aurélien Géron (book) | — | [O'Reilly](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) / [Amazon](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1492032646) |

---

## Topics Covered (Status)

| Topic | Folder | Status | Notes |
|-------|--------|--------|-------|
| Key terms & definitions | `00-Key-Terms` | ✅ Has notes | [01-key-terms-and-definitions.md](00-Key-Terms/01-key-terms-and-definitions.md) |
| Supervised learning | `01-Supervised-Learning` | ✅ Has notes | [01-what-is-supervised-learning.md](01-Supervised-Learning/01-what-is-supervised-learning.md) |
| Classification metrics | `02-Evaluation-Metrics` | ✅ Has notes | [01-classification-metrics.md](02-Evaluation-Metrics/01-classification-metrics.md) |
| Confusion matrix | `02-Evaluation-Metrics` | ✅ Has notes | [02-confusion-matrix.md](02-Evaluation-Metrics/02-confusion-matrix.md) |
| Regression metrics | `02-Evaluation-Metrics` | ✅ Has notes | [03-regression-metrics.md](02-Evaluation-Metrics/03-regression-metrics.md) |
| Scikit-learn overview | `03-ML-with-Python` | ✅ Has notes | [01-scikit-learn-overview.md](03-ML-with-Python/01-scikit-learn-overview.md) |
| Linear regression | `04-Linear-Regression` | 📋 Placeholder | — |
| Logistic regression | `05-Logistic-Regression` | 📋 Placeholder | — |
| KNN | `06-KNN` | 📋 Placeholder | — |
| Decision trees & random forests | `07-Decision-Trees-and-Random-Forests` | 📋 Placeholder | — |
| SVM | `08-SVM` | 📋 Placeholder | — |
| Ensemble methods | `09-Ensemble-Methods` | 📋 Placeholder | — |

---

## Existing Notes Index

| # | Topic | File |
|---|-------|------|
| 1 | Key terms | [00-Key-Terms/01-key-terms-and-definitions.md](00-Key-Terms/01-key-terms-and-definitions.md) |
| 2 | Supervised learning | [01-Supervised-Learning/01-what-is-supervised-learning.md](01-Supervised-Learning/01-what-is-supervised-learning.md) |
| 3 | Classification metrics | [02-Evaluation-Metrics/01-classification-metrics.md](02-Evaluation-Metrics/01-classification-metrics.md) |
| 4 | Confusion matrix | [02-Evaluation-Metrics/02-confusion-matrix.md](02-Evaluation-Metrics/02-confusion-matrix.md) |
| 5 | Regression metrics | [02-Evaluation-Metrics/03-regression-metrics.md](02-Evaluation-Metrics/03-regression-metrics.md) |
| 6 | Scikit-learn overview | [03-ML-with-Python/01-scikit-learn-overview.md](03-ML-with-Python/01-scikit-learn-overview.md) |

---

## Month 4 Plan: Core Algorithms

| Week | Topics | Notes location |
|------|--------|----------------|
| 4.1 | Linear regression (single/multiple), cost function, gradient descent | `04-Linear-Regression/` |
| 4.2 | Logistic regression, decision boundary, classification metrics | `05-Logistic-Regression/` |
| 4.3 | K-Nearest Neighbors; distance metrics; scaling | `06-KNN/` |
| 4.4 | Decision trees: splits, impurity (Gini, entropy), pruning | `07-Decision-Trees-and-Random-Forests/` |
| 4.5 | Support Vector Machines; kernels (linear, RBF); margin | `08-SVM/` |

---

## Month 5 Plan: Ensemble Methods, Tuning, Deployment

| Week | Topics | Notes location |
|------|--------|----------------|
| 5.1 | Random forests, bagging, feature importance | `07-Decision-Trees-and-Random-Forests/` |
| 5.2 | Ensemble methods: boosting, XGBoost, stacking | `09-Ensemble-Methods/` |
| 5.3 | Model tuning: pipelines, cross-validation, grid search | `03-ML-with-Python/`, `09-Ensemble-Methods/` |
| 5.4 | Model versioning, serialization (joblib, ONNX) | — |
| 5.5 | Deployment: REST API, container, K8s microservice | Mini-project |

---

## Key Deliverables

| # | Deliverable | Description |
|---|-------------|-------------|
| 1 | **Product recommendation engine** | Top-K recommendations (e.g. "customers who bought X also bought Y"); similarity or collaborative filtering; Scikit-learn or custom. |
| 2 | **Demand prediction model** | Predict demand (e.g. units per SKU per week); linear regression or XGBoost; pipeline with scaling/encoding; report RMSE/MAE. |
| 3 | **K8s microservice deployment** | Expose recommendation or demand model via REST API; Docker + K8s Deployment/Service; health checks; runbook for model rollback. |

---

## Architecture Connection: How Classical ML Powers Production Systems

| Use case | How classical ML fits | FreshHarvest-Market angle |
|----------|------------------------|----------------------------|
| **Recommendation engines** | Similarity (cosine, Jaccard), matrix factorization, or tree-based rankers | "Customers who bought this also bought…"; product discovery. |
| **Demand forecasting** | Linear regression, ARIMA, or gradient boosting (XGBoost) for time series / tabular | Inventory, restocking, promo planning. |
| **Fraud detection** | Classification (logistic regression, trees, ensembles) on transaction/behavior features | Anomaly scores, risk rules. |

Classical ML is **interpretable**, **fast to train**, and often **sufficient for tabular and behavioral data**—ideal for e-commerce features before you add deep learning (Phase 3+) for images and text.

---

## Navigation

| Link | Description |
|------|-------------|
| [Phase 1 — Mathematical Foundations](../Phase-1-Mathematical-Foundations/README.md) | Prerequisites (math) |
| [Phase 3 — Deep Learning](../Phase-3-Deep-Learning/README.md) | Next phase |

---

*Next: [Phase 3 — Deep Learning](../Phase-3-Deep-Learning/README.md).*
