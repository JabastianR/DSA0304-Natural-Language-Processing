from nltk.stem import PorterStemmer
import sys
print(sys.version)
print(sys.executable)

ps = PorterStemmer()

words = ["playing", "running", "studies", "easily"]

for word in words:
    print(word, "->", ps.stem(word))
