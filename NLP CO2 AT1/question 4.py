words = ["writes", "writing", "written"]
print("-" * 90)
print("{:<12} {:<20} {:<10} {:<15} {:<10}".format(
    "Word", "State Path", "Root", "Type", "Normalized"))
print("-" * 90)
for word in words:
    if word == "writes":
        path = "q0 -> q1 -> q2"
        root = "write"
        t = "Regular"
    elif word == "writing":
        path = "q0 -> q1 -> q3"
        root = "write"
        t = "Regular"
    elif word == "written":
        path = "q0 -> q4"
        root = "write"
        t = "Irregular"
    print("{:<12} {:<20} {:<10} {:<15} {:<10}".format(
        word, path, root, t, "write"))
