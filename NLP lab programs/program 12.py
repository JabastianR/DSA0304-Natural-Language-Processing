from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John'
VP -> 'runs'
""")

parser = EarleyChartParser(grammar)

sentence = "John runs".split()

for tree in parser.parse(sentence):
    print(tree)