import nltk
from nltk.corpus import wordnet as wn

# Define the primary synsets for our test cases
car = wn.synset('car.n.01')
truck = wn.synset('truck.n.01')

apple = wn.synset('apple.n.01')
orange = wn.synset('orange.n.01')

def analyze_wup_similarity(synset1, synset2):
    print(f"\nComparing: [{synset1.name()}] vs [{synset2.name()}]")
    
    # 1. Find the Least Common Subsumer (Shared Parent)
    # TODO: Use lowest_common_hypernyms() to find the LCS
    lcs = synset1.lowest_common_hypernyms(synset2)[0]
    print(f"Least Common Subsumer (LCS): {lcs.name()}")
    
    # 2. Calculate the Wu-Palmer Similarity score
    # NLTK has this math built-in based on the exact formula from the slides!
    # TODO: Use the .wup_similarity() method
    wup_score = synset1.wup_similarity(synset2)
    
    print(f"Wu-Palmer Similarity Score: {wup_score:.2f}")

# Run the tests
analyze_wup_similarity(car, truck)
analyze_wup_similarity(apple, orange)

# Question for the student:
# Look closely at the LCS for Apple and Orange. Did the algorithm successfully 
# realize they are both an "edible_fruit"?
