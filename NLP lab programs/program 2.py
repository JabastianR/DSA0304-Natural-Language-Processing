def fsa(string):
    if string.endswith("er"):
        return "Accepted"
    else:
        return "Rejected"

word = input("Enter a string: ")
print(fsa(word))
