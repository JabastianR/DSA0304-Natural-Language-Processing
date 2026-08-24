from nltk import bigrams

text = "machine learning is very useful".split()

bg = list(bigrams(text))

print("Bigrams:")
for b in bg:
    print(b)