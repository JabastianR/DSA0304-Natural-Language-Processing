"""
Task 1: Rule-Based Coreference Resolution Engine
"""

def resolve_coreference():
    entities = {
        "John": {"gender": "M", "num": "sg", "animate": True},
        "Mary": {"gender": "F", "num": "sg", "animate": True},
        "park": {"gender": "N", "num": "sg", "animate": False},
        "ball": {"gender": "N", "num": "sg", "animate": False},
        "dog":  {"gender": "M", "num": "sg", "animate": True}
    }
    
    pronouns = [
        {"token": "He", "gender": "M", "num": "sg", "animate": True},
        {"token": "She", "gender": "F", "num": "sg", "animate": True},
        {"token": "it", "gender": "N", "num": "sg", "animate": False},
        {"token": "him", "gender": "M", "num": "sg", "animate": True}
    ]

    print("--- Coreference Unification Results ---")
    for pronoun in pronouns:
        candidates = [
            name for name, feat in entities.items()
            if feat["gender"] == pronoun["gender"] and feat["num"] == pronoun["num"]
        ]
        print(f"Pronoun '{pronoun['token']}' matches domain: {candidates}")

resolve_coreference()