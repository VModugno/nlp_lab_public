import numpy as np
from numpy.linalg import norm

def cosine_similarity(u, v):
    if norm(u) == 0 or norm(v) == 0: return 0.0
    return np.dot(u, v) / (norm(u) * norm(v))

print("--- 1. Sparse Representations (Bag-of-Words) ---")
# In BoW, every word gets its own isolated dimension.
sparse_coffee = np.array([1, 0, 0, 0, 0])
sparse_tea =    np.array([0, 1, 0, 0, 0])

sparse_sim = cosine_similarity(sparse_coffee, sparse_tea)
print(f"Similarity between Sparse 'coffee' and 'tea': {sparse_sim:.2f}")
print("Result: The Orthogonality Trap. The machine thinks they share 0 meaning.\n")

print("--- 2. Dense Representations (Word2Vec Style) ---")
# In Dense models, concepts are compressed into real-valued dimensions (e.g., [Heat, Caffeine, Liquid])
dense_coffee = np.array([0.8, 0.9, 0.95])
dense_tea =    np.array([0.7, 0.6, 0.90])
dense_car =    np.array([0.1, 0.0, 0.05])

dense_sim_drink = cosine_similarity(dense_coffee, dense_tea)
dense_sim_car = cosine_similarity(dense_coffee, dense_car)

print(f"Similarity between Dense 'coffee' and 'tea': {dense_sim_drink:.2f}")
print(f"Similarity between Dense 'coffee' and 'car': {dense_sim_car:.2f}")

# Question for the student:
# How do dense representations successfully solve the information bottleneck that 
# restricted early NLP systems?
