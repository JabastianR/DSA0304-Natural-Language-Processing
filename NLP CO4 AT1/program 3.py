sense_dictionary = {
    "Apple": {
        "Fruit": ["fruit", "tree", "eat", "juice", "sweet", "organic"],
        "Technology Brand": ["iphone", "charger", "macbook", "tech", "device", "ios"]
    },
    "Mouse": {
        "Animal": ["rodent", "pest", "cheese", "animal", "trap"],
        "Computer Device": ["bluetooth", "wireless", "usb", "click", "hardware", "pc"]
    },
    "Java": {
        "Island": ["indonesia", "island", "coffee", "travel", "caribbean"],
        "Programming Language": ["coding", "lessons", "software", "code", "developer", "syntax"]
    },
    "Python": {
        "Snake": ["reptile", "snake", "zoo", "species", "wildlife"],
        "Programming Language": ["software", "development", "training", "code", "course", "script"]
    }
}

search_logs = [
    ("Apple accessories", "iPhone Charger", "Apple"),
    ("Mouse wireless", "Bluetooth Mouse", "Mouse"),
    ("Java tutorial", "Coding Lessons", "Java"),
    ("Python course", "Software Development Training", "Python")
]

def disambiguate_sense(target_word, context_text):
    context_words = set(context_text.lower().split())
    senses = sense_dictionary[target_word]
    
    best_sense = None
    max_overlap = -1
    
    for sense_name, keywords in senses.items():
        overlap = len(context_words.intersection(set(keywords)))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense_name
            
    return best_sense

print("--- TASK 1 & 2: Disambiguation Results ---")
for query, click, target in search_logs:
    selected_sense = disambiguate_sense(target, click)
    print(f"Query: '{query}' | Clicked Result: '{click}'")
    print(f" -> Disambiguated Sense: [{selected_sense}]\n")
