import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter sentence: ")
doc = nlp(text)

for np in doc.noun_chunks:
    print("Noun Phrase:", np.text)
    print("Meaning: Refers to ->", np.root.text)
    print()