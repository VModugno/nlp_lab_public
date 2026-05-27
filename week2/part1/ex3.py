import nltk
from nltk.corpus import wordnet as wn

# Download the required WordNet data (uncomment if running for the first time)
# nltk.download('wordnet')

# 1. Look up synsets (cognitive synonym sets) for both words
car_synsets = wn.synsets('car')
automobile_synsets = wn.synsets('automobile')

print(f"Synsets for 'car': {car_synsets}")
print(f"Synsets for 'automobile': {automobile_synsets}")

# 2. Isolate the primary meaning (the first synset) for both
primary_car = car_synsets[0]
primary_auto = automobile_synsets[0]

# 3. Check if they share the exact same conceptual meaning in WordNet
print("\n--- Semantic Check ---")
if primary_car == primary_auto:
    print("Success: WordNet knows that a 'car' and an 'automobile' are the exact same concept!")
else:
    print("WordNet sees these as different concepts.")

# 4. Explore the Graph (Hypernyms)
# Let's see what broader category (hypernym) a car belongs to in the graph
print(f"\nA {primary_car.name().split('.')[0]} is structurally a type of:")
for hypernym in primary_car.hypernyms():
    print(f"- {hypernym.name().split('.')[0]}")
