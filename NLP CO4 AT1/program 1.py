queries_data = [
    {"id": "Q1", "text": "Activate international roaming for my number.", "actual": "Activate Roaming", "predicted": "Activate Roaming"},
    {"id": "Q2", "text": "Deactivate caller tune service.", "actual": "Deactivate Caller Tune", "predicted": "Activate Caller Tune"},
    {"id": "Q3", "text": "Check my data balance.", "actual": "Query Data Balance", "predicted": "Query Data Balance"},
    {"id": "Q4", "text": "Enable 5G service.", "actual": "Activate 5G Service", "predicted": "Activate 5G Service"}
]

# Task 1: Parse Action-Object Relationships
def parse_semantic_frame(text):
    words = text.lower().split()
    if "activate" in words or "enable" in words:
        action = "ACTIVATE"
    elif "deactivate" in words or "disable" in words:
        action = "DEACTIVATE"
    elif "check" in words or "query" in words:
        action = "QUERY"
    else:
        action = "UNKNOWN"
        
    if "roaming" in words:
        obj = "Roaming"
    elif "caller" in words or "tune" in words:
        obj = "CallerTune"
    elif "data" in words or "balance" in words:
        obj = "DataBalance"
    elif "5g" in words:
        obj = "5GService"
    else:
        obj = "Unknown"
        
    return f"{action}({obj}, Customer)"

print("--- TASK 1: Action-Object Extraction ---")
for q in queries_data:
    print(f"Query: '{q['text']}' -> Semantic Representation: {parse_semantic_frame(q['text'])}")

print("\n--- TASK 2: Error Identification ---")
for q in queries_data:
    is_error = q["actual"] != q["predicted"]
    status = "ERROR DETECTED" if is_error else "CORRECT"
    print(f"[{q['id']}] Actual: '{q['actual']}' | Predicted: '{q['predicted']}' -> {status}")
