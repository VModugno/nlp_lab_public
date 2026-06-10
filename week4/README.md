# NLP and Deep Learning Concepts: Lab Exercises

This repository contains a set of foundational Python exercises designed to help you build intuition around core Natural Language Processing (NLP) and Deep Learning concepts, ranging from traditional count-based statistical models to modern attention mechanisms.

---

## 📚 Exercises Overview

### Exercise 1: N-Gram Counting and Probability
* [cite_start]**Core Concept:** Traditional language modeling prior to deep learning relies heavily on the Markov Assumption, simplifying sequence probabilities by looking only at a fixed history of the previous $n-1$ words[cite: 124, 129]. 
* [cite_start]**Objective:** You will implement a basic Bigram ($n=2$) Language Model from scratch using standard Python dictionaries[cite: 133]. This exercise demonstrates how statistical models approximate probabilities by calculating:
  $$P(w_2 \mid w_1) = \frac{\text{count}(w_1, w_2)}{\text{count}(w_1)}$$
* [cite_start]**Key Takeaway:** Helps understand the root cause of the **sparsity problem**—if a specific word combination never appears in the training data, its statistical count is zero, causing the entire sequence probability to drop to zero[cite: 153, 155].

### Exercise 2: The RNN Forward Pass
* [cite_start]**Core Concept:** Recurrent Neural Networks (RNNs) solve the fixed-window constraint of previous architectures by introducing a horizontal sequential dependency known as a "memory state"[cite: 249, 298].
* [cite_start]**Objective:** Using `numpy`, you will write the mathematical engine behind a single timestep update of a Vanilla RNN cell[cite: 302]. You will implement the standard hidden state formula:
  $$h^{(t)} = \tanh(W_h h^{(t-1)} + W_e e^{(t)} + b_1)$$
* [cite_start]**Key Takeaway:** Illustrates how an RNN repeatedly applies the exact same weight matrices over time, allowing the hidden state to act as a lossy compression of the sequence history[cite: 301, 304].

### Exercise 3: Bidirectional RNNs
* [cite_start]**Core Concept:** Standard left-to-right RNNs are restricted because they lack access to "future context" when making a prediction at the current timestep[cite: 841, 848]. 
* [cite_start]**Objective:** You will write a sequence processing loop that simultaneously runs a Forward RNN (left-to-right) and a Backward RNN (right-to-left)[cite: 853, 869]. [cite_start]You will then structurally merge their outputs by concatenating the hidden states[cite: 858, 872].
* [cite_start]**Key Takeaway:** Explains why bidirectionality is incredibly powerful for sentence encoding tasks (like BERT), but mathematically illegal for standard auto-regressive Language Modeling where future words are exactly what the model is trying to predict[cite: 879, 883].

### Exercise 4: The Attention Mechanism
* [cite_start]**Core Concept:** Sequence-to-sequence architectures suffer from an "information bottleneck" because the encoder is forced to compress a raw sentence of any length into a single, fixed-size vector before passing it to the decoder[cite: 988, 1056].
* [cite_start]**Objective:** You will implement the mathematical equations behind Dot-Product Attention[cite: 1324]. This involves three specific steps:
  1. [cite_start]Calculating raw alignment scores via a dot product between a decoder query ($s_t$) and all encoder keys ($h_i$)[cite: 1123, 1328].
  2. [cite_start]Applying a Softmax function to transform those raw scores into an attention probability distribution ($\alpha^t$)[cite: 1329, 1333].
  3. [cite_start]Computing a weighted sum of the encoder values to generate a context vector ($a_t$)[cite: 1124, 1334].
* [cite_start]**Key Takeaway:** Demonstrates how Attention achieves a maximum interaction distance of $O(1)$, creating a mathematical shortcut that bypasses sequential dependencies and completely mitigates the vanishing gradient problem over long sequences[cite: 1339, 1345].

---

## 🛠️ Environment Setup & Dependencies

To ensure reproducibility, a clean virtual environment managed via Miniconda or Anaconda is highly recommended. These exercises are built using pure Python and standard scientific computing libraries to keep the focus entirely on algorithmic logic rather than framework abstractions.

### Prerequisites
* **Python Version:** `3.10` or higher
* **Core Package:** `numpy` (used for matrix multiplication, vector transpositions, and activation functions)

### Configuration Instructions

1. **Create the Conda Environment:**
   Open your terminal and run the following command to create a isolated environment named `nlp-labs` with Python 3.10 installed:
   ```bash
   conda create --name nlp-labs python=3.10 -y
   ```
2. **Activate the Environment:**

```
conda activate nlp-labs
```
3. **Install Dependencies:**
Install numpy from the official conda-forge repository:



```bash
conda install -c conda-forge numpy -y
```

4. **Verify Installation:**
You can quickly verify that your environment is properly configured by launching Python and importing the dependency:


```bash
python -c "import numpy as np; print('NumPy version:', np.__version__)"
```

Once the configuration steps are complete, you are ready to open the exercise files and begin implementing the missing code sections marked with # TODO. 
   
   
   
   
   
