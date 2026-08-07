words = ["create", "creates", "creating"]

for word in words:

    if word == "create":
        root = "create"
        suffix = "-"
        category = "Base Form"

    elif word == "creates":
        root = "create"
        suffix = "-s"
        category = "Third-Person Singular"

    elif word == "creating":
        root = "create"
        suffix = "-ing"
        category = "Present Participle"

    print("Original Word :", word)
    print("Root Word     :", root)
    print("Suffix        :", suffix)
    print("Category      :", category)
    print("Normalized    :", root)
    print("-----------------------------")
