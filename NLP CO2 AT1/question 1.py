words = ["connected", "connecting", "connection"]
print("-" * 70)
print("{:<15} {:<12} {:<10} {:<15} {:<15}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))
print("-" * 70)
for word in words:
    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        t = "Inflectional"
    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        t = "Inflectional"
    elif word.endswith("ion"):
        root = "connect"
        suffix = "ion"
        t = "Derivational"
    print("{:<15} {:<12} {:<10} {:<15} {:<15}".format(
        word, root, suffix, t, "connect"))
