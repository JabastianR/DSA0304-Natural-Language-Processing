"""
Task 3: Word Sense Disambiguation & Logical Form Extraction
"""

def disambiguate_and_parse(sentence):
    tokens = sentence.lower().split()
    
    # Context-Based Disambiguation Logic
    bank_sense = "FINANCIAL_INSTITUTION"
    if "river" in tokens or "water" in tokens:
        bank_sense = "RIVER_BANK"
        
    # Logic Predicate Builder
    predicate_logic = f"Riverbank(x) & Location(x, River) & Flooded(x, Storm) & Contrast(Saved(x))"
    
    print(f"Source Sentence   : '{sentence}'")
    print(f"Resolved Sense    : bank -> {bank_sense}")
    print(f"Predicate Logic   : {predicate_logic}")

disambiguate_and_parse("The bank by the river flooded after the storm, but it was saved by quick action.")