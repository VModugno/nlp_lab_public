import nltk
from collections import Counter
import matplotlib.pyplot as plt

# You may need to run nltk.download('gutenberg') and nltk.download('punkt')
# We will use Shakespeare's Hamlet as our corpus
nltk.download('gutenberg', quiet=True)
nltk.download('punkt_tab', quiet=True)
words = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')

# Lowercase and filter out pure punctuation for a cleaner count
words = [w.lower() for w in words if w.isalpha()]

# Count frequencies
word_counts = Counter(words)
top_20_words = word_counts.most_common(20)

print("Top 20 Most Frequent Words:")
for rank, (word, count) in enumerate(top_20_words):
    print(f"{rank + 1}. {word}: {count}")

# Question for the student:
# How many of the top 10 words actually tell you what the play 'Hamlet' is about? 
# How does TF-IDF mathematically solve this exact problem?
