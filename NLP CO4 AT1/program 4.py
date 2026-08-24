sentences = [
    {"text": "Doctor prescribed medicine to patient.", "svo": ("Doctor", "prescribed", "medicine")},
    {"text": "Patient reported severe headache.", "svo": ("Patient", "reported", "headache")},
    {"text": "Nurse monitored patient continuously.", "svo": ("Nurse", "monitored", "patient")},
    {"text": "Medicine reduced blood pressure.", "svo": ("Medicine", "reduced", "blood pressure")}
]

entity_ontology = {
    "doctor": "Agent",
    "nurse": "Agent",
    "medicine": "Instrument",
    "patient": "Recipient",
    "headache": "Symptom",
    "blood pressure": "Biological Parameter"
}

def assign_semantic_roles(svo_tuple):
    subj, verb, obj = svo_tuple
    
    subj_role = entity_ontology.get(subj.lower(), "Theme")
    obj_role = entity_ontology.get(obj.lower(), "Theme")
    
    return {subj: subj_role, obj: obj_role}

print("--- TASK 1 & 2: Semantic Role Assignment ---")
for s in sentences:
    roles = assign_semantic_roles(s["svo"])
    print(f"Sentence: '{s['text']}'")
    for entity, role in roles.items():
        print(f"  - Entity: {entity:15} | Assigned Role: {role}")
    print()
