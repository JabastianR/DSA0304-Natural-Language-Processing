import re
import math
from collections import Counter


# -----------------------------
# Training Corpus
# -----------------------------
train_text = """
the student is studying artificial intelligence
the student is learning natural language processing
the teacher is teaching artificial intelligence
the student reads a book
the teacher reads a book
machine learning is useful
natural language processing is useful
"""


# -----------------------------
# Test Corpus
# -----------------------------
test_text = """
the student is learning
the teacher is reading
machine learning is useful
"""


def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())


train = tokenize(train_text)
test = tokenize(test_text)

train = ["<s>"] + train + ["</s>"]

# Counts
unigram = Counter(train)

bigram = Counter(
    (train[i], train[i+1])
    for i in range(len(train)-1)
)

trigram = Counter(
    (train[i], train[i+1], train[i+2])
    for i in range(len(train)-2)
)


# -----------------------------
# Probability Functions
# -----------------------------
def unigram_probability(word):
    return unigram[word] / len(train)


def bigram_probability(w1, w2):
    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def trigram_probability(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


# -----------------------------
# Entropy Calculation
# -----------------------------
def calculate_entropy(model):

    log_probability_sum = 0
    count = 0

    test_tokens = ["<s>"] + test + ["</s>"]

    for i in range(1, len(test_tokens)):

        word = test_tokens[i]

        if model == 1:
            probability = unigram_probability(word)

        elif model == 2:
            probability = bigram_probability(
                test_tokens[i-1],
                word
            )

        elif model == 3:

            if i < 2:
                continue

            probability = trigram_probability(
                test_tokens[i-2],
                test_tokens[i-1],
                word
            )

        # Avoid log(0)
        if probability > 0:
            log_probability_sum += math.log2(probability)
            count += 1

    if count == 0:
        return float("inf")

    return -log_probability_sum / count


# -----------------------------
# Calculate Entropy
# -----------------------------
print("ENTROPY RESULTS")

h1 = calculate_entropy(1)
h2 = calculate_entropy(2)
h3 = calculate_entropy(3)

print("Unigram Entropy :", round(h1, 4))
print("Bigram Entropy  :", round(h2, 4))
print("Trigram Entropy :", round(h3, 4))


# -----------------------------
# Prediction Scenario
# -----------------------------
def predictability(sentence):

    words = tokenize(sentence)

    if len(words) < 2:
        return

    w1 = words[-2]
    w2 = words[-1]

    probabilities = []

    for word in unigram:

        p = trigram_probability(w1, w2, word)

        if p > 0:
            probabilities.append((word, p))

    probabilities.sort(key=lambda x: x[1], reverse=True)

    print("\nNext Word Predictions:")

    for word, p in probabilities[:5]:
        print(word, "Probability:", round(p, 4))


sentence = input("\nEnter a sentence: ")

predictability(sentence)
