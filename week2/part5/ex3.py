import numpy as np

# Let's imagine our CLIP model has mapped these images and texts into a 4-dimensional shared space.
# Feature dimensions might loosely represent: [Feline, Canine, Fluffy, Outdoor]

# 1. The Image Encoders output these dense vectors:
image_dog = np.array([0.1, 0.9, 0.8, 0.6])
image_cat = np.array([0.9, 0.1, 0.7, 0.2])

# 2. The Text Encoders output these dense vectors:
text_dog = np.array([0.0, 0.95, 0.9, 0.5])  # "A fluffy dog outside"
text_cat = np.array([0.95, 0.0, 0.8, 0.1])  # "A cat indoors"

# 3. Contrastive Learning Alignment (Dot Product)
# Let's see how the model scores the pairs!
def get_alignment_score(image_vec, text_vec):
    # A simple dot product represents the unnormalized similarity in this shared space
    return np.dot(image_vec, text_vec)

print("--- Cross-Modal Alignment Matrix ---")

# Compare Image 1 (Dog) against both texts
print(f"Image(Dog) + Text(Dog): {get_alignment_score(image_dog, text_dog):.2f}")
print(f"Image(Dog) + Text(Cat): {get_alignment_score(image_dog, text_cat):.2f}")

print("-" * 35)

# Compare Image 2 (Cat) against both texts
print(f"Image(Cat) + Text(Dog): {get_alignment_score(image_cat, text_dog):.2f}")
print(f"Image(Cat) + Text(Cat): {get_alignment_score(image_cat, text_cat):.2f}")

# Question for the student:
# Look at the alignment matrix. Notice how the matching pairs have much higher scores 
# than the mismatched pairs. How does forcing a vision encoder and a text encoder into 
# the "exact same mathematical coordinate space" enable modern models to talk about images?
