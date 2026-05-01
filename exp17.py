from nltk.corpus import wordnet

word = input("Enter word: ")

synsets = wordnet.synsets(word)

for s in synsets:
    print("Synset:", s.name())
    print("Meaning:", s.definition())
    print("Example:", s.examples())
    print()