# NLP Semantic Modeling: Practical Exercises

This repository contains practical Python exercises designed to accompany the lecture series on **Statistical & Machine Learning Models (Part 4)**. These exercises focus on the mechanics, strengths, and inherent limitations of traditional Bag-of-Words (BoW) architectures and how they paved the way for modern NLP.

## Table of Contents
1. [Exercise 1: Building a Bag-of-Words (BoW) Vectorizer from Scratch](#exercise-1)
2. [Exercise 2: The "Man Bites Dog" Fallacy](#exercise-2)
3. [Exercise 3: Zipf's Law and the Noise Floor](#exercise-3)
4. [Exercise 4: The Closed-World Problem (Out-of-Vocabulary)](#exercise-4)

---

<a name="exercise-1"></a>
## Exercise 1: Building a Bag-of-Words (BoW) Vectorizer from Scratch
**Concept:** Understanding the BoW workflow.
* **Goal:** Implement the tokenization and matrix creation process from scratch without high-level libraries.
* **Key Learning:** Observing the creation of sparse Document-Term Matrices and understanding how document structure is sacrificed for frequency counting.
* **Run:** `python ex1.py`

<a name="exercise-2"></a>
## Exercise 2: The "Man Bites Dog" Fallacy
**Concept:** Loss of Compositionality.
* **Goal:** Use `scikit-learn` to demonstrate that BoW vectors are identical for sentences with swapped word orders.
* **Key Learning:** Witnessing how the commutative property of BoW addition leads to the destruction of syntax—meaning is emergent from sequence, which BoW ignores.
* **Run:** `python ex2.py`

<a name="exercise-3"></a>
## Exercise 3: Zipf's Law and the Noise Floor
**Concept:** Statistical Imbalance in Language.
* **Goal:** Use `nltk` to analyze the frequency distribution of words in Shakespeare's *Hamlet*.
* **Key Learning:** Demonstrating that natural language follows a Power-Law distribution (Zipf's Law), where high-frequency "noise" words dominate the vector magnitude, creating a critical need for weighting schemes like TF-IDF.
* **Run:** `python ex3.py`

<a name="exercise-4"></a>
## Exercise 4: The Closed-World Problem (Out-of-Vocabulary)
**Concept:** Robustness and vocabulary constraints.
* **Goal:** Train a vectorizer on a small corpus and observe how it "perceives" new, modern acronyms not present in its training phase.
* **Key Learning:** Understanding the dangers of "Closed-World" assumptions in enterprise systems, where novel, domain-specific tokens are ignored by the model.
* **Run:** `python ex4.py`

---

## Requirements
* **Python 3.x**
* **Dependencies:**
  ```bash
  pip install numpy scikit-learn nltk matplotlib
