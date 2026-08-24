sentence = input("Enter sentence: ").split()

for word in sentence:
    tag = "NN"

    if word.endswith("ing"):
        tag = "VBG"

    print(word, ":", tag)