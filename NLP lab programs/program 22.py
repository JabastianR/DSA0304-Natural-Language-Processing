text = "Ravi is a good student. He studies every day."

sentences = text.split(".")

name = "Ravi"

for sentence in sentences:
    if "He" in sentence:
        sentence = sentence.replace("He", name)
    print(sentence.strip())