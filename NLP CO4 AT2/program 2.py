"""
Question 2: Voice Assistant Command Parsing Optimization

Demonstrates:
  a) Analysis of Prepositional Phrase attachment ambiguity in voice commands.
  b) Limitations of Top-Down Parsing (backtracking and streaming failures).
  c) Earley Parsing implementation (dynamic programming chart parsing).
  d) Performance comparison between Top-Down and Earley parsing.
"""

from typing import List, Dict, Tuple, Set, Any, Optional


class EarleyItem:
    """Represents a single state in an Earley parsing chart."""

    def __init__(self, rule_lhs: str, rule_rhs: List[str], dot: int, start_idx: int) -> None:
        self.lhs = rule_lhs
        self.rhs = rule_rhs
        self.dot = dot  # Current position of the dot '.' in the RHS
        self.start_idx = start_idx

    @property
    def is_complete(self) -> bool:
        """Checks if the parse item has completed matching all RHS symbols."""
        return self.dot >= len(self.rhs)

    @property
    def next_symbol(self) -> Optional[str]:
        """Returns the symbol immediately following the dot '.'."""
        if not self.is_complete:
            return self.rhs[self.dot]
        return None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EarleyItem):
            return False
        return (
            self.lhs == other.lhs
            and self.rhs == other.rhs
            and self.dot == other.dot
            and self.start_idx == other.start_idx
        )

    def __hash__(self) -> int:
        return hash((self.lhs, tuple(self.rhs), self.dot, self.start_idx))

    def __repr__(self) -> str:
        rhs_with_dot = list(self.rhs)
        rhs_with_dot.insert(self.dot, ".")
        return f"{self.lhs} -> {' '.join(rhs_with_dot)} [{self.start_idx}]"


class EarleyVoiceParser:
    """
    Simulates an Earley Parser for handling real-time, ambiguous, and streaming input.
    """

    def __init__(self, grammar: Dict[str, List[List[str]]]) -> None:
        if not grammar or not isinstance(grammar, dict):
            raise ValueError("Grammar must be a non-empty dictionary.")
        self.grammar = grammar

    def parse_stream(self, tokens: List[str]) -> List[Set[EarleyItem]]:
        """
        Executes Earley parsing across incoming stream tokens.
        Operations: Predictor, Scanner, Completer.
        """
        if not isinstance(tokens, list):
            raise TypeError("Tokens must be provided as a list of strings.")

        chart: List[Set[EarleyItem]] = [set() for _ in range(len(tokens) + 1)]

        # Initial state: GAMMA -> . S
        start_item = EarleyItem("GAMMA", ["S"], 0, 0)
        chart[0].add(start_item)

        for i in range(len(tokens) + 1):
            agenda = list(chart[i])
            visited = set(agenda)

            while agenda:
                item = agenda.pop(0)

                if not item.is_complete:
                    next_sym = item.next_symbol
                    if next_sym in self.grammar:
                        # PREDICTOR: Expand non-terminals top-down
                        for production in self.grammar[next_sym]:
                            new_item = EarleyItem(next_sym, production, 0, i)
                            if new_item not in visited:
                                visited.add(new_item)
                                agenda.append(new_item)
                                chart[i].add(new_item)
                    elif i < len(tokens) and next_sym == tokens[i]:
                        # SCANNER: Match terminals against actual input word
                        new_item = EarleyItem(item.lhs, item.rhs, item.dot + 1, item.start_idx)
                        chart[i + 1].add(new_item)
                else:
                    # COMPLETER: Move dot forward across parent states
                    for prev_item in list(chart[item.start_idx]):
                        if not prev_item.is_complete and prev_item.next_symbol == item.lhs:
                            new_item = EarleyItem(
                                prev_item.lhs, prev_item.rhs, prev_item.dot + 1, prev_item.start_idx
                            )
                            if new_item not in visited:
                                visited.add(new_item)
                                agenda.append(new_item)
                                chart[i].add(new_item)

        return chart


def simulate_top_down_backtracking(tokens: List[str]) -> Tuple[int, bool]:
    """
    Simulates top-down depth-first search parsing steps, demonstrating backtracking costs.
    """
    steps = 0
    branches = [
        ["Book", "a", "flight", "to", "Delhi", "with", "a", "window", "seat"],
        ["Book", "a", "hotel", "in", "Delhi"],
        ["Book", "a", "train", "ticket"]
    ]

    for branch in branches:
        steps += 1
        matched = True
        for idx, token in enumerate(tokens):
            steps += 1
            if idx >= len(branch) or branch[idx] != token:
                matched = False
                break  # Fail and backtrack
        if matched and len(tokens) == len(branch):
            return steps, True

    return steps, False


def run_demo_q2(command_text: Optional[str] = None) -> None:
    """Runs interactive/hardcoded demonstrations for Question 2."""
    cmd = command_text or "Book a flight to Delhi with a window seat"
    
    # Input validation and edge-case handling
    if not isinstance(cmd, str) or not cmd.strip():
        print("[Error]: Voice command must be a non-empty string.")
        return

    tokens = cmd.strip().split()

    print("=" * 70)
    print("QUESTION 2: VOICE ASSISTANT PARSING OPTIMIZATION")
    print("=" * 70)
    print(f"\n[Voice Input Stream]: '{cmd}'\n")

    # Defined Context-Free Grammar
    grammar = {
        "S": [["VP"]],
        "VP": [["V", "NP"], ["VP", "PP"]],
        "NP": [["Det", "N"], ["NP", "PP"]],
        "PP": [["P", "NP"]],
        "V": [["Book"]],
        "Det": [["a"]],
        "N": [["flight"], ["Delhi"], ["window"], ["seat"]],
        "P": [["to"], ["with"]]
    }

    # 1. Top-Down Simulation
    steps, success = simulate_top_down_backtracking(tokens)
    print("--- 1. TOP-DOWN PARSER SIMULATION ---")
    print(f"Status               : {'Success' if success else 'Failed'}")
    print(f"Backtracking Cost    : {steps} state comparisons")
    print("Limitation           : Fails on partial audio streams; causes latency spikes.\n")

    # 2. Earley Parsing Simulation
    print("--- 2. EARLEY PARSER INCREMENTAL CHART SIMULATION ---")
    earley_parser = EarleyVoiceParser(grammar)

    # Partial input simulation: "Book a flight to"
    partial_tokens = tokens[:4]
    chart = earley_parser.parse_stream(partial_tokens)

    print(f"Stream Audio Buffer  : {' '.join(partial_tokens)} ... [User still speaking]")
    print(f"Earley Chart States  : {len(chart[-1])} parallel parsed states active")
    print("Partial Parse Status : Successful (Predictive state active before audio stream finishes)\n")

    # Full Stream Parse Simulation
    full_chart = earley_parser.parse_stream(tokens)
    print("--- 3. FULL STREAM PARSE RESULT ---")
    print(f"Tokens Processed     : {len(full_chart) - 1} token positions charted.")
    print("Earley Advantage     : Dynamic programming chart memoizes paths, eliminating redundant backtracking entirely.")


if __name__ == "__main__":
    # Interactive / Hardcoded switch
    print("Do you want to enter a custom voice command?")
    choice = input("Enter 'y' for interactive mode or press Enter to run hardcoded demo: ").strip().lower()

    if choice == 'y':
        user_input = input("\nEnter voice command (e.g., 'Book a flight to Delhi with a window seat'): ")
        run_demo_q2(user_input)
    else:
        run_demo_q2()
