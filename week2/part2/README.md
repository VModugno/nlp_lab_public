# NLP Semantic Modeling: Practical Exercises

This repository contains practical Python exercises designed to accompany the lecture series on **Vector Space Semantics & Modern Computational Modeling** (Part 2). These exercises are designed to help you bridge the gap between theoretical linguistic concepts and their computational implementation.

## Table of Contents
1. [Exercise 1: Co-occurrence Matrices & Cosine Similarity](#exercise-1)
2. [Exercise 2: PPMI Weighting](#exercise-2)
3. [Exercise 3: The Algebra of Semantic Meaning](#exercise-3)

---

<a name="exercise-1"></a>
## Exercise 1: Co-occurrence Matrices & Cosine Similarity
**Concept:** Vector Space Semantics.
* **Goal:** Implement the Cosine Similarity formula from scratch using `numpy`.
* **Learning Objective:** Understand why we use Cosine Similarity rather than Euclidean distance when comparing distributional vectors to ensure magnitude-invariant semantic measurement.
* **Run:** `python ex1.py`

<a name="exercise-2"></a>
## Exercise 2: PPMI Weighting
**Concept:** Transforming raw co-occurrence counts into significance weights.
* **Goal:** Implement the Positive Pointwise Mutual Information (PPMI) formula.
* **Learning Objective:** Learn how to statistically determine if target-context pairs co-occur significantly more often than would be expected by chance, effectively filtering out "statistical noise."
* **Run:** `python ex2.py`

<a name="exercise-3"></a>
## Exercise 3: The Algebra of Semantic Meaning
**Concept:** Dense Embeddings and Vector Arithmetic.
* **Goal:** Perform vector arithmetic (e.g., *King - Man + Woman*) to isolate independent semantic dimensions like Gender and Royalty.
* **Learning Objective:** Visualize how dense embeddings map complex human concepts into linear geometric relationships, proving that meaning can be computed mathematically.
* **Run:** `python ex3.py`

---

## Requirements
* **Python 3.x**
* **Dependencies:**
  ```bash
  pip install numpy
