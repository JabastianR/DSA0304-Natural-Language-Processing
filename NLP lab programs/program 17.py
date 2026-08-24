import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

word = "bank"

synsets = wordnet.synsets(word)

for s in synsets:
    print("Synset:", s.name())
    print("Meaning:", s.definition())
    print()