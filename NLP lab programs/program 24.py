sentence = input("Enter a sentence: ")

if sentence.endswith("?"):
    print("Dialog Act: Question")
elif sentence.endswith("!"):
    print("Dialog Act: Exclamation")
else:
    print("Dialog Act: Statement")