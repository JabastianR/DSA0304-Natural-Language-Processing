from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'Ram'
VP -> V NP
V -> 'likes'
NP -> 'apple'
""")

parser = ChartParser(grammar)

sentence = "Ram likes apple".split()

for tree in parser.parse(sentence):
    tree.pretty_print()