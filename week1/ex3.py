import spacy

nlp = spacy.load("en_core_web_sm")
text = "JPMorgan Chase announced today that CEO Jamie Dimon will be visiting their new offices in Paris, France next month. The company plans to invest over €50 million in European markets by 2025."

# Iterate through the named entities recognized by the pipeline

