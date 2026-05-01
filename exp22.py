import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter text: ")
doc = nlp(text)

last_noun = ""
resolved = []

for token in doc:
    if token.pos_ == "NOUN":
        last_noun = token.text
        resolved.append(token.text)
    elif token.pos_ == "PRON":
        resolved.append(last_noun)
    else:
        resolved.append(token.text)

print("Resolved Text:", " ".join(resolved))