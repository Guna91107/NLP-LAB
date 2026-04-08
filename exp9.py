import re

sentence = "Ram is running quickly"
words = sentence.split()

for word in words:
    if re.match(r'.*ing$', word):
        print(word, "-> VBG")
    elif re.match(r'.*ly$', word):
        print(word, "-> RB")
    elif word[0].isupper():
        print(word, "-> NNP")
    else:
        print(word, "-> NN")