text = "I love NLP"

words = text.split()

bigrams = []
for i in range(len(words) - 1):
    bigrams.append((words[i], words[i+1]))

print("Bigrams:", bigrams)

sentence = ""
for pair in bigrams:
    sentence += pair[0] + " "
sentence += bigrams[-1][1]

print("Generated text:", sentence)