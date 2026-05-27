import numpy as np

# 1. Define our Vocabulary V
vocabulary = ["car", "automobile", "dog", "tree"]
V_size = len(vocabulary)
print(f"Vocabulary Size |V| = {V_size}")

# 2. Create one-hot vectors (x = [0, ..., 1, ... 0])
# TODO: Create a one-hot vector for 'car' (index 0) and 'automobile' (index 1)
vector_car = np.array([1, 0, 0, 0])
vector_automobile = np.array([0, 1, 0, 0])

# 3. The Orthogonality Problem
# TODO: Calculate the dot product of the two vectors using np.dot()
dot_product = np.dot(vector_car, vector_automobile)

print(f"Vector for 'car':        {vector_car}")
print(f"Vector for 'automobile': {vector_automobile}")
print(f"Dot Product (Similarity): {dot_product}")

# Question for the student: 
# Even though "car" and "automobile" mean the same thing, what does the math say?
