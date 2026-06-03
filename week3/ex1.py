import gensim
from gensim.models import Word2Vec
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# Sample technical corpus (Logs from a robotics system)
corpus = [
    "The autonomous drone navigates the extreme environment.",
    "Reinforcement learning is used for dynamic robotic control.",
    "Machine learning algorithms optimize the flight path.",
    "The robot sensor detects obstacles in the river.",
    "Autonomous navigation requires advanced control theory.",
    "The drone sensor monitors water pollution levels."
]

# TODO 1: Tokenize the corpus
# Iterate through the corpus, convert to lowercase, and split into individual word tokens.
tokenized_corpus = [
    # YOUR CODE HERE
]

# TODO 2: Initialize and train the Word2Vec model
# Create a Word2Vec model. Decide whether to use CBOW (sg=0) or Skip-Gram (sg=1).
# Set a small vector size (e.g., size=10) and window size (e.g., window=3) given our small corpus.
model = # YOUR CODE HERE

# TODO 3: Extract Semantic Similarity
# Use the trained model to find the top 2 words most mathematically similar to 'drone'.
similar_to_drone = # YOUR CODE HERE
print("Words most similar to 'drone':", similar_to_drone)

# TODO 4: Vector Arithmetic (The "King - Man + Woman" analogy)
# Calculate: 'learning' - 'reinforcement' + 'control' 
# Hint: Use the model.wv.most_similar(positive=[...], negative=[...]) method
analogy_result = # YOUR CODE HERE
print("Vector Arithmetic Result:", analogy_result)
