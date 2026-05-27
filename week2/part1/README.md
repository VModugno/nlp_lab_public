# NLP Foundations & Semantic Modeling: Exercises

This repository contains practical Python exercises designed to accompany the lecture series on **Representing Meanings with Math**. These exercises help bridge the gap between linguistic theory and computational implementation.

## Table of Contents
1. [Exercise 1: Pattern-Matching (RegEx)](#exercise-1)
2. [Exercise 2: Vector Spaces & Orthogonality](#exercise-2)
3. [Exercise 3: Semantic Networks (WordNet)](#exercise-3)

---

<a name="exercise-1"></a>
## Exercise 1: Pattern-Matching with Regular Expressions
**Concept:** Before statistical models, machines relied on human-provided rules to induce logic.
* **Goal:** Implement a pattern matcher to identify user intent (e.g., "I want to buy a product").
* **Key Learning:** Understanding how `RegEx` serves as a foundation for early conversational agents and dialogue engines.
* **Run:** `python ex1.py`

<a name="exercise-2"></a>
## Exercise 2: Vector Spaces & Orthogonality
**Concept:** Representing language in discrete vector spaces.
* **Goal:** Create one-hot vectors for a vocabulary and calculate their dot products.
* **Key Learning:** Proving the "Orthogonality Problem"—the mathematical reality that traditional discrete space sees synonyms (like 'car' and 'automobile') as completely unrelated (dot product = 0).
* **Run:** `python ex2.py`

<a name="exercise-3"></a>
## Exercise 3: Semantic Networks (WordNet)
**Concept:** Using human-annotated dictionaries to solve the limitations of vector spaces.
* **Goal:** Utilize `nltk` and `WordNet` to explore synonym sets (synsets) and hypernym trees.
* **Key Learning:** Understanding how explicit, human-curated knowledge graphs can successfully map synonyms to the same conceptual node, bypassing the mathematical flaws of discrete vectors.
* **Run:** `python ex3.py`

---

## Requirements
* **Python 3.x**
* **Libraries:** ```bash
  pip install numpy nltk
  
NLTK Data: The first time you run ex3.py, it will prompt you to download the WordNet database. Follow the in-script instructions to ensure the library is fully functional.
