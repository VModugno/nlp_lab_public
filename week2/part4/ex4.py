from sklearn.feature_extraction.text import CountVectorizer

# 1. The Training Phase (The Closed World)
training_corpus = [
    "I do not know the answer.",
    "For your information, the meeting is tomorrow."
]

vectorizer = CountVectorizer()
vectorizer.fit(training_corpus) # The vocabulary is locked here!

print(f"Locked Vocabulary ({len(vectorizer.get_feature_names_out())} words):")
print(vectorizer.get_feature_names_out())

# 2. The Real World (Encountering OOV tokens)
modern_sentence = ["IDK the answer, FYI the meeting is tomorrow."]
print(f"\nProcessing new sentence: '{modern_sentence[0]}'")

# Transform the new sentence using the locked vocabulary
new_vector = vectorizer.transform(modern_sentence).toarray()

# Let's see what the machine actually "read"
reconstructed = vectorizer.inverse_transform(new_vector)
print(f"\nWhat the BoW model actually perceived: {' '.join(reconstructed[0])}")

# Question for the student:
# Which specific words were completely deleted from the modern sentence? 
# Why is this highly dangerous for an enterprise NLP system processing live Twitter/X data?
