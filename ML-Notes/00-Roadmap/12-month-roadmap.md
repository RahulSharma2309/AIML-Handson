# 12-Month AI/ML Learning Roadmap

**Target Identity:** AI-Native Distributed Systems Architect / GenAI Platform Engineer / LLM Systems Designer

**Background:** 10-year distributed systems architect (C#/.NET, microservices, Kubernetes) transitioning into AI-native systems engineering. E-commerce microservices platform: **FreshHarvest-Market** (GitHub).

---

## Roadmap Overview

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                    12-MONTH AI/ML LEARNING JOURNEY — 6 PHASES                             │
├──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────────┤
│   M1     │   M2     │   M3     │   M4     │   M5     │   M6     │   M7     │     M8       │
│ Linear   │ Prob &   │ Calculus │ Classical│ Classical│ Deep     │ Deep     │ Transformers │
│ Algebra  │ Stats    │ for ML   │ ML Core  │ ML Deploy│ Learning │ Learning │ & LLMs       │
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────────┤
│   M9     │   M10    │   M11    │   M12    │          │          │          │              │
│ LLM Apps │ Agentic  │ MLOps    │ AI       │          │          │          │              │
│ & RAG    │ AI       │          │ Infra    │          │          │          │              │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────────┘

PHASE 1: Math Foundations (M1–M3)
    → PHASE 2: Classical ML (M4–M5)
        → PHASE 3: Deep Learning (M6–M7)
            → PHASE 4: Transformers & LLMs (M8)
                → PHASE 5: RAG & Agents (M9–M10)
                    → PHASE 6: MLOps & AI Architecture (M11–M12)
```

---

# PHASE 1 — Mathematical Foundations (Months 1–3)

> **Goal:** Build the mathematical intuition required to understand neural networks, optimization, and probabilistic ML. No black boxes.

---

## MONTH 1 — Linear Algebra

### Learning Goals

| Goal | Description |
|------|-------------|
| **Conceptual** | Understand vectors, matrices, and linear transformations as the language of neural networks and embeddings |
| **Computational** | Implement dot products, matrix multiplication, and SVD in code |
| **Application** | Connect linear algebra to embedding-based search (vector similarity, attention) |

### Primary Course

| Resource | Provider | Type |
|----------|----------|------|
| **Mathematics for Machine Learning: Linear Algebra** | Imperial College London (Coursera) | Primary course |

### Exact Topics

| Topic | Why It Matters for AI/ML |
|-------|---------------------------|
| Vectors, vector operations, norms | Embeddings are vectors; similarity = geometry |
| Dot products, cosine similarity | Attention uses scaled dot product; retrieval uses cosine |
| Matrices, matrix multiplication | Neural layers = matrix multiply: y = Wx + b |
| Basis, span, linear transformations | Latent space, representation learning |
| Eigenvalues & eigenvectors | PCA, spectral methods, dimensionality reduction |
| SVD (Singular Value Decomposition) | Recommender factorizations, low-rank approximations |

### Why This Month Matters

```
Neural forward pass:     y = σ(Wx + b)                    ← matrix multiply + nonlinearity
Embedding similarity:    sim(a,b) = a·b / (‖a‖‖b‖)       ← dot product / cosine
Attention scores:        Attention(Q,K,V) ∝ softmax(QK^T/√d) V  ← scaled dot product
```

### Weekly Milestones (Week 1–4)

| Week | Focus | Milestones | Deliverables |
|------|--------|------------|--------------|
| **Week 1** | Vectors, vector operations, dot product, geometric interpretation | Complete Coursera Week 1; implement dot product and norm in Python | `vectors.py`: Vector class, dot product, norm, cosine similarity |
| **Week 2** | Matrices, multiplication, inverses, systems of linear equations | Solve Ax=b by hand for 2×2; implement matrix multiply from scratch | `matrices.py`: Matrix multiply, inverse (small), SVD wrapper |
| **Week 3** | Basis, span, transformations, change of basis | Explain how a linear map changes coordinates; 2D transformation demo | Notes + small demo script for 2D transformations |
| **Week 4** | Eigenvalues, eigenvectors, SVD intuition, PCA preview | Compute top-2 PCA by hand on small matrix; SVD in NumPy | `pca_demo.py`: PCA from SVD on toy data |

### Implementation Tasks

- [ ] Implement a `Vector` class with `dot`, `norm`, `cosine_similarity`
- [ ] Implement matrix multiplication from scratch (no NumPy for core algo)
- [ ] Use NumPy SVD to compute PCA on a small dataset; plot first 2 components
- [ ] Build product embedding representation (e.g., category + price bins → vector)
- [ ] Implement brute-force top-K similarity search over product embeddings

### Mini-Project: Vector Similarity Search (FreshHarvest-Market)

| Item | Description |
|------|-------------|
| **Objective** | Implement cosine similarity manually in Python; store product embeddings and compute similarity for FreshHarvest catalog |
| **Scope** | Small product catalog (100–500 items); precomputed or simple embeddings (category + price bins, or manual feature vector) |
| **Output** | Script that, given a product ID, returns top-K similar products with similarity scores |
| **Tech** | Python, NumPy; no sklearn for similarity (implement from scratch) |

### Production Deliverable

- A **similarity search module** that can be called from a service: input `product_id`, output list of `(product_id, similarity_score)`. Document API contract for future integration into FreshHarvest-Market search/recommendation service.

### GitHub Portfolio Artifact

```
FreshHarvest-Market/  (or repo: linear-algebra-from-scratch/)
├── ml-foundations/
│   ├── vectors.py              # Vector class, dot product, norm, cosine similarity
│   ├── matrices.py             # Matrix multiply, inverse (small), SVD wrapper
│   ├── pca_demo.py             # PCA from SVD on toy data
│   └── similarity_search/      # Mini-project: product embeddings + similarity
│       ├── embeddings.py       # Build product embeddings (FreshHarvest schema)
│       ├── search.py           # Top-K similarity search
│       └── README.md           # How to run, link to FreshHarvest
└── README.md
```

### Evaluation Criteria

- [ ] Explain in one paragraph how matrix multiplication appears in a single neural layer
- [ ] Implement cosine similarity and use it to find similar vectors in O(n) for n items
- [ ] Describe how embedding-based search scales (brute-force vs approximate indexes) in a production context
- [ ] Run similarity search on FreshHarvest product set and document one example query + results

---

## MONTH 2 — Probability & Statistics

### Learning Goals

| Goal | Description |
|------|-------------|
| **Conceptual** | Model uncertainty; connect distributions to likelihoods and training objectives |
| **Computational** | Derive MLE for common distributions; implement logistic regression from scratch |
| **Application** | Churn probability, A/B testing, model evaluation (precision, recall, ROC) |

### Primary Course

| Resource | Provider | Type |
|----------|----------|------|
| **Mathematics for Machine Learning: Probability & Statistics** | Imperial College London (Coursera) | Primary |

### Exact Topics

| Topic | Why It Matters for AI/ML |
|-------|---------------------------|
| Random variables, PMF/PDF, CDF | Modeling outputs and uncertainties |
| Expectation, variance | Loss design, evaluation metrics |
| Gaussian, Bernoulli, Binomial, Poisson | Common likelihoods and priors |
| Bayes theorem, conditional probability | Naive Bayes, Bayesian inference |
| MLE (Maximum Likelihood Estimation) | Training objective; cross-entropy as MLE of Bernoulli |
| Hypothesis testing, confidence intervals | A/B tests, model comparison |

### Why This Month Matters

- **Logistic regression:** Binary classification as MLE of Bernoulli likelihood
- **Naive Bayes:** Text/classification with conditional independence
- **Model evaluation:** Accuracy, precision, recall, ROC; variance of metrics
- **Bias–variance tradeoff:** Underfitting vs overfitting

### Weekly Milestones (Week 1–4)

| Week | Focus | Milestones | Deliverables |
|------|--------|------------|--------------|
| **Week 1** | Random variables, PMF/PDF, CDF, expectation, variance | Derive E[X] and Var(X) for Bernoulli and Gaussian; code sampling | `distributions.py`: PMF/PDF/CDF for Bernoulli, Gaussian |
| **Week 2** | Common distributions (Bernoulli, Binomial, Gaussian, Poisson), CLT | When to use which; CLT demo with sample means | Add Binomial, Poisson; CLT demo script |
| **Week 3** | Bayes theorem, conditional probability, Bayesian thinking | Bayes by hand (e.g., medical test); posterior vs prior | `bayes_demo.py`: Bayes theorem examples |
| **Week 4** | MLE, MAP, hypothesis testing, confidence intervals | MLE for Gaussian mean; t-test for two means; bootstrap CI | `mle_map.py`: MLE for Gaussian, MAP with prior |

### Implementation Tasks

- [ ] Implement PMF/PDF/CDF for Bernoulli, Gaussian (and optionally Binomial, Poisson)
- [ ] Derive Bernoulli likelihood and show how maximizing it gives logistic regression
- [ ] Implement logistic regression from scratch (no sklearn for core algorithm): gradient ascent/descent on log-likelihood
- [ ] Train on churn dataset; report accuracy, precision, recall, ROC-AUC
- [ ] Design an A/B test (null, alternative, metric, sample size intuition) for a model change

### Mini-Project: Churn Probability Estimator (FreshHarvest-Market)

| Item | Description |
|------|-------------|
| **Objective** | Build a churn probability estimator; implement logistic regression from scratch |
| **Data** | Synthetic or public (e.g., Telco churn); features: tenure, usage, contract type (map to FreshHarvest: order frequency, basket size, subscription) |
| **Output** | Trained coefficients; predict P(churn); report accuracy, precision, recall, ROC-AUC |
| **Tech** | Python only for model; sklearn only for metrics/splits if desired |

### Production Deliverable

- **Churn probability API contract**: input (customer_id or feature vector), output P(churn). Document how this would plug into FreshHarvest-Market (e.g., retention campaign triggers).

### GitHub Portfolio Artifact

```
FreshHarvest-Market/  (or probability-stats-implementations/)
├── ml-foundations/
│   ├── distributions.py   # PMF/PDF/CDF for Bernoulli, Gaussian, etc.
│   ├── bayes_demo.py      # Bayes theorem examples
│   ├── mle_map.py         # MLE for Gaussian, MAP with prior
│   └── logistic_regression/
│       ├── model.py       # From-scratch logistic regression
│       ├── train.py       # Training loop, data load
│       ├── evaluate.py    # Metrics, ROC curve
│       └── README.md      # FreshHarvest churn use case
└── README.md
```

### Evaluation Criteria

- [ ] Write the Bernoulli likelihood and show how maximizing it gives logistic regression
- [ ] Design an A/B test (null, alternative, metric, sample size intuition) for a model change
- [ ] Explain how you would monitor a production classifier (metrics, confidence, drift)
- [ ] Deliver trained churn model with reported metrics and one paragraph on FreshHarvest integration

---

## MONTH 3 — Calculus for ML

### Learning Goals

| Goal | Description |
|------|-------------|
| **Conceptual** | Gradients as direction of steepest ascent; chain rule as backpropagation |
| **Computational** | Implement gradient descent (batch, SGD, mini-batch); visualize convergence |
| **Application** | Loss minimization, learning rates, batch size vs convergence |

### Primary Courses

| Resource | Provider | Type |
|----------|----------|------|
| **Essence of Calculus** | 3Blue1Brown (YouTube) | Intuition |
| **Mathematics for ML: Multivariate Calculus** | Imperial College London (Coursera) | Primary |

### Exact Topics

| Topic | Why It Matters for AI/ML |
|-------|---------------------------|
| Derivatives, rules of differentiation | Rate of change of loss w.r.t. parameters |
| Partial derivatives, gradients | ∇L(θ) for multi-parameter models |
| Chain rule, computation graphs | Backpropagation = chain rule on a graph |
| Gradient descent (batch, SGD, mini-batch) | How neural nets are trained |
| Optimization landscape (convex, saddle) | Why initialization and learning rate matter |

### Why This Month Matters

- **Backpropagation:** Application of chain rule to computation graph
- **Loss minimization:** Gradient descent and variants (learning rate, momentum, Adam)
- **Training infrastructure:** Batch size ↔ throughput vs convergence; GPU for matrix ops

### Weekly Milestones (Week 1–4)

| Week | Focus | Milestones | Deliverables |
|------|--------|------------|--------------|
| **Week 1** | Derivatives, rules of differentiation, intuition | Derivative of polynomial, exp, log; tangent line = direction of steepest ascent | Notes + small derivative exercises in code |
| **Week 2** | Partial derivatives, gradients, directional derivatives | ∇f(x,y) by hand; gradient points uphill; implement gradient for 2D function | `derivatives.py`: numerical/symbolic gradient for toy functions |
| **Week 3** | Chain rule, computation graphs, backpropagation math | Draw 2-layer net as graph; write ∂L/∂W for one layer symbolically | Hand-written derivation + 1-page doc |
| **Week 4** | Gradient descent variants (batch, SGD, mini-batch), learning rate, convergence | Code GD, SGD, mini-batch GD; plot loss curves; try different learning rates | `gradient_descent.py`, `linear_regression_gd.py`, visualizations |

### Implementation Tasks

- [ ] Implement numerical gradient for a scalar function of 2 variables
- [ ] Implement batch, stochastic, and mini-batch gradient descent
- [ ] Fit linear regression (y = Wx + b) using GD only (MSE loss)
- [ ] Visualize convergence: 2D contour plot of loss with trajectory overlay
- [ ] Compare convergence on convex bowl vs saddle (if time)

### Mini-Project: Gradient Descent from Scratch + Visualize Convergence

| Item | Description |
|------|-------------|
| **Objective** | Implement gradient descent from scratch; visualize convergence on different loss surfaces |
| **Output** | Script that runs GD/SGD on a simple loss (e.g., linear regression MSE); 2D contour plot of loss with trajectory overlay |
| **Link to FreshHarvest** | Optional: use a tiny slice of FreshHarvest data (e.g., price vs demand) for linear fit |

### Production Deliverable

- **Reusable gradient descent module** with batch/SGD/mini-batch options and logging of loss per step. Document how this translates to “training infrastructure” (batch size, iteration count, GPU vs CPU).

### GitHub Portfolio Artifact

```
FreshHarvest-Market/  (or calculus-gradient-descent/)
├── ml-foundations/
│   ├── derivatives.py         # Symbolic or numerical gradients for toy functions
│   ├── gradient_descent.py    # Batch, SGD, mini-batch
│   ├── visualizations/        # Loss surfaces and trajectories
│   ├── linear_regression_gd.py # Fit y = Wx + b with GD
│   └── README.md
└── README.md
```

### Evaluation Criteria

- [ ] Derive ∂L/∂W for one layer (e.g., linear layer + MSE)
- [ ] Explain the tradeoff between batch size, iteration count, and convergence
- [ ] Justify when to use GPU (large matrix multiplies) vs CPU (small models, preprocessing)
- [ ] Produce at least one convergence plot and one contour plot with trajectory

---

### PHASE 1 — Supplementary Resources

| Type | Resource | Use |
|------|----------|-----|
| YouTube | 3Blue1Brown — Linear Algebra, Essence of Calculus | Visual intuition |
| YouTube | StatQuest — Statistics Fundamentals | Probability & stats intuition |
| Blog | Distill.pub — Linear Algebra, Calculus | Clear explanations |
| Book | *Linear Algebra and Its Applications* (Gilbert Strang) | Reference |
| Paper | “Matrix Calculus” (Wikipedia / Petersen) | Chain rule reference |

### PHASE 1 — Architecture-Level Application

| Knowledge Area | How It Maps to Production AI Systems |
|----------------|--------------------------------------|
| **Linear algebra** | Embedding-based search: vector DBs, similarity indexes, scaling (brute-force vs HNSW/IVF). Understanding why “embedding + similarity” is the backbone of RAG and recommendations. |
| **Probability & statistics** | A/B testing framework design; probabilistic model monitoring (drift, confidence intervals on metrics); defining “good” via precision/recall/ROC. |
| **Calculus** | Training infrastructure: batch size, GPU vs CPU, memory, distributed training; interpreting loss curves and learning rate schedules. |

### PHASE 1 — Checkpoint Criteria (How to Know You’ve Mastered It)

- [ ] **Linear algebra:** Explain in 2 minutes how a single neural layer is a matrix multiply + nonlinearity; implement and run cosine similarity search on 500+ vectors.
- [ ] **Probability & stats:** Derive logistic regression from Bernoulli MLE; design one A/B test and one monitoring plan for a classifier.
- [ ] **Calculus:** Derive gradients for a 2-layer MLP (symbolically or on paper); implement and tune GD/SGD and explain batch size vs convergence in one paragraph.

---

# PHASE 2 — Classical Machine Learning (Months 4–5)

> **Goal:** Implement and deploy classical ML models; connect to FreshHarvest-Market and Kubernetes experience.

---

## MONTH 4 — Core ML Algorithms

### Learning Goals

| Goal | Description |
|------|-------------|
| **Conceptual** | Linear/logistic regression, regularization, bias/variance, evaluation metrics, pipelines |
| **Computational** | Train and evaluate models with Scikit-learn; build recommendation and forecasting pipelines |
| **Application** | Product recommendation (collaborative filtering), demand prediction, microservice design |

### Primary Courses & Materials

| Resource | Provider | Type |
|----------|----------|------|
| **Machine Learning** | Andrew Ng (Coursera) | Primary |
| **Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow** | Aurélien Géron (Book) | Primary |
| **ML with Python** (Udemy, Scikit-learn based) | Udemy | Current / parallel |

### Exact Topics

| Topic | Relevance |
|-------|-----------|
| Linear regression, normal equation, gradient descent | Baseline, interpretability |
| Logistic regression, regularization (L1/L2) | Classification, overfitting control |
| Neural network basics (Ng) | Bridge to Phase 3 |
| SVM (linear and kernel) | High-dimensional classification |
| K-means | Clustering, segmentation |
| Bias/variance, evaluation metrics (accuracy, precision, recall, F1, RMSE, MAE) | Reliable evaluation |
| Pipelines, preprocessing | Reproducibility, productionization |
| Ensemble methods (trees, bagging intro) | Robustness |

### Weekly Milestones (Week 1–4)

| Week | Focus | Milestones | Deliverables |
|------|--------|------------|--------------|
| **Week 1** | Linear regression (analytical + GD), cost function, feature scaling | Implement or use sklearn; interpret coefficients; RMSE/R² | Trained linear regression; short report on coefficients |
| **Week 2** | Logistic regression, decision boundary, regularization (Ridge/Lasso) | Binary classifier; regularization strength vs overfitting | Regularized logistic model; learning curve plot |
| **Week 3** | SVMs: margin, kernel trick (RBF), C and gamma; K-means | SVM for non-linear data; when to use vs trees; clustering demo | SVM + K-means notebooks or scripts |
| **Week 4** | Decision trees (splits, impurity), Random Forest and bagging; pipelines | Train tree and small forest; feature importance; sklearn Pipeline | End-to-end pipeline: raw data → features → model |

### Implementation Tasks

- [ ] Build a collaborative filtering recommendation model (user-item matrix; matrix factorization or k-NN on embeddings)
- [ ] Evaluate with RMSE/MAE or ranking metric (e.g., NDCG, hit rate)
- [ ] Expose recommendations via REST API (e.g., “recommended for user X”, “similar to item Y”)
- [ ] Document how to deploy as a K8s microservice (Dockerfile, health checks)

### Mini-Project: Product Recommendation Engine (FreshHarvest-Market)

| Item | Description |
|------|-------------|
| **Objective** | Build a product recommendation engine using collaborative filtering |
| **Scope** | Small dataset (MovieLens or synthetic e-commerce interactions); map to FreshHarvest products/users |
| **Output** | API that returns “recommended for user X” or “similar to item Y”; model versioning plan |
| **Deployment** | Package as microservice (FastAPI); document K8s deployment |

### Production Deliverable

- **Recommendation microservice**: one or more endpoints (e.g., `GET /recommend?user_id=`, `GET /similar?product_id=`); Dockerfile; optional K8s Deployment + Service; README with runbook.

### GitHub Portfolio Artifact

```
FreshHarvest-Market/  (or recommendation-microservice/)
├── services/
│   └── recommendation-service/
│       ├── app/           # FastAPI app
│       ├── model/         # Training script, data load
│       ├── Dockerfile
│       ├── k8s/           # Deployment, Service (optional)
│       └── README.md      # Run locally + K8s
└── README.md
```

### Evaluation Criteria

- [ ] Train and evaluate a collaborative filtering model (RMSE/MAE or ranking metric)
- [ ] Expose recommendations via REST API and document it
- [ ] Describe how you would add health checks and readiness for K8s
- [ ] One paragraph on how recommendation service fits into FreshHarvest-Market architecture

---

## MONTH 5 — Advanced ML & Deployment

### Learning Goals

| Goal | Description |
|------|-------------|
| **Conceptual** | Ensemble methods (RF, gradient boosting), feature engineering, model versioning |
| **Computational** | Pipelines, cross-validation, hyperparameter tuning; export and load model artifacts |
| **Application** | Demand prediction for FreshHarvest; deploy as K8s microservice with model versioning |

### Exact Topics

| Topic | Relevance |
|-------|-----------|
| Random forests, gradient boosting (XGBoost/LightGBM) | Production tabular ML |
| Feature engineering, pipelines | Reproducibility, productionization |
| Model tuning (grid/random search), cross-validation | Reliable evaluation and hyperparameters |
| Model versioning, deployment patterns | MLOps basics |

### Weekly Milestones (Week 1–4)

| Week | Focus | Milestones | Deliverables |
|------|--------|------------|--------------|
| **Week 1** | Random forests in depth, hyperparameters; gradient boosting (XGBoost) | Train RF and XGBoost; compare on same dataset | Comparison report; best model chosen |
| **Week 2** | Feature engineering (encoding, scaling, temporal), sklearn Pipelines | End-to-end pipeline: raw data → features → model | Pipeline code; feature doc |
| **Week 3** | Cross-validation, grid/random search, metric choice | Tuned model with CV; report best params and validation score | Tuned model; validation metrics |
| **Week 4** | Model versioning (artifact store), deployment as microservice, basic monitoring | Versioned model artifact; deploy in container; log predictions (POC) | Versioned artifact; Docker + K8s; logging design |

### Implementation Tasks

- [ ] Build demand prediction model (units sold per product/week or similar) using XGBoost or LightGBM
- [ ] Create reproducible training pipeline (data → features → train → artifact)
- [ ] Version model (path or tag in artifact store; e.g., S3, GCS, or local with naming convention)
- [ ] Deploy model behind FastAPI; run in Docker and in K8s (Deployment + Service)
- [ ] Document rollback to a previous model version

### Mini-Project: Demand Prediction + Deploy as K8s Microservice (FreshHarvest-Market)

| Item | Description |
|------|-------------|
| **Objective** | Demand prediction model for e-commerce (units sold per product/week). Deploy as microservice in K8s; add model versioning |
| **Output** | Trained model (e.g., XGBoost), pipeline from raw data to prediction; API endpoint; Docker image; K8s Deployment + Service; short doc on model versioning |
| **Production** | API contract: input (product_id, optional features), output (predicted demand); versioned model load |

### Production Deliverable

- **Demand forecast microservice** running in K8s with versioned model artifact; README with runbook, rollback procedure, and placeholder for monitoring (latency, errors).

### GitHub Portfolio Artifact

```
FreshHarvest-Market/  (or demand-forecast-pipeline/)
├── services/
│   └── demand-forecast-service/
│       ├── data/           # Prep scripts
│       ├── pipeline/       # Feature pipeline, train script
│       ├── model_registry/ # Versioning strategy (paths/tags)
│       ├── app/            # FastAPI, model load
│       ├── Dockerfile
│       ├── k8s/            # Deployment, Service
│       └── README.md       # Runbook, versioning, rollback
└── README.md
```

### Evaluation Criteria

- [ ] Deliver a reproducible training pipeline and a versioned model artifact
- [ ] Run the model behind an API in a container and in K8s
- [ ] Explain one way to roll back to a previous model version
- [ ] Document where model artifacts are stored and how the service loads a specific version

---

### PHASE 2 — Supplementary Resources

| Type | Resource | Use |
|------|----------|-----|
| YouTube | StatQuest — ML algorithms | Quick intuition |
| Book | *Hands-On ML* (Géron) | End-to-end projects |
| Docs | Scikit-learn user guide | Pipelines, APIs |
| Blog | ML design patterns (Google) | Production patterns |

### PHASE 2 — Architecture-Level Application

| Area | Application |
|------|-------------|
| **Service boundary** | Recommendation and demand forecast as separate microservices; versioned APIs |
| **Scaling** | Stateless inference; horizontal pod scaling; caching recommendations |
| **Data** | Where user/item embeddings or model artifacts are stored; pipeline reproducibility |
| **Lifecycle** | Model versioning and rollback; health checks and readiness for K8s |

### PHASE 2 — Checkpoint Criteria

- [ ] Train and evaluate at least two classical ML models (e.g., collaborative filtering + XGBoost demand model)
- [ ] Deploy both as containerized services and document K8s deployment
- [ ] Implement model versioning for one service and document rollback

---

# PHASE 3 — Deep Learning (Months 6–7)

> **Goal:** Understand and implement neural networks, CNNs, and RNNs; connect to training infrastructure and deployment.

---

## MONTH 6 — Neural Networks & CNNs

### Learning Goals

| Goal | Description |
|------|-------------|
| **Conceptual** | Perceptron to MLP; backpropagation; regularization (L2, dropout); optimization (Adam, RMSProp) |
| **Computational** | Implement or use PyTorch/TensorFlow for MLP and CNN; train on product images |
| **Application** | Product image classifier for FreshHarvest; deploy with FastAPI |

### Primary Course

| Resource | Provider | Type |
|----------|----------|------|
| **Deep Learning Specialization** (Courses 1–3) | Andrew Ng (Coursera) | Primary |

### Exact Topics

| Topic | Relevance |
|-------|-----------|
| Perceptron, activation functions (ReLU, sigmoid, softmax) | Building blocks of NNs |
| Forward propagation, backward propagation | Training NNs |
| Regularization (L2, dropout), batch normalization | Stability and generalization |
| Optimization: SGD, momentum, Adam, RMSProp | Practical training |
| CNNs: conv, pooling, architectures | Vision in production |

### Weekly Milestones (Week 1–4)

| Week | Focus | Milestones | Deliverables |
|------|--------|------------|--------------|
| **Week 1** | Perceptron, MLP, activations; forward pass | Implement 2-layer MLP in NumPy or PyTorch from scratch (no autograd) | MLP code; forward pass verified |
| **Week 2** | Backpropagation, chain rule in layers | Backprop for MLP; gradient check | Backprop implementation; gradient check |
| **Week 3** | Regularization (dropout, L2), batch norm | Train on overfitting-prone data; compare with/without dropout | Comparison report; tuned model |
| **Week 4** | CNNs: conv, pooling; product image classifier | Train CNN on product images by category; evaluate | CNN model; accuracy on held-out set |

### Implementation Tasks

- [ ] Implement or use a CNN for image classification (e.g., PyTorch or TensorFlow)
- [ ] Use product images by category (e.g., fashion, electronics, produce) — FreshHarvest or public dataset
- [ ] Report accuracy (and optionally precision/recall per class)
- [ ] Create inference script; optional: wrap in FastAPI

### Mini-Project: Product Image Classifier (FreshHarvest-Market)

| Item | Description |
|------|-------------|
| **Objective** | Build a product image classifier using CNNs; dataset: product images by category |
| **Output** | Trained CNN; evaluation metrics; inference script; optional simple API |
| **Deployment** | Deploy with FastAPI (single or batch inference) |

### Production Deliverable

- **Image classification API**: input image(s), output category (and confidence). Dockerfile; document batch vs single image and latency/throughput tradeoff.

### GitHub Portfolio Artifact

```
FreshHarvest-Market/  (or product-image-classifier/)
├── ml-models/
│   └── product-image-classifier/
│       ├── data/           # Loader, augmentation
│       ├── model/           # CNN definition
│       ├── train.py
│       ├── evaluate.py
│       ├── inference.py
│       └── README.md
├── services/
│   └── image-classifier-api/  # FastAPI, Dockerfile
└── README.md
```

### Evaluation Criteria

- [ ] Implement or use a CNN and report accuracy on a held-out set
- [ ] Explain what dropout and batch norm do in one sentence each
- [ ] Describe batch size vs GPU memory and throughput tradeoff
- [ ] Ship inference script or API that can be called with an image

---

## MONTH 7 — RNNs & Sequence Models

### Learning Goals

| Goal | Description |
|------|-------------|
| **Conceptual** | RNN, LSTM, GRU; sequence-to-sequence; attention intro |
| **Computational** | Train RNN/LSTM on sequences (time-series or text); optional seq2seq/attention |
| **Application** | Review text generator (RNN) or time-series; deploy with FastAPI |

### Primary Course

| Resource | Provider | Type |
|----------|----------|------|
| **Deep Learning Specialization** (Courses 4–5) | Andrew Ng (Coursera) | Primary |

### Exact Topics

| Topic | Relevance |
|-------|-----------|
| RNNs, vanishing gradient; LSTM, GRU | Sequences (time-series, text) |
| Sequence-to-sequence, attention (high level) | Bridge to transformers |
| Transfer learning (ResNet backbone) | Vision production |

### Weekly Milestones (Week 1–4)

| Week | Focus | Milestones | Deliverables |
|------|--------|------------|--------------|
| **Week 1** | CNN recap; transfer learning (e.g., ResNet backbone) | Fine-tune pretrained model on product images | Transfer-learned classifier; accuracy |
| **Week 2** | RNN, vanishing gradient; LSTM/GRU | Train small RNN/LSTM on sequence data (time-series or text) | Trained RNN/LSTM; loss curve |
| **Week 3** | Seq2seq, attention mechanism (high level) | Read “Attention Is All You Need” abstract and intro; diagram encoder–decoder | 1-page summary + diagram |
| **Week 4** | Integration: review text generator or time-series | Mini-project: review text generator (character/word-level RNN) or demand forecasting with LSTM | Review generator or LSTM forecaster; README |

### Implementation Tasks

- [ ] Train an RNN or LSTM for either: (A) short review text generation (character or word-level), or (B) demand forecasting (compare to XGBoost)
- [ ] Explain the role of the hidden state in one paragraph
- [ ] Deploy one DL model (CNN or RNN) with FastAPI; document latency and batch behavior

### Mini-Project: Review Text Generator (FreshHarvest-Market)

| Item | Description |
|------|-------------|
| **Objective** | Short review text generator (character or word-level RNN); quality secondary to understanding the pipeline |
| **Alternative** | Time-series demand forecasting with LSTM; compare to XGBoost from Month 5 |
| **Output** | Trained model; inference script; optional API |
| **Deployment** | Deploy with FastAPI |

### Production Deliverable

- **Sequence model service**: either review generation or LSTM forecast endpoint; Dockerfile; one paragraph on challenges of serving autoregressive models at scale (latency, batching, state).

### GitHub Portfolio Artifact

```
FreshHarvest-Market/  (or demand-forecast-lstm/ / review-text-rnn/)
├── ml-models/
│   ├── review-text-rnn/      # or demand-forecast-lstm/
│   │   ├── model/
│   │   ├── train.py
│   │   ├── generate.py
│   │   └── README.md
│   └── ...
├── services/
│   └── sequence-model-api/   # FastAPI for RNN/LSTM
└── README.md
```

### Evaluation Criteria

- [ ] Use transfer learning to train an image model and report accuracy
- [ ] Train an RNN/LSTM and explain the role of the hidden state
- [ ] Describe one challenge of serving autoregressive sequence models at scale
- [ ] Ship at least one DL model (CNN or RNN) behind FastAPI with Docker

---

### PHASE 3 — Supplementary Resources

| Type | Resource | Use |
|------|----------|-----|
| Paper | “Attention Is All You Need” | Transformer intro |
| Blog | Jay Alammar — Visualizing RNNs, CNNs | Intuition |
| Book | *Deep Learning* (Goodfellow et al.) | Reference |
| YouTube | 3Blue1Brown — Neural networks | Intuition |

### PHASE 3 — Architecture-Level Application

| Area | Application |
|------|-------------|
| **Training** | GPU usage, batch size, epoch time; when to use GPU in production |
| **Inference** | Batch vs single request; latency vs throughput; GPU vs CPU |
| **Serving** | When to use CNNs vs classical ML for tabular; sequence model latency and state handling |

### PHASE 3 — Checkpoint Criteria

- [ ] Train and evaluate a CNN (product images) and an RNN/LSTM (text or time-series)
- [ ] Deploy at least one DL model with FastAPI and document tradeoffs
- [ ] Explain in one paragraph: batch size vs GPU memory and throughput; one challenge of autoregressive serving

---

# PHASE 4 — Transformers & LLMs (Month 8)

> **Goal:** Deep dive into transformer architecture and LLM engineering (tokenization, fine-tuning, serving).

---

## MONTH 8 — Transformers & LLMs

### Learning Goals

| Goal | Description |
|------|-------------|
| **Conceptual** | Attention mechanism, self-attention math, BERT/GPT architectures, pretraining vs fine-tuning |
| **Computational** | Tokenization (BPE, WordPiece); fine-tune model for classification/sentiment; host with FastAPI |
| **Application** | Product classification (title + description → category); sentiment analysis; production API |

### Primary Course & Materials

| Resource | Provider | Type |
|----------|----------|------|
| **Natural Language Processing with Transformers** | HuggingFace (Book + HuggingFace course) | Primary |
| **Attention Is All You Need** | Paper | Supplementary |
| **Jay Alammar’s illustrated guides** | Blog | Supplementary |

### Exact Topics

| Topic | Relevance |
|-------|-----------|
| Attention mechanism, self-attention, scaled dot-product | Core of transformers |
| Multi-head attention, positional encoding | Expressiveness and order |
| Encoder-only (BERT), decoder-only (GPT) | Model families |
| Tokenization (BPE, WordPiece), vocabulary | Input pipeline |
| Pretraining vs fine-tuning | When to fine-tune vs prompt |
| Fine-tuning for classification and sentiment | Downstream tasks |

### Weekly Milestones (Week 1–4)

| Week | Focus | Milestones | Deliverables |
|------|--------|------------|--------------|
| **Week 1** | Attention: Q, K, V; scaled dot-product; self-attention | Implement single-head self-attention in code; diagram | Self-attention code; 1-page diagram |
| **Week 2** | Multi-head attention, positional encoding, transformer block | Assemble block from HF or from scratch; run on dummy sequence | Transformer block demo; notes |
| **Week 3** | BERT vs GPT; tokenization (BPE) | Use tokenizer on sample text; run BERT and GPT-2 for fill-mask/generation | Tokenization examples; BERT/GPT-2 runs |
| **Week 4** | Fine-tuning: data, loss, eval; product classification + sentiment | Fine-tune small model (e.g., BERT/DistilBERT) on product category and sentiment; host with FastAPI | Fine-tuned model; eval metrics; FastAPI service |

### Implementation Tasks

- [ ] Implement or use self-attention; explain Q, K, V in one paragraph
- [ ] Fine-tune BERT-base or DistilBERT for: (1) product category (title + description → category), (2) sentiment analysis (reviews)
- [ ] Evaluate: accuracy, F1; document encoder-only vs decoder-only for these use cases
- [ ] Host model(s) with FastAPI; Dockerfile; document token limits and chunking

### Mini-Project: Fine-Tune for Product Classification + Sentiment (FreshHarvest-Market)

| Item | Description |
|------|-------------|
| **Objective** | Fine-tune a small transformer (e.g., BERT-base or DistilBERT) for product category classification and review sentiment analysis |
| **Output** | Fine-tuned model(s); evaluation (accuracy, F1); inference script; FastAPI host |
| **Production** | API: input text (product title/description or review), output category and/or sentiment |

### Production Deliverable

- **Transformer API**: at least one endpoint (e.g., classify product category, or sentiment); Dockerfile; short doc on model size vs latency and GPU memory.

### GitHub Portfolio Artifact

```
FreshHarvest-Market/  (or transformer-product-classifier/)
├── ml-models/
│   └── transformer-models/
│       ├── product-classifier/   # Fine-tune BERT for category
│       ├── sentiment-analysis/   # Fine-tune for sentiment
│       ├── tokenization_demos/
│       └── README.md
├── services/
│   └── transformer-api/         # FastAPI, Dockerfile
└── README.md
```

### Evaluation Criteria

- [ ] Implement or use self-attention and explain Q, K, V in one paragraph
- [ ] Fine-tune a HuggingFace model and report metrics for classification and/or sentiment
- [ ] Explain the difference between encoder-only and decoder-only for your use case
- [ ] Ship FastAPI service that returns category or sentiment; document token limits and one scaling consideration

---

### PHASE 4 — Supplementary Resources

| Type | Resource | Use |
|------|----------|-----|
| Paper | “Attention Is All You Need” | Full detail |
| Blog | Jay Alammar — The Illustrated Transformer | Visual guide |
| Docs | HuggingFace Transformers | Implementation |
| Course | HuggingFace NLP Course | Hands-on |

### PHASE 4 — Architecture-Level Application

| Area | Application |
|------|-------------|
| **Token limits** | Chunking for long documents; truncation strategies |
| **Model size** | Small vs large in production; latency and GPU memory |
| **Serving** | Caching repeated inputs; batch inference for cost/latency |

### PHASE 4 — Checkpoint Criteria

- [ ] Fine-tune at least one transformer (e.g., BERT/DistilBERT) for a FreshHarvest-relevant task
- [ ] Host it with FastAPI and document one production consideration (token limits, model size, or scaling)
- [ ] Explain self-attention (Q, K, V) and encoder-only vs decoder-only in writing

---

# PHASE 5 — RAG & Agents (Months 9–10)

> **Goal:** Design and build RAG systems and agentic workflows that integrate with FreshHarvest-Market.

---

## MONTH 9 — LLM Apps & RAG

### Learning Goals

| Goal | Description |
|------|-------------|
| **Conceptual** | Embeddings, vector DBs, RAG pipeline (index, retrieve, rerank, generate), prompt templates, memory |
| **Computational** | Index catalog in vector DB; build RAG pipeline; AI Shopping Assistant with conversation memory |
| **Application** | Replace or augment FreshHarvest search with RAG; AI Shopping Assistant |

### Primary Course

| Resource | Provider | Type |
|----------|----------|------|
| **LangChain & Vector Databases in Production** | DeepLearning.AI | Primary |

### Exact Topics

| Topic | Relevance |
|-------|-----------|
| Embeddings (open-source vs API) | Retrieval backbone |
| Vector DBs (Pinecone, Qdrant, ChromaDB) | Scalable similarity search |
| RAG pipeline: index, retrieve, rerank, generate | End-to-end RAG |
| Chunking strategies, metadata filtering | Quality and relevance |
| Prompt templates, conversation memory | UX and consistency |
| Agents (intro) | Bridge to Month 10 |

### Weekly Milestones (Week 1–4)

| Week | Focus | Milestones | Deliverables |
|------|--------|------------|--------------|
| **Week 1** | Embeddings (open-source vs API); vector DB setup | Index 1k+ documents in a vector DB; run similarity search | Indexed corpus; similarity search script |
| **Week 2** | Chunking (size, overlap, semantic); metadata | Compare chunking strategies; measure retrieval recall (manual or sample) | Chunking comparison doc; chosen strategy |
| **Week 3** | RAG pipeline: retrieve → rerank (optional) → prompt → LLM | End-to-end RAG on product catalog or docs | RAG pipeline code; example Q&A |
| **Week 4** | Prompt templates, history/memory; replace search | “AI Shopping Assistant”: question over catalog; optional conversation | AI Shopping Assistant; conversation memory; architecture doc |

### Implementation Tasks

- [ ] Ingest FreshHarvest product catalog (or subset) into a vector DB (Qdrant, ChromaDB, or Pinecone)
- [ ] Build RAG pipeline: query → embed → retrieve → (rerank) → prompt → LLM → answer
- [ ] Add prompt templates and conversation memory for multi-turn “AI Shopping Assistant”
- [ ] Document architecture: index, retrieval, model, API; compare two chunking strategies on a small eval set

### Mini-Project: Replace FreshHarvest Search with RAG + AI Shopping Assistant

| Item | Description |
|------|-------------|
| **Objective** | Replace or augment e-commerce search with RAG (product catalog as knowledge base). Add AI Shopping Assistant that answers product questions and suggests items. |
| **Output** | Indexed catalog; RAG pipeline; simple chat or Q&A interface; conversation memory; architecture diagram (ASCII) |
| **Production** | API or UI that can be integrated into FreshHarvest-Market front-end |

### Production Deliverable

- **RAG service**: endpoint(s) for “ask about products” and optional chat; document failure modes (retrieval misses, hallucination) and mitigation (rerank, grounding, prompts).

### GitHub Portfolio Artifact

```
FreshHarvest-Market/  (or rag-shopping-assistant/)
├── services/
│   └── rag-shopping-assistant/
│       ├── ingestion/      # Index catalog to vector DB
│       ├── pipeline/       # Retrieve, rerank, prompt, LLM
│       ├── memory/         # Conversation memory
│       ├── api/             # FastAPI or LangChain serve
│       ├── docs/            # Architecture diagram (ASCII)
│       └── README.md
└── README.md
```

### Evaluation Criteria

- [ ] Run RAG end-to-end and show one example query with retrieved context + answer
- [ ] Compare two chunking strategies with a small eval set
- [ ] Draw the RAG pipeline and list failure modes (e.g., retrieval misses, model hallucination) and one mitigation each
- [ ] Demonstrate AI Shopping Assistant with at least one multi-turn conversation using memory

---

## MONTH 10 — Agentic AI

### Learning Goals

| Goal | Description |
|------|-------------|
| **Conceptual** | Tool calling, planning, multi-step reasoning, memory systems, workflow orchestration |
| **Computational** | Build agent with 2+ tools; planning and re-plan on failure; optional multi-agent design |
| **Application** | Inventory management AI agent; auto-generate supplier orders; pricing trend analysis |

### Primary Course

| Resource | Provider | Type |
|----------|----------|------|
| **Building Autonomous AI Agents** | DeepLearning.AI (short courses) | Primary |

### Exact Topics

| Topic | Relevance |
|-------|-----------|
| Tool calling (function calling) | Agents that use APIs and tools |
| Planning, multi-step reasoning | Break goal into steps; execute and re-plan on failure |
| Memory (short/long-term) | Coherent multi-turn and cross-session behavior |
| Workflow orchestration, multi-agent (intro) | Production agent design |

### Weekly Milestones (Week 1–4)

| Week | Focus | Milestones | Deliverables |
|------|--------|------------|--------------|
| **Week 1** | Tool use: define tools, LLM chooses tool and args; execute and feed back | Agent that can query product API and answer user questions | Agent with 1–2 tools (e.g., get product, get stock) |
| **Week 2** | Planning: break goal into steps; execute and re-plan on failure | Agent that “plans” a small workflow (e.g., find product → check stock → suggest) | Planning demo; re-plan on failure |
| **Week 3** | Memory: summarize or store key facts; use in next turn | Add memory to agent; multi-turn coherent behavior | Agent with memory; example dialogue |
| **Week 4** | Multi-agent (optional): specialist agents + orchestrator | Design or implement inventory + pricing agents; orchestrator coordinates | Design doc or code: inventory agent, pricing agent, orchestrator |

### Implementation Tasks

- [ ] Build an inventory management AI agent with at least 2–3 tools: e.g., “get low-stock items”, “get pricing history”, “place order” (mock)
- [ ] Implement auto-generate supplier orders (rule-based or simple model) as a tool or sub-agent
- [ ] Implement or mock pricing trend analysis (tool or sub-agent)
- [ ] Document one risk (e.g., wrong tool, wrong args) and a mitigation; sketch tracing/logging for production

### Mini-Project: Inventory Management AI Agent (FreshHarvest-Market)

| Item | Description |
|------|-------------|
| **Objective** | Build an inventory management AI agent that can: auto-generate supplier orders (based on rules or model), auto-analyze pricing trends (using tool or sub-agent), and answer operator questions (RAG over inventory docs) |
| **Output** | Agent with at least 2–3 tools; optional dashboard or CLI; architecture doc |
| **Production** | Design for reliability (timeouts, retries, idempotency for orders); security (which tools, input validation, audit logging) |

### Production Deliverable

- **Agent service**: agent loop (ReAct or similar) with tools; mock or real APIs; README and architecture diagram; document reliability and security considerations.

### GitHub Portfolio Artifact

```
FreshHarvest-Market/  (or inventory-agent/)
├── services/
│   └── inventory-agent/
│       ├── tools/          # get_low_stock, get_pricing_history, place_order (mock)
│       ├── agent/          # ReAct or similar loop
│       ├── memory/         # If applicable
│       ├── docs/           # Architecture, risks, tracing
│       └── README.md
└── README.md
```

### Evaluation Criteria

- [ ] Demonstrate an agent that uses at least two tools correctly in one run
- [ ] Document one risk of agentic systems (e.g., wrong tool, wrong args) and a mitigation
- [ ] Sketch how you would trace and log agent decisions in production
- [ ] Deliver architecture diagram and one paragraph on reliability (timeouts, idempotency) and security (tool scope, audit)

---

### PHASE 5 — Supplementary Resources

| Type | Resource | Use |
|------|----------|-----|
| Course | LangChain docs — Agents | Implementation |
| Blog | Lilian Weng — LLM Agent survey | Theory and patterns |
| Docs | OpenAI / Anthropic — Tool use | API design |

### PHASE 5 — Architecture-Level Application

| Area | Application |
|------|-------------|
| **RAG** | When to use RAG vs fine-tuning; cost and freshness; vector DB choice; caching embeddings and responses |
| **Agents** | Reliability: timeouts, retries, idempotency for tool calls (e.g., orders) |
| **Security** | Which tools the agent can call; input validation and audit logging |
| **Observability** | Tracing agent steps and tool calls for debugging |

### PHASE 5 — Checkpoint Criteria

- [ ] Ship a RAG pipeline and an AI Shopping Assistant with conversation memory
- [ ] Ship an agent with at least two tools and document risks and mitigations
- [ ] Produce architecture diagrams and one paragraph each on RAG scaling and agent observability

---

# PHASE 6 — MLOps & AI Architecture (Months 11–12)

> **Goal:** Productionize LLM-powered services on Kubernetes with lifecycle, observability, and cost in mind.

---

## MONTH 11 — MLOps

### Learning Goals

| Goal | Description |
|------|-------------|
| **Conceptual** | Model lifecycle, data versioning, feature stores, model serving, CI/CD for ML, monitoring, drift detection |
| **Computational** | DVC or similar for versioning; CI pipeline that trains/tests/deploys; metrics and one dashboard |
| **Application** | Full lifecycle for one ML/LLM service; deploy to K8s with monitoring |

### Primary Course

| Resource | Provider | Type |
|----------|----------|------|
| **MLOps Specialization** | DeepLearning.AI (Coursera) | Primary |

### Exact Topics

| Topic | Relevance |
|-------|-----------|
| Model lifecycle | Reproducibility and reuse |
| Data versioning (DVC), feature stores | Reproducibility and reuse |
| Model serving (TFServing, Triton, vLLM/TGI) | Low-latency inference |
| CI/CD for ML (tests, training triggers, deployment gates) | Safe releases |
| Monitoring, drift detection | Reliability and quality |
| LLM-specific metrics | Evaluation in production |

### Weekly Milestones (Week 1–4)

| Week | Focus | Milestones | Deliverables |
|------|--------|------------|--------------|
| **Week 1** | Model and data versioning; feature store concepts; experiment tracking | DVC or similar for one project; document versioning strategy | Versioning setup; 1-page strategy doc |
| **Week 2** | Serving: TFServing/Triton vs dedicated LLM servers (vLLM, TGI); batching | Run one model in a serving stack; measure latency and throughput | Serving PoC; latency/throughput notes |
| **Week 3** | CI/CD: unit tests, integration tests, training pipeline, deploy pipeline | Pipeline that trains (or downloads), tests, and deploys to K8s | CI/CD pipeline (e.g., GitHub Actions); deploy to K8s |
| **Week 4** | Monitoring: latency, errors, drift; LLM caching; cost; evaluation dashboard | Add metrics and one dashboard; document alerting and rollback | Dashboard; alerting/rollback doc |

### Implementation Tasks

- [ ] Set up data/model versioning (DVC or path-based) for at least one project
- [ ] Run one model (classical or LLM) in a serving stack (e.g., vLLM or TGI for LLM); measure latency and throughput
- [ ] Build CI pipeline: build image, run tests, deploy to K8s (or staging)
- [ ] Add metrics (latency, errors, optional drift) and one dashboard (Grafana or simple UI); document rollback

### Mini-Project: MLOps Pipeline for One Service

| Item | Description |
|------|-------------|
| **Objective** | Apply MLOps practices to one existing service (e.g., demand forecast, RAG, or transformer API): versioning, serving, CI/CD, monitoring |
| **Output** | Versioned data/model; serving config; CI pipeline; dashboard; runbook with rollback |

### Production Deliverable

- **MLOps-ready service**: versioned artifacts, CI/CD that deploys to K8s, at least one dashboard and rollback procedure.

### GitHub Portfolio Artifact

```
FreshHarvest-Market/  (or mlops-pipeline/)
├── .github/workflows/   # CI: build, test, deploy
├── dvc/ or model_registry/  # Versioning
├── serving/             # vLLM/TGI or similar config (if LLM)
├── monitoring/          # Prometheus/OpenTelemetry, dashboard config
├── runbook.md           # Rollback, alerting
└── README.md
```

### Evaluation Criteria

- [ ] Document versioning strategy and use it for one project
- [ ] Run one model in a proper serving stack and report latency/throughput
- [ ] Have a CI pipeline that deploys to K8s (or staging)
- [ ] Expose at least one business or reliability metric and one dashboard; document rollback

---

## MONTH 12 — AI Infrastructure

### Learning Goals

| Goal | Description |
|------|-------------|
| **Conceptual** | GPU scheduling in K8s, model scaling, batch vs real-time inference, LLM caching, observability, cost optimization |
| **Computational** | Deploy LLM microservice in K8s with autoscaling; evaluation metrics dashboard |
| **Application** | Production-ready LLM service on K8s; autoscaling; evaluation dashboard; one-pager “AI-Native Architect” design |

### Primary Materials

| Resource | Type |
|----------|------|
| MLOps Specialization (continued) | Course |
| Kubernetes docs — GPU, HPA, resource limits | Docs |
| vLLM / TGI / similar — deployment guides | Docs |

### Exact Topics

| Topic | Relevance |
|-------|-----------|
| GPU scheduling in K8s (node pools, resource requests/limits) | Cost and performance |
| Model scaling (horizontal pod autoscaling, scale-to-zero) | Cost and latency |
| Batch vs real-time inference | When to use which |
| LLM caching (prompt/response) | Cost and latency |
| Observability (traces, logs, metrics) | Debugging and SLOs |
| Cost optimization (spot, reserved, token-based) | Production at scale |

### Weekly Milestones (Week 1–4)

| Week | Focus | Milestones | Deliverables |
|------|--------|------------|--------------|
| **Week 1** | GPU scheduling in K8s; node pools; resource requests/limits | Deploy GPU workload (or document for CPU-only); bin-packing considerations | K8s manifest with GPU (or doc); resource doc |
| **Week 2** | Autoscaling (HPA, KEDA); batch vs real-time | Configure HPA or KEDA for LLM service; document batch vs real-time use cases | Autoscaling config; 1-page design |
| **Week 3** | LLM caching; observability (traces, metrics) | Add caching for prompts/responses; add or refine metrics and traces | Caching design; observability diagram |
| **Week 4** | Evaluation dashboard; cost; one-pager | Build evaluation dashboard (sample prompts, expected behavior, or latency percentiles); cost notes; final one-pager | Dashboard; cost doc; one-pager |

### Implementation Tasks

- [ ] Deploy an LLM-powered microservice (e.g., sentiment, RAG, or agent) in a K8s cluster
- [ ] Configure autoscaling (HPA or KEDA) and document scaling triggers
- [ ] Add or use LLM caching (prompt/response) and document invalidation policy
- [ ] Build an evaluation metrics dashboard (e.g., sample prompts + expected outputs, or latency percentiles)
- [ ] Write a one-pager: “Design for an AI-Native Distributed Systems Architect: production GenAI on K8s” (lifecycle, serving, monitoring, cost)

### Mini-Project: Deploy LLM Microservice in K8s (FreshHarvest-Market)

| Item | Description |
|------|-------------|
| **Objective** | Deploy an LLM-powered microservice in a K8s cluster with autoscaling (HPA or KEDA), basic monitoring, and an evaluation dashboard |
| **Output** | K8s manifests (Deployment, Service, HPA, optional Ingress); Docker image; metrics (Prometheus/OpenTelemetry or cloud); dashboard (Grafana or simple UI); runbook; one-pager design doc |
| **Production** | GPU scheduling (if available), batch vs real-time, caching, cost optimization notes |

### Production Deliverable

- **Production-ready LLM service on K8s**: autoscaling, monitoring, evaluation dashboard, runbook, and one-pager summarizing lifecycle, serving, monitoring, and cost for an AI-native architect.

### Target State Architecture (ASCII)

```
                    ┌──────────────────────────────────────────────────────────────┐
                    │                    Kubernetes Cluster                           │
                    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐   │
                    │  │ Ingress /   │  │ LLM Service │  │ Vector DB           │   │
                    │  │ Gateway     │──│ (vLLM/TGI)  │  │ (Chroma/Qdrant)      │   │
                    │  └─────────────┘  │ + HPA/KEDA  │  └─────────────────────┘   │
                    │         │         └──────┬──────┘            │                │
                    │         │                │                   │                │
                    │         ▼                ▼                   ▼                │
                    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐   │
                    │  │ RAG/Agent   │  │ GPU Node    │  │ Monitoring          │   │
                    │  │ API         │  │ Pool        │  │ (Prometheus/        │   │
                    │  │ (FastAPI)   │  │             │  │  Grafana/Dashboard) │   │
                    │  └─────────────┘  └─────────────┘  └─────────────────────┘   │
                    │         │                │                   │                │
                    │         └────────────────┴───────────────────┘                │
                    └──────────────────────────────────────────────────────────────┘
```

### GitHub Portfolio Artifact

```
FreshHarvest-Market/  (or llm-k8s-production/)
├── services/
│   └── llm-production-service/
│       ├── app/              # FastAPI, model load, cache
│       ├── Dockerfile
│       ├── k8s/              # Deployment, Service, HPA, Ingress
│       ├── monitoring/       # Prometheus, dashboard config
│       ├── evaluation/       # Sample prompts, expected behavior, metrics
│       └── runbook.md
├── docs/
│   └── ai-native-architect-onepager.md   # Lifecycle, serving, monitoring, cost
└── README.md
```

### Evaluation Criteria

- [ ] Deploy the service to K8s and show it scales under load (manual or simple test)
- [ ] Expose at least one business or reliability metric and one dashboard
- [ ] Document rollback procedure and one failure scenario (e.g., model OOM, drift)
- [ ] Write one-pager: “Design for an AI-Native Distributed Systems Architect: production GenAI on K8s” (lifecycle, serving, monitoring, cost)

---

### PHASE 6 — Supplementary Resources

| Type | Resource | Use |
|------|----------|-----|
| Course | MLOps Specialization (DeepLearning.AI) | Full lifecycle |
| Docs | Kubernetes — GPU, HPA, resource management | Infrastructure |
| Blog | ML design patterns (Google), LLM production (Anthropic/OpenAI) | Patterns |
| Tools | DVC, MLflow, Weights & Biases, vLLM, TGI | Implementation |

### PHASE 6 — Architecture-Level Application

| Area | Application |
|------|-------------|
| **GPU scheduling** | Node pools, resource requests/limits, bin-packing |
| **Autoscaling** | Scale on RPS or queue depth; scale-to-zero for cost |
| **Caching** | Cache embeddings and frequent prompts; invalidation policy |
| **Cost** | Spot/preemptible for batch; reserved for latency-sensitive; token-based cost tracking |
| **Lifecycle** | Data and model versioning, CI/CD, rollback, drift detection |

### PHASE 6 — Checkpoint Criteria

- [ ] Deploy at least one LLM (or ML) service to K8s with autoscaling and monitoring
- [ ] Have a versioning strategy and CI/CD that deploys to K8s
- [ ] Produce evaluation dashboard and runbook with rollback
- [ ] Write and refine the “AI-Native Distributed Systems Architect” one-pager

---

# Summary: 12 Months to AI-Native Distributed Systems Architect

| Phase | Months | Focus | Key Outcome |
|-------|--------|--------|-------------|
| **1. Math** | 1–3 | Linear algebra, probability, calculus | No black boxes; implement similarity, logistic regression, gradient descent from scratch |
| **2. Classical ML** | 4–5 | Core ML, pipelines, deployment | Recommendation + demand forecast microservices on K8s; model versioning |
| **3. Deep Learning** | 6–7 | CNNs, RNNs, transfer learning | Product image classifier, review generator or LSTM; FastAPI deployment |
| **4. Transformers** | 8 | Attention, BERT/GPT, fine-tuning | Product classification + sentiment; transformer API |
| **5. RAG & Agents** | 9–10 | RAG, vector DBs, agents | RAG + AI Shopping Assistant; inventory management agent |
| **6. MLOps & Infra** | 11–12 | Lifecycle, serving, K8s, monitoring | LLM microservice on K8s; autoscaling; dashboard; one-pager |

**Target identity after 12 months:**  
**AI-Native Distributed Systems Architect / GenAI Platform Engineer / LLM Systems Designer** — capable of designing and articulating production GenAI systems on Kubernetes: data and model versioning, training and fine-tuning pipelines, serving (classical ML and LLMs), RAG and agents, observability, and cost-aware GPU and scaling decisions, all in the language of a cloud-native architect, with FreshHarvest-Market as the reference e-commerce platform.

---

*Document version: 2.0 | Last updated: February 2025*
