import re

# A list of simulated user utterances
utterances = [
    "I would like to buy a product.",
    "Where can I purchase this item?",
    "I am just browsing the website.",
    "Can I buy an item using my credit card?",
    "What is the return policy for a purchase?"
]

def detect_purchase_intent(text):
    # TODO: Write a RegEx pattern that matches variations of buying or purchasing an item/product.
    # Hint: Look at Slide 15 for the exact pattern logic!
    pattern = r"(buy|purchase)\s+(?:an?\s+)?(item|product)" 
    
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return f"Intent Detected: {match.group(0)}"
    return "No Intent Detected"

# Test the function
for sentence in utterances:
    print(f"User: '{sentence}' \nSystem: {detect_purchase_intent(sentence)}\n")
