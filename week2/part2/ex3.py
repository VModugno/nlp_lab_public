import numpy as np
from numpy.linalg import norm

# Simulated 4-dimensional dense vectors [Royalty, Masculinity, Femininity, Age]
dense_vectors = {
    "king":  np.array([0.95, 0.90, 0.05, 0.60]),
    "man":   np.array([0.05, 0.95, 0.02, 0.55]),
    "woman": np.array([0.02, 0.05, 0.95, 0.50]),
    "queen": np.array([0.92, 0.03, 0.98, 0.55]),
    "apple": np.array([0.00, 0.00, 0.00, 0.00]) 
}

# 1. Perform the Vector Arithmetic
# TODO: Calculate: King - Man + Woman
result_vector = dense_vectors["king"] - dense_vectors["man"] + dense_vectors["woman"]

print(f"Resulting Arithmetic Vector: {result_vector}")

# 2. Check the similarity to "Queen"
def cosine_sim(u, v):
    if norm(u) == 0 or norm(v) == 0: return 0.0
    return np.dot(u, v) / (norm(u) * norm(v))

sim_to_queen = cosine_sim(result_vector, dense_vectors["queen"])
sim_to_apple = cosine_sim(result_vector, dense_vectors["apple"])

print(f"Similarity to Queen: {sim_to_queen:.4f}")
print(f"Similarity to Apple: {sim_to_apple:.4f}")
