import nltk
from nltk.corpus import wordnet as wn

# Run this once to download the WordNet database
# nltk.download('wordnet')

target_word = "bank"

# 1. Retrieve all synsets for the target word
# TODO: Use wn.synsets() to get the list of synsets for 'bank'
bank_synsets = wn.synsets(target_word)

print(f"Total distinct synsets found for '{target_word}': {len(bank_synsets)}\n")

# 2. Iterate through the synsets and print their glosses (definitions)
for i, synset in enumerate(bank_synsets):
    # TODO: Get the name of the synset and its definition using .name() and .definition()
    name = synset.name()
    gloss = synset.definition()
    
    print(f"Sense {i + 1}: {name}")
    print(f"Gloss: {gloss}\n")

# Question for the student:
# Based on the output, which Sense represents the financial institution, 
# and which Sense represents the side of a river?
