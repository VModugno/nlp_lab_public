import numpy as np
from numpy.linalg import norm

# 1. Define the Co-occurrence Matrix (from the Slide 7 scenario)
# Context columns: [bite, buy, drive, eat, ride]
vectors = {
    "bike": np.array([0, 15, 0, 0, 85]),
    "car":  np.array([0, 42, 91, 0, 5]),
    "dog":  np.array([35, 2, 0, 12, 0]),
    "lion": np.array([12, 0, 0, 45, 0])
}

def cosine_similarity(u, v):
    # TODO: Implement the Cosine Similarity formula: (u dot v) / (||u|| * ||v||)
    # Hint: Use np.dot() and norm()
    if norm(u) == 0 or norm(v) == 0:
        return 0.0
    return np.dot(u, v) / (norm(u) * norm(v))

# 2. Test the comparisons
print("Cosine Similarity Results:")
print(f"Car vs. Bike: {cosine_similarity(vectors['car'], vectors['bike']):.4f}")
print(f"Car vs. Dog:  {cosine_similarity(vectors['car'], vectors['dog']):.4f}")
print(f"Car vs. Car:  {cosine_similarity(vectors['car'], vectors['car']):.4f}")
