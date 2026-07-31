words = ["played", "player", "playing"]
print("-" * 75)
print("{:<12} {:<10} {:<15} {:<15} {:<10}".format(
    "Word", "Stem", "Removed Affix", "Type", "Normalized"))
print("-" * 75)
for word in words:
    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        t = "Inflectional"
    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        t = "Inflectional"
    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        t = "Derivational"
    print("{:<12} {:<10} {:<15} {:<15} {:<10}".format(
        word, stem, affix, t, "play"))
