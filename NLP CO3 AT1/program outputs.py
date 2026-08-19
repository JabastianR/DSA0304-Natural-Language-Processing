Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/cravi/OneDrive/Desktop/Jabastian college/NLP folder/NLP CO3 AT1/program 1.py
UNIGRAM COUNTS
<s> : 1
the : 8
student : 5
is : 8
studying : 1
artificial : 4
intelligence : 4
learning : 3
natural : 3
language : 3
processing : 3
reading : 2
a : 4
book : 3
teacher : 2
teaching : 1
likes : 2
machine : 2
part : 2
of : 2
interesting : 1
</s> : 1

BIGRAM COUNTS
('<s>', 'the') : 1
('the', 'student') : 5
('student', 'is') : 3
('is', 'studying') : 1
('studying', 'artificial') : 1
('artificial', 'intelligence') : 4
('intelligence', 'the') : 3
('is', 'learning') : 1
('learning', 'natural') : 1
('natural', 'language') : 3
('language', 'processing') : 3
('processing', 'the') : 1
('is', 'reading') : 2
('reading', 'a') : 2
('a', 'book') : 2
('book', 'the') : 2
('the', 'teacher') : 2
('teacher', 'is') : 2
('is', 'teaching') : 1
('teaching', 'artificial') : 1
('student', 'likes') : 2
('likes', 'machine') : 1
('machine', 'learning') : 2
('learning', 'the') : 1
('likes', 'natural') : 1
('processing', 'machine') : 1
('learning', 'is') : 1
('is', 'a') : 2
('a', 'part') : 2
('part', 'of') : 2
('of', 'artificial') : 2
('intelligence', 'natural') : 1
('processing', 'is') : 1
('the', 'book') : 1
('book', 'is') : 1
('is', 'interesting') : 1
('interesting', '</s>') : 1

TRIGRAM COUNTS
('<s>', 'the', 'student') : 1
('the', 'student', 'is') : 3
('student', 'is', 'studying') : 1
('is', 'studying', 'artificial') : 1
('studying', 'artificial', 'intelligence') : 1
('artificial', 'intelligence', 'the') : 3
('intelligence', 'the', 'student') : 1
('student', 'is', 'learning') : 1
('is', 'learning', 'natural') : 1
('learning', 'natural', 'language') : 1
('natural', 'language', 'processing') : 3
('language', 'processing', 'the') : 1
('processing', 'the', 'student') : 1
('student', 'is', 'reading') : 1
('is', 'reading', 'a') : 2
('reading', 'a', 'book') : 2
('a', 'book', 'the') : 2
('book', 'the', 'teacher') : 1
('the', 'teacher', 'is') : 2
('teacher', 'is', 'teaching') : 1
('is', 'teaching', 'artificial') : 1
('teaching', 'artificial', 'intelligence') : 1
('intelligence', 'the', 'teacher') : 1
('teacher', 'is', 'reading') : 1
('book', 'the', 'student') : 1
('the', 'student', 'likes') : 2
('student', 'likes', 'machine') : 1
('likes', 'machine', 'learning') : 1
('machine', 'learning', 'the') : 1
('learning', 'the', 'student') : 1
('student', 'likes', 'natural') : 1
('likes', 'natural', 'language') : 1
('language', 'processing', 'machine') : 1
('processing', 'machine', 'learning') : 1
('machine', 'learning', 'is') : 1
('learning', 'is', 'a') : 1
('is', 'a', 'part') : 2
('a', 'part', 'of') : 2
('part', 'of', 'artificial') : 2
('of', 'artificial', 'intelligence') : 2
('artificial', 'intelligence', 'natural') : 1
('intelligence', 'natural', 'language') : 1
('language', 'processing', 'is') : 1
('processing', 'is', 'a') : 1
('intelligence', 'the', 'book') : 1
('the', 'book', 'is') : 1
('book', 'is', 'interesting') : 1
('is', 'interesting', '</s>') : 1

N-GRAM LANGUAGE MODEL
Select N (1, 2, or 3): 1
Enter incomplete sentence: the student

Top 5 predictions:
the -> 0.1231
is -> 0.1231
student -> 0.0769
artificial -> 0.0615
intelligence -> 0.0615

UNSEEN N-GRAM EXAMPLE
P(student | the) = 0.625
P(computer | the student) = 0.0

================== RESTART: C:/Users/cravi/OneDrive/Desktop/Jabastian college/NLP folder/NLP CO3 AT1/program 2.py =================
LANGUAGE PREDICTION SYSTEM
Enter incomplete sentence: natural

1. Unsmoothed
2. Backoff
3. Deleted Interpolation
Choose method: 1
Enter at least two words.
language model
SyntaxError: invalid syntax

================== RESTART: C:/Users/cravi/OneDrive/Desktop/Jabastian college/NLP folder/NLP CO3 AT1/program 2.py =================
LANGUAGE PREDICTION SYSTEM
Enter incomplete sentence: the student

1. Unsmoothed
2. Backoff
3. Deleted Interpolation
Choose method: 2

Top Predictions:
is -> 0.75
likes -> 0.25
the -> 0.13725
student -> 0.07843
learning -> 0.05882

================== RESTART: C:/Users/cravi/OneDrive/Desktop/Jabastian college/NLP folder/NLP CO3 AT1/program 3.py =================
ENTROPY RESULTS
Unigram Entropy : 3.889
Bigram Entropy  : 0.9288
Trigram Entropy : 0.5121

Enter a sentence: natural language processing

Next Word Predictions:
the Probability: 0.5
is Probability: 0.5

================== RESTART: C:/Users/cravi/OneDrive/Desktop/Jabastian college/NLP folder/NLP CO3 AT1/program 4.py =================
Enter an English sentence: the boy likes the bat

RULE-BASED TAGGER
[('the', 'DT'), ('boy', 'NN'), ('likes', 'NNS'), ('the', 'DT'), ('bat', 'NN')]

STOCHASTIC TAGGER
[('the', 'DT'), ('boy', 'NN'), ('likes', 'NNS'), ('the', 'DT'), ('bat', 'NN')]

TRANSFORMATION-BASED TAGGER
[('the', 'DT'), ('boy', 'NN'), ('likes', 'NNS'), ('the', 'DT'), ('bat', 'NN')]
