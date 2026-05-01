from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

sentence = input("Enter sentence: ")
word = input("Enter ambiguous word: ")

tokens = word_tokenize(sentence)
sense = lesk(tokens, word)

print("Sense:", sense)
print("Meaning:", sense.definition())