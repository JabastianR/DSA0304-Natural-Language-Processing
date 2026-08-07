words = ["analyzing", "analysis", "analytical"]

for word in words:

    if word == "analyzing":
        root = "analyze"
        affix = "-ing"
        word_type = "Inflectional"

    elif word == "analysis":
        root = "analyze"
        affix = "-sis"
        word_type = "Derivational"

    elif word == "analytical":
        root = "analyze"
        affix = "-ical"
        word_type = "Derivational"

    print("Original Word :", word)
    print("Root Word     :", root)
    print("Affix         :", affix)
    print("Type          :", word_type)
    print("Normalized    :", root)
    print("-----------------------------")
