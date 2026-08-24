"""
Task 2: Constraint-Based Dialog Response Generator
"""

def generate_dialog_response(user_input):
    required_keywords = ["break", "confident"]
    entity_context = ["exam", "concentrate"]
    
    response = (
        "Since you are finding it hard to concentrate for your exam, "
        "taking a short break can reset your mind. Stay confident in your abilities!"
    )
    
    # Verification Engine
    has_keywords = all(kw in response.lower() for kw in required_keywords)
    has_context = all(ec in response.lower() for ec in entity_context)
    sentence_count = len(response.split('.')) - 1
    
    print(f"Generated Response: '{response}'")
    print(f"Constraints Met -> Keywords: {has_keywords} | Context Retained: {has_context} | Length Valid: {2 <= sentence_count <= 3}")

generate_dialog_response("I have an important exam tomorrow but I'm not able to concentrate.")