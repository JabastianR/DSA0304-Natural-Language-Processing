words = ["activate", "activation", "reactivation"]

for word in words:

    if word == "activate":
        prefix = "-"
        root = "activate"
        suffix = "-"
        process = "Base form"

    elif word == "activation":
        prefix = "-"
        root = "activate"
        suffix = "-ion"
        process = "Verb to Noun"

    elif word == "reactivation":
        prefix = "re-"
        root = "activate"
        suffix = "-ion"
        process = "Prefix + Noun formation"

    print("Original Word :", word)
    print("Prefix        :", prefix)
    print("Root Word     :", root)
    print("Suffix        :", suffix)
    print("Transformation:", process)
    print("Normalized    :", root)
    print("-----------------------------")
