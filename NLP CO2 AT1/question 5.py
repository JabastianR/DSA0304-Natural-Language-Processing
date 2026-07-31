from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["relational", "relation", "relate"]
print("-" * 80)
print("{:<15} {:<25} {:<20} {:<15}".format(
    "Word", "Rule Applied", "Intermediate", "Final Stem"))
print("-" * 80)
for word in words:
    if word == "relational":
        rule = 'Removed "ional"'
        intermediate = "relate"
    elif word == "relation":
        rule = 'Removed "ion"'
        intermediate = "relate"
    elif word == "relate":
        rule = 'Removed "e"'
        intermediate = "relat"
    stem = ps.stem(word)
    print("{:<15} {:<25} {:<20} {:<15}".format(
        word, rule, intermediate, stem))
