from transformers import pipeline

# Load BERT's Masked Language Modeling pipeline
# (This will download a small model to your machine the first time you run it)
print("Loading BERT Masked Language Model...")
unmasker = pipeline('fill-mask', model='bert-base-uncased')

# Test Case 1: The "River" context
sentence_a = "I sat by the [MASK] of the river to go fishing."
print(f"\nInput A: {sentence_a}")
results_a = unmasker(sentence_a)
for res in results_a[:3]:
    print(f"Guess: {res['token_str']:<10} | Confidence: {res['score']:.4f}")

# Test Case 2: The "Financial" context
sentence_b = "I went to the [MASK] to deposit my money into my account."
print(f"\nInput B: {sentence_b}")
results_b = unmasker(sentence_b)
for res in results_b[:3]:
    print(f"Guess: {res['token_str']:<10} | Confidence: {res['score']:.4f}")

# Question for the student:
# In the slides, we discussed the "Polysemy Problem" (e.g., river bank vs. financial bank). 
# How does BERT's bidirectional reading specifically solve the polysemy problem 
# that static models like Word2Vec failed at?
