from collections import defaultdict

corpus = "the students opened their books . the students opened their laptops . the students opened their exams"
tokens = corpus.split()

# Dictionaries to store counts
bigram_counts = defaultdict(int)
unigram_counts = defaultdict(int)

# 1. TODO: Iterate through the tokens and populate the bigram and unigram counts
for i in range(len(tokens) - 1):
    w1, w2 = tokens[i], tokens[i+1]
    # Your code here: update counts
    pass

def get_bigram_probability(word1, word2):
    """
    2. TODO: Calculate P(word2 | word1) = count(word1, word2) / count(word1)
    Return 0.0 if the word1 has never been seen.
    """
    # Your code here
    return 0.0

# Test the implementation
print("P(books | their) =", get_bigram_probability("their", "books")) 
print("P(laptops | their) =", get_bigram_probability("their", "laptops"))
