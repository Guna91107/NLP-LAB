train_data = [
    ("I", "PRP"),
    ("love", "VBP"),
    ("NLP", "NNP"),
    ("love", "VBP"),
    ("Python", "NNP")
]

freq = {}

for word, tag in train_data:
    freq.setdefault(word, {})
    freq[word][tag] = freq[word].get(tag, 0) + 1

sentence = ["I", "love", "Python"]

result = []
for word in sentence:
    if word in freq:
        tag = max(freq[word], key=freq[word].get)
    else:
        tag = "NN"
    result.append((word, tag))

print(result)