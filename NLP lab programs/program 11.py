import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John'
VP -> 'runs'
""")

parser = RecursiveDescentParser(grammar)

sentence = "John runs".split()

for tree in parser.parse(sentence):
    print(tree)