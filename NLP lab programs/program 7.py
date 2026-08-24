import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "Machine learning is interesting."

words = nltk.word_tokenize(text)

print(nltk.pos_tag(words))