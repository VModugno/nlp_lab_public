from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# The two sentences with vastly different meanings
sentence_1 = "Man bites dog"
sentence_2 = "Dog bites man"

# Initialize the vectorizer
vectorizer = CountVectorizer()

# Fit the vectorizer and transform the sentences
X = vectorizer.fit_transform([sentence_1, sentence_2]).toarray()
features = vectorizer.get_feature_names_out()

print(f"Vocabulary Dimensions: {features}\n")

print(f"Vector 1 ('{sentence_1}'): {X[0]}")
print(f"Vector 2 ('{sentence_2}'): {X[1]}\n")

# Mathematical comparison
if np.array_equal(X[0], X[1]):
    print("FALLACY CONFIRMED: The machine sees these two sentences as 100% mathematically identical!")
else:
    print("The vectors are different.")

# Question for the student:
# If you were building a sentiment analysis tool to determine if a customer review is about 
# a "good product but bad shipping" versus "bad product but good shipping", 
# why would BoW completely fail?
