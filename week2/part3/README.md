# NLP Semantic Modeling: Practical Exercises

This repository contains practical Python exercises designed to accompany the lecture series on **Representing Meanings in Human-Annotated Dictionaries** (Part 3). These exercises explore how rule-based semantic systems, specifically WordNet, categorize language and enable logical reasoning in computational systems.

## Table of Contents
1. [Exercise 1: Exploring Synsets, Glosses, and Ambiguity](#exercise-1)
2. [Exercise 2: Navigating the Concept Hierarchy (ISA Relations)](#exercise-2)
3. [Exercise 3: Quantifying Proximity with Wu-Palmer Similarity (WUP)](#exercise-3)

---

<a name="exercise-1"></a>
## Exercise 1: Exploring Synsets, Glosses, and Ambiguity
**Concept:** WordNet handles lexical ambiguity by grouping meanings into distinct "synsets" (synonym sets). Each synset includes a "gloss," which provides a dictionary-style definition to disambiguate meaning.
* **Goal:** Use `nltk.corpus.wordnet` to retrieve all synsets for an ambiguous word like "bank" and inspect their unique definitions.
* **Key Learning:** Understanding that WordNet separates concepts like "financial institutions" and "river banks" into distinct, non-overlapping categories.
* **Run:** `python ex1.py`

<a name="exercise-2"></a>
## Exercise 2: Navigating the Concept Hierarchy (ISA Relations)
**Concept:** WordNet is structured as a Directed Acyclic Graph (DAG) where concepts are nodes and relations (like hypernymy/hyponymy) are edges. The "ISA" (is-a) relation allows for the traversal from highly specific concepts (e.g., "hatchback") up to abstract root nodes (e.g., "entity").
* **Goal:** Trace the lineage of a specific concept back to the root of the taxonomy.
* **Key Learning:** Seeing how a structured knowledge map allows algorithms to compute paths between concepts, reinforcing the logical "ISA" hierarchy.
* **Run:** `python ex2.py`

<a name="exercise-3"></a>
## Exercise 3: Quantifying Proximity with Wu-Palmer Similarity (WUP)
**Concept:** The structure of WordNet enables mathematical quantification of semantic proximity using the Wu-Palmer Similarity (WUP) metric. WUP calculates similarity based on the depth of the Least Common Subsumer (LCS)—the first shared ancestor node in the tree—between two concepts.
* **Goal:** Compare pairs like "car/truck" and "apple/orange" to observe how shared ancestry drives similarity scores.
* **Key Learning:** Understanding how the depth of the LCS in a human-annotated hierarchy provides a logical, explainable measure of similarity, contrasting with the "noisy" nature of vector-based statistics.
* **Run:** `python ex3.py`

---

## Requirements
* **Python 3.x**
* **Dependencies:**
  ```bash
  pip install nltk
