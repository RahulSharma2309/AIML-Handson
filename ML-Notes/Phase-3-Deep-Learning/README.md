# Phase 3 — Deep Learning (Months 6–7)

**Timeline:** Months 6–7  
**Audience:** Distributed systems architect (C#/.NET, K8s, microservices) transitioning into AI — **FreshHarvest-Market** and production DL.

---

## Phase Overview

This phase introduces **neural networks and deep learning**—the machinery behind modern computer vision, NLP, and generative models. You go from perceptrons to **CNNs and RNNs**, with a focus on how these models are trained (forward/backward pass, optimizers), regularized (dropout, batch norm), and deployed. As an architect, you'll think about **GPU infrastructure, training pipelines, and distributed training** with the same rigor as designing a distributed data pipeline.

**In short:** Deep learning is where **scale and infrastructure** become first-class: GPU scheduling, checkpointing, and reproducibility matter as much as algorithm choice.

---

## Timeline: Months 6–7

| Month | Focus | Main idea |
|-------|--------|-----------|
| **6** | Neural network fundamentals | Backpropagation, optimization, regularization |
| **7** | CNNs & RNNs | Computer vision and sequence models; practical projects |

---

## Folder Structure

```
Phase-3-Deep-Learning/
├── README.md                                    ← You are here
├── 01-Neural-Network-Fundamentals/
├── 02-CNNs/
├── 03-RNNs-and-Sequence-Models/
└── 04-Regularization-and-Optimization/
```

---

## Courses

| Course | Platform | Duration | Link |
|--------|----------|----------|------|
| **Deep Learning Specialization** (5 courses) | Andrew Ng, Coursera | ~5 months part-time | [Coursera — Deep Learning](https://www.coursera.org/specializations/deep-learning) |

### Deep Learning Specialization — Course Breakdown

| # | Course name | Content |
|---|-------------|---------|
| 1 | Neural Networks and Deep Learning | Perceptron, shallow and deep nets, forward/backward prop, vectorization |
| 2 | Improving Deep Neural Networks | Regularization, dropout, batch norm; optimizers (Adam, etc.); tuning |
| 3 | Structuring Machine Learning Projects | Train/dev/test; bias-variance; error analysis; project workflow |
| 4 | Convolutional Neural Networks | Conv layers, padding, stride; CNNs; transfer learning; detection |
| 5 | Sequence Models | RNNs, LSTM, GRU; sequence-to-sequence; attention intro |

---

## Prerequisites

- **Phase 1 (Math):** Linear algebra (vectors, matrices, dot products), **calculus** (chain rule, gradients — essential for backprop), basic probability.
- **Phase 2 (Classical ML):** Supervised learning, loss functions, train/val/test splits, metrics (accuracy, F1, RMSE), pipelines.
- **Python:** NumPy; PyTorch or TensorFlow/Keras will be built in this phase.

---

## Month 6 Plan: Neural Network Fundamentals

| Week | Topics | Notes location |
|------|--------|----------------|
| 6.1 | Perceptron, activation functions (ReLU, sigmoid, softmax) | `01-Neural-Network-Fundamentals/` |
| 6.2 | Forward propagation; loss (cross-entropy, MSE); dimensions | `01-Neural-Network-Fundamentals/` |
| 6.3 | Backward propagation; chain rule; gradients w.r.t. weights/biases | `01-Neural-Network-Fundamentals/` |
| 6.4 | Regularization: L2, dropout; batch normalization | `04-Regularization-and-Optimization/` |
| 6.5 | Optimizers: SGD, momentum, RMSProp, Adam | `04-Regularization-and-Optimization/` |
| 6.6 | Training loop: batching, epochs, validation, early stopping | `01-Neural-Network-Fundamentals/` |

---

## Month 7 Plan: CNNs, RNNs, Practical Projects

| Week | Topics | Notes location |
|------|--------|----------------|
| 7.1 | Convolutional layers; padding, stride; feature maps; pooling | `02-CNNs/` |
| 7.2 | CNN architectures; transfer learning (e.g. ResNet, fine-tune head) | `02-CNNs/` |
| 7.3 | RNNs; LSTM, GRU; vanishing/exploding gradients | `03-RNNs-and-Sequence-Models/` |
| 7.4 | Sequence-to-one and sequence-to-sequence; padding, masking, batching | `03-RNNs-and-Sequence-Models/` |
| 7.5–7.6 | Projects: image classifier, review sentiment; FastAPI deployment | — |

---

## Key Deliverables

| # | Deliverable | Description |
|---|-------------|-------------|
| 1 | **Product image classifier** | Classify product images into categories (e.g. produce, dairy) using a CNN; transfer learning (e.g. ResNet) + custom head. |
| 2 | **Review sentiment model** | Classify or score review sentiment using an RNN/LSTM (or simple transformer later); embed + LSTM/GRU → sentiment. |
| 3 | **FastAPI deployment** | Serve the image classifier or sentiment model via FastAPI; containerize; health checks and simple versioning. |

---

## Architecture Connection: How Deep Learning Powers Production Systems

| Use case | How deep learning fits | FreshHarvest-Market angle |
|----------|------------------------|----------------------------|
| **Image recognition** | CNNs for local structure; transfer learning for limited data | Product photo tagging, category from image, quality checks. |
| **NLP / text** | RNNs/LSTMs (or transformers in Phase 4) for sequences | Review sentiment, search intent, support ticket routing. |
| **Recommendation ranking** | Neural rankers (embeddings + MLP) on top of classical retrieval | Re-rank "also bought" or "for you" lists. |

Deep learning adds **representation learning** (no need to hand-craft all features) and scales with **data and compute**—GPU infrastructure and training pipelines become part of your system design.

---

## Navigation

| Link | Description |
|------|-------------|
| [Phase 1 — Mathematical Foundations](../Phase-1-Mathematical-Foundations/README.md) | Math prerequisites (especially calculus for backprop) |
| [Phase 2 — Classical ML](../Phase-2-Classical-ML/README.md) | ML concepts prerequisite |
| Phase 4+ | Transformers & LLMs (next in roadmap) |

---

*Next: Phase 4 — Transformers & LLMs.*
