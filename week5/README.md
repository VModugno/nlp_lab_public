# Transformer Building Blocks: Practical Lab

Welcome to the Transformer Building Blocks lab! In this session, you will build the core components of a Transformer model from scratch using PyTorch. 

This lab is divided into four distinct exercises. In the provided Python file, you will find skeleton code with several `TODO` comments. Your objective is to complete these sections to make the architecture functional.

## Prerequisites
* Python 3.7+
* PyTorch (`torch`)

## Exercise 1: Scaled Dot-Product Self-Attention
**Objective:** Implement the core attention mechanism that allows the model to weigh the importance of different words in a sequence.

**What you need to do:**
1. **Compute Dot Product:** Calculate the raw attention scores by taking the matrix multiplication of the queries ($Q$) and the transposed keys ($K^{\top}$).
2. **Scale the Scores:** Divide the raw scores by the square root of the key dimension ($d_k$) to prevent vanishing gradients during the softmax step.
3. **Apply Softmax:** Convert the scaled scores into a probability distribution (attention weights) along the last dimension.
4. **Compute Output:** Multiply the resulting attention weights by the values matrix ($V$) to get the final contextualized output.

## Exercise 2: Implementing Causal Masking
**Objective:** Create a mask for autoregressive decoders to prevent the model from "cheating" by looking at future tokens during text generation.

**What you need to do:**
1. **Generate a Triangular Matrix:** Use PyTorch's built-in triangular matrix function to generate a 2D tensor where the lower triangle contains `1`s (allowed positions) and the upper triangle contains `0`s (masked future positions).

## Exercise 3: Sinusoidal Positional Encoding
**Objective:** Inject mathematical signatures into the word embeddings so the order-agnostic attention mechanism can understand sequence order.

**What you need to do:**
1. **Calculate the Divisor:** Compute the scaling denominator using the formula $e^{2i \times (-\ln(10000) / d_{model})}$. Note that this is calculated in log space for numerical stability.
2. **Apply Sine:** Assign the sine of the `position * div_term` to all even indices of the positional encoding matrix.
3. **Apply Cosine:** Assign the cosine of the `position * div_term` to all odd indices of the positional encoding matrix.
4. **Add to Embeddings:** In the forward pass, add the appropriately sliced positional encoding matrix directly to the incoming input embeddings.

## Exercise 4: Building a Pre-LN Transformer Block
**Objective:** Assemble the multi-head attention and feed-forward networks into a complete, modern "Pre-LN" (Pre-Layer Normalization) Transformer block.

**What you need to do:**
1. **First Normalization:** Apply the first Layer Normalization module to the inputs *before* passing them into the multi-head attention mechanism.
2. **First Residual Connection:** Add the original, un-normalized input back to the output of the attention mechanism (along with dropout).
3. **Second Normalization & FFN:** Apply the second Layer Normalization module to the new hidden state, then pass it through the Feed-Forward Network.
4. **Second Residual Connection:** Add the state from step 2 back to the output of the Feed-Forward network to complete the block.

---
*Run the test blocks provided at the bottom of each exercise in your script to verify your tensor shapes and outputs!*
