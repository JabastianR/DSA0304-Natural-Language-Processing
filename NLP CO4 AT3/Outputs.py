Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\cravi\OneDrive\Desktop\Jabastian college\NLP folder\NLP CO4 AT3\program 1.py
CFG Constituent Hierarchy:
{'S': {'NP': {'Det': 'The', 'N': 'patient'}, 'VP': {'V': 'took', 'NP': {'Det': 'the', 'N': 'medication'}}}}

Dependency Head-Dependent Arcs:
'The' --(det)--> Head Index: 2
'patient' --(nsubj)--> Head Index: 3
'took' --(ROOT)--> Head Index: 0
'the' --(det)--> Head Index: 5
'medication' --(dobj)--> Head Index: 3
>>> 
= RESTART: C:\Users\cravi\OneDrive\Desktop\Jabastian college\NLP folder\NLP CO4 AT3\program 2.py
Earley Chart State after processing stream 'Book':
  Active Item: VP -> V . NP (Origin: 0)
  Active Item: NP -> . Det N (Origin: 1)
>>> 
= RESTART: C:\Users\cravi\OneDrive\Desktop\Jabastian college\NLP folder\NLP CO4 AT3\program 3.py
CFG Parses (Unranked): ['Tree_1 (PP attached to VP)', 'Tree_2 (PP attached to NP)']
PCFG Rule Probabilities: {'VP -> VP PP': 0.4, 'NP -> NP PP': 0.15}
Neural Model Scores: {'VP_Attachment': 3.7740000000000005, 'NP_Attachment': 0.8568}
>>> 
= RESTART: C:\Users\cravi\OneDrive\Desktop\Jabastian college\NLP folder\NLP CO4 AT3\program 4.py
Valid Agreement Unification  : None
Invalid Agreement Unification: None
Subcategorization Frame Valid: False
>>> 
= RESTART: C:\Users\cravi\OneDrive\Desktop\Jabastian college\NLP folder\NLP CO4 AT3\program 5.py
Transition-Based Generated Arcs (Linear Time O(N)):
  Arcs: [('runs', '->', 'She')]
  Remaining Stack: ['ROOT', 'runs']
