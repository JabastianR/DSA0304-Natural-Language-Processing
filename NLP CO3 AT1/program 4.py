import re
from collections import Counter, defaultdict


# =====================================================
# TRAINING DATA
# =====================================================

training_sentences = [
    ("the student reads a book",
     ["DT", "NN", "VBZ", "DT", "NN"]),

    ("the teacher teaches students",
     ["DT", "NN", "VBZ", "NNS"]),

    ("the students are learning",
     ["DT", "NNS", "VBP", "VBG"]),

    ("she reads the book",
     ["PRP", "VBZ", "DT", "NN"]),

    ("he is a good teacher",
     ["PRP", "VBZ", "DT", "JJ", "NN"]),

    ("the boy runs quickly",
     ["DT", "NN", "VBZ", "RB"]),

    ("the student studies in college",
     ["DT", "NN", "VBZ", "IN", "NN"]),

    ("ram and sam play cricket",
     ["NNP", "CC", "NNP", "VBP", "NN"])
]


# =====================================================
# LEXICAL DICTIONARY
# =====================================================

lexicon = {
    "the": "DT",
    "a": "DT",
    "an": "DT",

    "i": "PRP",
    "he": "PRP",
    "she": "PRP",
    "we": "PRP",
    "they": "PRP",

    "is": "VBZ",
    "are": "VBP",
    "am": "VBP",

    "reads": "VBZ",
    "teaches": "VBZ",
    "runs": "VBZ",
    "studies": "VBZ",
    "plays": "VBZ",

    "read": "VB",
    "teach": "VB",
    "play": "VB",

    "student": "NN",
    "teacher": "NN",
    "book": "NN",
    "boy": "NN",
    "college": "NN",
    "cricket": "NN",

    "students": "NNS",

    "good": "JJ",
    "quickly": "RB",

    "in": "IN",
    "on": "IN",
    "at": "IN",

    "and": "CC",
    "but": "CC",

    "ram": "NNP",
    "sam": "NNP"
}


# =====================================================
# RULE-BASED POS TAGGER
# =====================================================

def rule_based_tagger(sentence):

    words = sentence.lower().split()

    tags = []

    for word in words:

        if word in lexicon:
            tag = lexicon[word]

        elif word.endswith("ly"):
            tag = "RB"

        elif word.endswith("ing"):
            tag = "VBG"

        elif word.endswith("ed"):
            tag = "VBD"

        elif word.endswith("s"):
            tag = "NNS"

        else:
            tag = "NN"

        tags.append((word, tag))

    return tags


# =====================================================
# STOCHASTIC MODEL
# =====================================================

word_tag_count = defaultdict(Counter)
tag_transition_count = defaultdict(Counter)

for sentence, tags in training_sentences:

    words = sentence.split()

    for i, word in enumerate(words):

        word_tag_count[word][tags[i]] += 1

        if i > 0:
            previous_tag = tags[i-1]
            tag_transition_count[previous_tag][tags[i]] += 1


def stochastic_tagger(sentence):

    words = sentence.lower().split()

    result = []

    previous_tag = None

    for word in words:

        if word in word_tag_count:

            possible_tags = word_tag_count[word]

            best_tag = None
            best_score = -1

            for tag in possible_tags:

                word_probability = (
                    word_tag_count[word][tag]
                    / sum(word_tag_count[word].values())
                )

                if previous_tag is not None:

                    transition_total = sum(
                        tag_transition_count[previous_tag].values()
                    )

                    if transition_total > 0:

                        transition_probability = (
                            tag_transition_count[previous_tag][tag]
                            / transition_total
                        )

                    else:
                        transition_probability = 0

                else:
                    transition_probability = 1

                score = (
                    word_probability
                    * transition_probability
                )

                if score > best_score:
                    best_score = score
                    best_tag = tag

            tag = best_tag

        else:

            # Unknown word
            if word.endswith("ing"):
                tag = "VBG"
            elif word.endswith("ly"):
                tag = "RB"
            elif word.endswith("s"):
                tag = "NNS"
            else:
                tag = "NN"

        result.append((word, tag))
        previous_tag = tag

    return result


# =====================================================
# TRANSFORMATION-BASED TAGGING
# =====================================================

def transformation_based_tagger(sentence):

    # Start with rule-based tags
    tagged = rule_based_tagger(sentence)

    for i in range(len(tagged)):

        word, tag = tagged[i]

        # Transformation 1:
        # Pronoun + noun -> verb
        if i > 0:

            previous_word, previous_tag = tagged[i-1]

            if previous_tag == "PRP" and tag == "NN":
                tagged[i] = (word, "VB")

        # Transformation 2:
        # Auxiliary + noun -> verb
        if i > 0:

            previous_word, previous_tag = tagged[i-1]

            if previous_tag in ["VBZ", "VBP"] and tag == "NN":
                tagged[i] = (word, "VB")

        # Transformation 3:
        # adjective + noun
        if i > 0:

            previous_word, previous_tag = tagged[i-1]

            if previous_tag == "JJ" and tag == "NN":
                tagged[i] = (word, "NN")

    return tagged


# =====================================================
# COMPARISON
# =====================================================

sentence = input("Enter an English sentence: ")

print("\nRULE-BASED TAGGER")
print(rule_based_tagger(sentence))

print("\nSTOCHASTIC TAGGER")
print(stochastic_tagger(sentence))

print("\nTRANSFORMATION-BASED TAGGER")
print(transformation_based_tagger(sentence))
