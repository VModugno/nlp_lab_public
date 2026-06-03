# Run this pip install first if running in Colab:
# !pip install transformers torch pillow requests

from PIL import Image
import requests
from transformers import CLIPProcessor, CLIPModel
import torch
import torch.nn.functional as F

# Load the CLIP model and processor from Hugging Face
model_id = "openai/clip-vit-base-patch32"
model = CLIPModel.from_pretrained(model_id)
processor = CLIPProcessor.from_pretrained(model_id)

# Fetch a sample image (e.g., a drone shot of a polluted waterway)
url = "https://images.unsplash.com/photo-1621451537084-482c73073e0f"
image = Image.open(requests.get(url, stream=True).raw)
image.show()

# TODO 1: The Art of Prompt Engineering
# Define 3 to 4 candidate text labels. 
# Remember Slide 56: Single words perform poorly. Use template strategies 
# (e.g., "An aerial photo of a clean river", "A drone view of water pollution").
candidate_labels = [
    # YOUR CODE HERE
]

# TODO 2: Process the inputs
# Pass both the image and the candidate text labels through the processor.
# Ensure return_tensors is set to "pt" (PyTorch).
inputs = # YOUR CODE HERE

# TODO 3: Compute the Similarity Matrix
# Perform a forward pass through the model using your inputs.
with torch.no_grad():
    outputs = # YOUR CODE HERE
    
    # Extract the image-to-text similarity scores (logits_per_image)
    logits_per_image = outputs.logits_per_image 
    
    # Apply a softmax function to these logits to convert them into probabilities summing to 1.0
    probs = # YOUR CODE HERE

# Print out the predictions
print("\n--- Zero-Shot Classification Results ---")
for label, prob in zip(candidate_labels, probs[0]):
    print(f"{label}: {prob.item() * 100:.2f}% probability")
