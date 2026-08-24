import spacy

nlp = spacy.load("en_core_web_sm")

text = "The smart student completed the project."

doc = nlp(text)

print("Noun Phrases:")
for chunk in doc.noun_chunks:
    print(chunk.text)