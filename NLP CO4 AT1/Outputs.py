Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\cravi\OneDrive\Desktop\Jabastian college\NLP folder\NLP CO4 AT1\program 1.py
--- TASK 1: Action-Object Extraction ---
Query: 'Activate international roaming for my number.' -> Semantic Representation: ACTIVATE(Roaming, Customer)
Query: 'Deactivate caller tune service.' -> Semantic Representation: DEACTIVATE(CallerTune, Customer)
Query: 'Check my data balance.' -> Semantic Representation: QUERY(DataBalance, Customer)
Query: 'Enable 5G service.' -> Semantic Representation: ACTIVATE(5GService, Customer)

--- TASK 2: Error Identification ---
[Q1] Actual: 'Activate Roaming' | Predicted: 'Activate Roaming' -> CORRECT
[Q2] Actual: 'Deactivate Caller Tune' | Predicted: 'Activate Caller Tune' -> ERROR DETECTED
[Q3] Actual: 'Query Data Balance' | Predicted: 'Query Data Balance' -> CORRECT
[Q4] Actual: 'Activate 5G Service' | Predicted: 'Activate 5G Service' -> CORRECT

= RESTART: C:\Users\cravi\OneDrive\Desktop\Jabastian college\NLP folder\NLP CO4 AT1\program 2.py
--- TASK 1 & 2: Inference Results ---
Producing Machines   : ['M1', 'M2', 'M4']
Non-Producing Machines: ['M3']
Available Products   : ['Shaft', 'Engine', 'Gear']

--- TASK 3: Impact Analysis on Gear ---
Machines configured for Gear: ['M2', 'M3']
Active Gear Machines        : ['M2']
Gear Production Affected?   : Yes, capacity reduced, but product remains AVAILABLE via ['M2'].

================== RESTART: C:\Users\cravi\OneDrive\Desktop\Jabastian college\NLP folder\NLP CO4 AT1\program 3.py =================
--- TASK 1 & 2: Disambiguation Results ---
Query: 'Apple accessories' | Clicked Result: 'iPhone Charger'
 -> Disambiguated Sense: [Technology Brand]

Query: 'Mouse wireless' | Clicked Result: 'Bluetooth Mouse'
 -> Disambiguated Sense: [Computer Device]

Query: 'Java tutorial' | Clicked Result: 'Coding Lessons'
 -> Disambiguated Sense: [Programming Language]

Query: 'Python course' | Clicked Result: 'Software Development Training'
 -> Disambiguated Sense: [Programming Language]

>>> 
================== RESTART: C:\Users\cravi\OneDrive\Desktop\Jabastian college\NLP folder\NLP CO4 AT1\program 4.py =================
--- TASK 1 & 2: Semantic Role Assignment ---
Sentence: 'Doctor prescribed medicine to patient.'
  - Entity: Doctor          | Assigned Role: Agent
  - Entity: medicine        | Assigned Role: Instrument

Sentence: 'Patient reported severe headache.'
  - Entity: Patient         | Assigned Role: Recipient
  - Entity: headache        | Assigned Role: Symptom

Sentence: 'Nurse monitored patient continuously.'
  - Entity: Nurse           | Assigned Role: Agent
  - Entity: patient         | Assigned Role: Recipient

Sentence: 'Medicine reduced blood pressure.'
  - Entity: Medicine        | Assigned Role: Instrument
  - Entity: blood pressure  | Assigned Role: Biological Parameter

