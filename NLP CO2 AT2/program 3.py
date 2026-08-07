words = ["govern", "government", "governance"]

for word in words:

    if word == "govern":
        root = "govern"
        affix = "-"
        level = "Level 0"

    elif word == "government":
        root = "govern"
        affix = "-ment"
        level = "Level 1"

    elif word == "governance":
        root = "govern"
        affix = "-ance"
        level = "Level 1"

    print("Original Word :", word)
    print("Root Word     :", root)
    print("Affix         :", affix)
    print("Derivation    :", level)
    print("Normalized    :", root)
    print("-----------------------------")
