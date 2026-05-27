# NLP Semantic Modeling: Practical Exercises

This repository contains practical Python exercises designed to accompany the lecture series on **Modern Machine Learning Architecture & The Frontier (Part 5)**. These exercises explore the transition from traditional, sparse representations to modern dense embeddings, contextual understanding, and multimodal alignment.

## Table of Contents
1. [Exercise 1: Sparse vs. Dense Embeddings](#exercise-1)
2. [Exercise 2: Contextual Embeddings (BERT)](#exercise-2)
3. [Exercise 3: Cross-Modal Alignment (CLIP)](#exercise-3)

---

<a name="exercise-1"></a>
## Exercise 1: Sparse vs. Dense Embeddings
**Concept:** Moving from Bag-of-Words to Dense Vectors.
* **Goal:** Compare the Cosine Similarity of synonyms ("coffee" and "tea") using sparse one-hot vectors versus dense, real-valued vectors.
* **Key Learning:** Proving the "Orthogonality Trap" in traditional sparse models and seeing how dense embeddings enable true semantic retrieval by clustering related concepts in vector space.
* **Run:** `python ex1.py`

<a name="exercise-2"></a>
## Exercise 2: Contextual Embeddings (BERT)
**Concept:** Solving the Polysemy Problem.
* **Goal:** Use a pre-trained BERT model to mask and predict words in different contexts (e.g., river bank vs. financial bank).
* **Key Learning:** Understanding how bidirectional training and attention mechanisms allow modern models to resolve ambiguity dynamically, moving beyond the limitations of static word vectors.
* **Run:** `python ex2.py`

<a name="exercise-3"></a>
## Exercise 3: Cross-Modal Alignment (CLIP)
**Concept:** Shared Latent Spaces in Multimodal AI.
* **Goal:** Simulate the contrastive learning process by calculating alignment scores between image vectors and text vectors.
* **Key Learning:** Discovering how forcing vision and text encoders into the same mathematical coordinate space enables models to "see" images and discuss them with human-like nuance.
* **Run:** `python ex3.py`

---

## Requirements
* **Python 3.x**
* **Dependencies:**
  ```bash
  pip install numpy transformers
