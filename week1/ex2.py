import spacy

nlp = spacy.load("en_core_web_sm")
text = "The central bank is expected to announce a major policy change regarding interest rates on Monday."


# List comprehension to filter out stop words and punctuation, keeping only lemmas

