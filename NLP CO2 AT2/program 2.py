words = ["disagree", "agreement", "agreeable"]

for word in words:

    if word == "disagree":
        prefix = "dis-"
        root = "agree"
        suffix = "-"
        word_type = "Derivational"
        meaning = "Opposite of agree"

    elif word == "agreement":
        prefix = "-"
        root = "agree"
        suffix = "-ment"
        word_type = "Derivational"
        meaning = "State of agreeing"

    elif word == "agreeable":
        prefix = "-"
        root = "agree"
        suffix = "-able"
        word_type = "Derivational"
        meaning = "Willing or suitable"

    print("Original Word :", word)
    print("Prefix        :", prefix)
    print("Root Word     :", root)
    print("Suffix        :", suffix)
    print("Type          :", word_type)
    print("Meaning       :", meaning)
    print("Normalized    :", root)
    print("-----------------------------")
