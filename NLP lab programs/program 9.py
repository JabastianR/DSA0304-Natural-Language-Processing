import re

words = input("Enter words: ").split()

for word in words:
    if re.match(r".*ing$", word):
        print(word, "-> Verb")
    elif re.match(r".*ly$", word):
        print(word, "-> Adverb")
    else:
        print(word, "-> Noun")