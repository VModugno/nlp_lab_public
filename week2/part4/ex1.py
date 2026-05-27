import numpy as np

# A small corpus of documents
corpus = [
    "A bat and a rat",
    "The bat is good",
    "A good rat"
]

def build_bow_matrix(corpus):
    print("--- Step 1: Tokenization & Vocabulary ---")
    # 1. Extract unique tokens (Vocabulary V)
    vocabulary = set()
    tokenized_docs = []
    
    for doc in corpus:
        # Simple whitespace tokenizer and lowercase
        tokens = doc.lower().split()
        tokenized_docs.append(tokens)
        for token in tokens:
            vocabulary.add(token)
            
    # Sort vocabulary to ensure consistent indexing
    vocabulary = sorted(list(vocabulary))
    print(f"Vocabulary (|V|={len(vocabulary)}): {vocabulary}")
    
    print("\n--- Step 2: Creating the Matrix X ---")
    # 2. Initialize X as a zero matrix of size M x N
    M = len(corpus)
    N = len(vocabulary)
    X = np.zeros((M, N), dtype=int)
    
    # 3. Populate the matrix with Term Frequencies
    for i, tokens in enumerate(tokenized_docs):
        for token in tokens:
            j = vocabulary.index(token) # Find index of token in V
            X[i, j] += 1                # Increment count
            
    return X, vocabulary

# Run the algorithm
X_matrix, vocab = build_bow_matrix(corpus)

print("\nFinal Document-Term Matrix:")
for i, row in enumerate(X_matrix):
    print(f"Doc {i+1}: {row}")

# Question for the student: 
# Look at the matrix. How many zeros are there? As the vocabulary grows to 50,000 words, 
# what happens to the sparsity of this matrix?
