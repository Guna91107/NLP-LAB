sentence = ["I", "like", "to", "play", "running"]

tags = [(word, "NN") for word in sentence]

for i in range(len(tags)):
    word, tag = tags[i]

    if word.endswith("ing"):
        tags[i] = (word, "VBG")

    elif i > 0 and sentence[i-1] == "to":
        tags[i] = (word, "VB")

print(tags)