import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'a' | 'the'
N -> 'cat' | 'dog'
V -> 'chased' | 'saw'
""")

parser = ChartParser(grammar)

sentence = input("Enter sentence: ").split()

try:
    for tree in parser.parse(sentence):
        print(tree)
        tree.pretty_print()
except:
    print("Invalid sentence")