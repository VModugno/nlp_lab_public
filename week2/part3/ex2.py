import nltk
from nltk.corpus import wordnet as wn

# Start with the specific synset for a hatchback car
current_synset = wn.synset('hatchback.n.01')
hierarchy_path = [current_synset.name().split('.')[0]]

print(f"Tracing lineage for: {current_synset.name()}...\n")

# Loop to climb the tree until we hit the root (which has no hypernyms)
while current_synset.hypernyms():
    # TODO: Get the first hypernym (parent) of the current synset
    parent = current_synset.hypernyms()[0]
    
    # Add the parent's name to our path list
    hierarchy_path.append(parent.name().split('.')[0])
    
    # Move up the tree for the next iteration
    current_synset = parent

# Print the path from Abstract to Concrete (reversing the list)
print("--- Concept Hierarchy (Top-Down) ---")
for level, concept in enumerate(reversed(hierarchy_path)):
    indent = "  " * level
    print(f"{indent}↳ {concept.capitalize()}")

# Question for the student:
# Did the script successfully hit 'motor_vehicle', 'artifact', and 'entity' 
# exactly as depicted in the slide diagram?
