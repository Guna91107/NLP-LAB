import nltk
from nltk.stem import PorterStemmer

words = ["running", "jumps", "easily", "studies", "playing"]

ps = PorterStemmer()

for word in words:
    print(word, "->", ps.stem(word))P