from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'John' [0.5] | 'Mary' [0.5]
VP -> 'runs' [0.6] | 'walks' [0.4]
""")

parser = ViterbiParser(grammar)

sentence = "John runs".split()

for tree in parser.parse(sentence):
    print(tree)