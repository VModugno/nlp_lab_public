# Applied Natural Language Processing: Lab Exercises
**Session 3: Vector Semantics & Embeddings**

Welcome to the lab exercises for Session 3. In these tasks, you will explore both traditional dense static embeddings (Word2Vec) and modern multimodal embeddings (CLIP). 

These exercises are designed around a practical, real-world scenario: **Autonomous Systems and Environmental Monitoring**.

---

## 🛠 Prerequisites

Before starting, ensure you have the required libraries installed in your Python environment. You can install them using pip:

```bash
conda install -c conda-forge -c pytorch gensim nltk transformers pytorch torchvision pillow requests
```

## 💻 Exercise 1: Word2Vec – Semantic Math & Vector Context

Objective: Tokenize a specialized text corpus, train a Continuous Bag of Words (CBOW) or Skip-Gram model, and extract semantic meaning using vector arithmetic and similarity metrics.

Instructions: In this exercise, you will build a Word2Vec model from scratch using the gensim library. You will be provided with a small corpus of technical logs from an autonomous drone. Your task is to prepare the text, train the embedding space, and extract semantic relationships to see how the model groups technical concepts.

Challenge: Try adding 10-15 more sentences to your corpus related to drones and robotics. Run the model again and observe how the mathematical relationships and analogies improve with more data!



##🖼️ Exercise 2: CLIP – Zero-Shot Multimodal Alignment
Objective: Use a pre-trained CLIP model to perform zero-shot classification on an image without any prior fine-tuning, demonstrating the power of shared latent spaces.

Instructions: Traditional vision models require rigid integer labels. In this exercise, you will use CLIP's multimodal embeddings to classify an image from a river monitoring drone using only natural language. You will need to engineer context-rich prompts and compute the mathematical alignment between the visual and textual vectors.

Challenge: Experiment with your candidate labels. Try stripping away the context (e.g., just passing the word "water" instead of "a photo of water") to witness the "polysemy issues" and context dependency discussed in the lecture.
