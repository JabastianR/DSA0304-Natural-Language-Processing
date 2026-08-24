"""
Question 1: CFG vs Dependency Structure Representation
"""

# CFG Tree Representation (Nested Constituent Structure)
cfg_tree = {
    "S": {
        "NP": {"Det": "The", "N": "patient"},
        "VP": {
            "V": "took",
            "NP": {"Det": "the", "N": "medication"}
        }
    }
}

# Dependency Parsing Representation (Direct Head -> Dependent Relations)
dependency_graph = [
    {"id": 1, "text": "The", "head": 2, "dep": "det"},
    {"id": 2, "text": "patient", "head": 3, "dep": "nsubj"},  # Subject directly linked to verb
    {"id": 3, "text": "took", "head": 0, "dep": "ROOT"},      # Core predicate
    {"id": 4, "text": "the", "head": 5, "dep": "det"},
    {"id": 5, "text": "medication", "head": 3, "dep": "dobj"} # Direct object linked to verb
]

print("CFG Constituent Hierarchy:")
print(cfg_tree)
print("\nDependency Head-Dependent Arcs:")
for arc in dependency_graph:
    print(f"'{arc['text']}' --({arc['dep']})--> Head Index: {arc['head']}")