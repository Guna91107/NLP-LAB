import nltk

text = "NLP is very interesting"

words = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(words)

print(pos_tags)