"""
Question 4: Feature Structure Unification & Subcategorization
"""

def unify_features(fs1: dict, fs2: dict) -> dict | None:
    """Performs Feature Structure Unification for Subject-Verb Agreement."""
    unified = fs1.copy()
    for key, val in fs2.items():
        if key in unified:
            if unified[key] != val:
                return None  # Unification Failure (Agreement Error)
        else:
            unified[key] = val
    return unified

# Feature Structure Unification Check
subj_features = {"CAT": "NP", "NUM": "sg", "PERS": 3}
verb_valid    = {"CAT": "VP", "NUM": "sg", "PERS": 3}
verb_invalid  = {"CAT": "VP", "NUM": "pl", "PERS": 3}

print("Valid Agreement Unification  :", unify_features(subj_features, verb_valid))
print("Invalid Agreement Unification:", unify_features(subj_features, verb_invalid))

# Subcategorization Frame Validation
subcat_frames = {"devour": ["Agent", "DirectObject"]}
present_args = ["Agent"] # Missing Direct Object

is_valid = set(subcat_frames["devour"]).issubset(set(present_args))
print("Subcategorization Frame Valid:", is_valid)