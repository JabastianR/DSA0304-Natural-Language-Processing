"""
Question 5: Transition-Based vs Graph-Based Parsing Simulation
"""

class TransitionParser:
    """Simulates a Transition-Based (Shift-Reduce) Dependency Parser."""
    def __init__(self, tokens: list):
        self.stack = ["ROOT"]
        self.buffer = tokens
        self.arcs = []

    def parse_step(self, action: str):
        if action == "SHIFT" and self.buffer:
            self.stack.append(self.buffer.pop(0))
        elif action == "LEFT-ARC" and len(self.stack) >= 2:
            dependent = self.stack.pop(-2)
            head = self.stack[-1]
            self.arcs.append((head, "->", dependent))
        elif action == "RIGHT-ARC" and len(self.stack) >= 2:
            dependent = self.stack.pop()
            head = self.stack[-1]
            self.arcs.append((head, "->", dependent))

# Process tokens in linear O(N) steps
parser = TransitionParser(["She", "runs"])
parser.parse_step("SHIFT")      # Move 'She' to Stack
parser.parse_step("SHIFT")      # Move 'runs' to Stack
parser.parse_step("LEFT-ARC")   # 'runs' -> 'She' (nsubj)

print("Transition-Based Generated Arcs (Linear Time O(N)):")
print("  Arcs:", parser.arcs)
print("  Remaining Stack:", parser.stack)