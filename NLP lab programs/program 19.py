import nltk
from nltk.wsd import lesk

nltk.download('wordnet')
nltk.download('omw-1.4')

sentence = "I went to the bank to deposit money".split()

sense = lesk(sentence, "bank")

print("Word Sense:", sense)
print("Meaning:", sense.definition())