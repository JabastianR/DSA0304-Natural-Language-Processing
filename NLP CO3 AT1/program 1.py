import re
from collections import Counter, defaultdict

# -----------------------------
# Training Corpus
# -----------------------------
corpus = """
the student is studying artificial intelligence
the student is learning natural language processing
the student is reading a book
the teacher is teaching artificial intelligence
the teacher is reading a book
the student likes machine learning
the student likes natural language processing
machine learning is a part of artificial intelligence
natural language processing is a part of artificial intelligence
the book is interesting
"""

# -----------------------------
# Preprocessing
# -----------------------------
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

words = tokenize(corpus)

# Add sentence boundaries
tokens = ["<s>"] + words + ["</s>"]

# -----------------------------
# N-gram Counts
# -----------------------------
unigram = Counter(tokens)

bigram = Counter(
    (tokens[i], tokens[i+1])
    for i in range(len(tokens)-1)
)

trigram = Counter(
    (tokens[i], tokens[i+1], tokens[i+2])
    for i in range(len(tokens)-2)
)

# -----------------------------
# Probability Functions
# -----------------------------
def unigram_probability(word):
    return unigram[word] / sum(unigram.values())


def bigram_probability(w1, w2):
    if unigram[w1] == 0:
        return 0
    return bigram[(w1, w2)] / unigram[w1]


def trigram_probability(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0
    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


# -----------------------------
# Display Counts
# -----------------------------
print("UNIGRAM COUNTS")
for word, count in unigram.items():
    print(word, ":", count)

print("\nBIGRAM COUNTS")
for pair, count in bigram.items():
    print(pair, ":", count)

print("\nTRIGRAM COUNTS")
for tri, count in trigram.items():
    print(tri, ":", count)


# -----------------------------
# Prediction
# -----------------------------
def predict_next(sentence, n):
    input_words = tokenize(sentence)

    if n == 1:
        candidates = unigram.keys()

        results = [
            (word, unigram_probability(word))
            for word in candidates
        ]

    elif n == 2:
        previous = input_words[-1]

        results = [
            (word, bigram_probability(previous, word))
            for word in unigram.keys()
            if bigram[(previous, word)] > 0
        ]

    elif n == 3:
        if len(input_words) < 2:
            print("Trigram prediction needs at least 2 words.")
            return

        w1 = input_words[-2]
        w2 = input_words[-1]

        results = [
            (word, trigram_probability(w1, w2, word))
            for word in unigram.keys()
            if trigram[(w1, w2, word)] > 0
        ]

    else:
        print("N must be 1, 2 or 3.")
        return

    results.sort(key=lambda x: x[1], reverse=True)

    print("\nTop 5 predictions:")
    for word, probability in results[:5]:
        print(word, "->", round(probability, 4))


# -----------------------------
# User Interface
# -----------------------------
print("\nN-GRAM LANGUAGE MODEL")

n = int(input("Select N (1, 2, or 3): "))
sentence = input("Enter incomplete sentence: ")

predict_next(sentence, n)


# -----------------------------
# Demonstrate unseen N-gram
# -----------------------------
print("\nUNSEEN N-GRAM EXAMPLE")

print(
    "P(student | the) =",
    bigram_probability("the", "student")
)

print(
    "P(computer | the student) =",
    trigram_probability("the", "student", "computer")
)
