text = input("Enter text: ")

sentences = text.split(".")

if len(sentences) > 1:
    print("The text has multiple sentences.")
    print("Coherence: Good")
else:
    print("Coherence: Poor")