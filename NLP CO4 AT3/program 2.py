"""
Question 2: Top-Down Backtracking vs Earley Chart Parsing
"""

# Earley Chart Item Representation
class EarleyItem:
    def __init__(self, rule_lhs: str, rhs: list, dot: int, start: int):
        self.lhs = rule_lhs
        self.rhs = rhs
        self.dot = dot      # Position of dot (.) in RHS
        self.start = start  # Start position in input stream

    def __repr__(self):
        rhs_curr = self.rhs[:self.dot] + ["."] + self.rhs[self.dot:]
        return f"{self.lhs} -> {' '.join(rhs_curr)} (Origin: {self.start})"

# Partial streaming input
stream_tokens = ["Book", "a", "flight"]
grammar = {"S": [["VP"]], "VP": [["V", "NP"]], "V": [["Book"]]}

# Simulated Earley State Chart at Position 1 ("Book" scanned)
chart_slot_1 = [
    EarleyItem("VP", ["V", "NP"], 1, 0),  # Scanned 'Book', now expecting 'NP'
    EarleyItem("NP", ["Det", "N"], 0, 1)  # Predictor pre-emptively expands NP
]

print("Earley Chart State after processing stream 'Book':")
for item in chart_slot_1:
    print("  Active Item:", item)