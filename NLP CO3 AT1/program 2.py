import re
from collections import Counter

# -----------------------------
# Corpus
# -----------------------------
corpus = """
the student is studying artificial intelligence
the student is learning natural language processing
the student is reading a book
the teacher is teaching artificial intelligence
the teacher is reading a book
the student likes machine learning
machine learning is useful
natural language processing is useful
the book is interesting
"""

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

words = tokenize(corpus)

tokens = ["<s>"] + words + ["</s>"]

# -----------------------------
# Counts
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

total_words = len(tokens)


# -----------------------------
# Unsmoothed probabilities
# -----------------------------
def P1(word):
    return unigram[word] / total_words


def P2(w1, w2):
    if unigram[w1] == 0:
        return 0
    return bigram[(w1, w2)] / unigram[w1]


def P3(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0
    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


# -----------------------------
# Backoff Model
# -----------------------------
def backoff_probability(w1, w2, w3):

    # Try trigram
    p = P3(w1, w2, w3)

    if p > 0:
        return p, "Trigram"

    # Try bigram
    p = P2(w2, w3)

    if p > 0:
        return p, "Bigram"

    # Try unigram
    p = P1(w3)

    return p, "Unigram"


# -----------------------------
# Deleted Interpolation
# -----------------------------
lambda1 = 0.2
lambda2 = 0.3
lambda3 = 0.5


def interpolation_probability(w1, w2, w3):

    return (
        lambda1 * P1(w3)
        + lambda2 * P2(w2, w3)
        + lambda3 * P3(w1, w2, w3)
    )


# -----------------------------
# Prediction
# -----------------------------
def predict(sentence, method):

    words = tokenize(sentence)

    if len(words) < 2:
        print("Enter at least two words.")
        return

    w1 = words[-2]
    w2 = words[-1]

    results = []

    for word in unigram:

        if method == "unsmoothed":
            probability = P3(w1, w2, word)

        elif method == "backoff":
            probability, source = backoff_probability(w1, w2, word)

        elif method == "interpolation":
            probability = interpolation_probability(w1, w2, word)

        results.append((word, probability))

    results.sort(key=lambda x: x[1], reverse=True)

    print("\nTop Predictions:")

    for word, probability in results[:5]:
        print(word, "->", round(probability, 5))


# -----------------------------
# Main Program
# -----------------------------
print("LANGUAGE PREDICTION SYSTEM")

sentence = input("Enter incomplete sentence: ")

print("\n1. Unsmoothed")
print("2. Backoff")
print("3. Deleted Interpolation")

choice = input("Choose method: ")

if choice == "1":
    predict(sentence, "unsmoothed")

elif choice == "2":
    predict(sentence, "backoff")

elif choice == "3":
    predict(sentence, "interpolation")

else:
    print("Invalid choice.")
