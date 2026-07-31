words = ["unhappy", "happiness", "happily"]
print("-" * 85)
print("{:<12} {:<10} {:<10} {:<10} {:<15} {:<10}".format(
    "Word", "Prefix", "Root", "Suffix", "Type", "Normalized"))
print("-" * 85)
for word in words:
    prefix = "-"
    suffix = "-"
    if word.startswith("un"):
        prefix = "un"
        root = "happy"
    elif word.endswith("ness"):
        suffix = "ness"
        root = "happy"
    elif word.endswith("ly"):
        suffix = "ly"
        root = "happy"
    print("{:<12} {:<10} {:<10} {:<10} {:<15} {:<10}".format(
        word, prefix, root, suffix, "Derivational", "happy"))
