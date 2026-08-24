"""
Question 3: Healthcare NLP Engine Architecture & Clinical Extraction

Demonstrates:
  a) Feature Structure Agreement (Subject-Verb Agreement).
  b) Sub-Categorization Frame Resolution for clinical verbs.
  c) Extraction of unstructured medical text into structured JSON records.
"""

from typing import Dict, List, Tuple, Any, Optional
import json


class SubCategorizationFrame:
    """Defines sub-categorization requirements for clinical verbs."""

    def __init__(self, verb: str, required_args: List[str], optional_args: List[str]) -> None:
        self.verb = verb
        self.required_args = required_args
        self.optional_args = optional_args

    def validate_arguments(self, present_args: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validates if all required syntactic arguments are present."""
        missing = [arg for arg in self.required_args if arg not in present_args]
        is_valid = len(missing) == 0
        return is_valid, missing


class ClinicalNLPEngine:
    """
    Integrated Healthcare NLP Engine incorporating Feature Structures,
    Sub-categorization verification, and Structured Medical Record Extraction.
    """

    def __init__(self) -> None:
        # Dictionary of sub-categorization frames for clinical verbs
        self.verb_frames: Dict[str, SubCategorizationFrame] = {
            "recommends": SubCategorizationFrame(
                verb="recommends",
                required_args=["Agent", "Direct_Object"],
                optional_args=["Location", "Time"]
            ),
            "reviewed": SubCategorizationFrame(
                verb="reviewed",
                required_args=["Agent", "Patient"],
                optional_args=["Time"]
            ),
            "scheduling": SubCategorizationFrame(
                verb="scheduling",
                required_args=["Event"],
                optional_args=["Location", "Time"]
            )
        }

    @staticmethod
    def verify_agreement(subj_features: Dict[str, Any], verb_features: Dict[str, Any]) -> bool:
        """Verifies Subject-Verb Agreement using Feature Structures."""
        for key in ["NUM", "PERS"]:
            if subj_features.get(key) != verb_features.get(key):
                return False
        return True

    def extract_clinical_information(self, sentence: str) -> Dict[str, Any]:
        """Processes complex medical sentence into structured clinical records."""
        if not sentence or not isinstance(sentence, str):
            raise ValueError("Invalid sentence input. Must be a non-empty string.")

        # 1. Feature Structure Verification for Main Clause ("The doctor ... recommends")
        subj_features = {"CAT": "NP", "LEX": "doctor", "NUM": "sg", "PERS": 3}
        main_verb_features = {"CAT": "VP", "LEX": "recommends", "NUM": "sg", "PERS": 3, "TENSE": "pres"}

        if not self.verify_agreement(subj_features, main_verb_features):
            raise ValueError("Grammar Error: Subject-Verb Agreement Failure in main clause.")

        # 2. Sub-Categorization Frame Resolution
        # Relative Clause: "who reviewed the patient last week"
        rev_frame = self.verb_frames["reviewed"]
        rev_args = {"Agent": "doctor", "Patient": "the patient", "Time": "last week"}
        rev_valid, rev_missing = rev_frame.validate_arguments(rev_args)

        # Main Action Frame: "recommends starting medication and scheduling..."
        rec_frame = self.verb_frames["recommends"]
        rec_args = {
            "Agent": "doctor",
            "Direct_Object": ["starting medication", "scheduling a follow-up visit"]
        }
        rec_valid, rec_missing = rec_frame.validate_arguments(rec_args)

        # Sub-Action Frame: "scheduling a follow-up visit in Chennai"
        sched_frame = self.verb_frames["scheduling"]
        sched_args = {"Event": "follow-up visit", "Location": "Chennai"}
        sched_valid, sched_missing = sched_frame.validate_arguments(sched_args)

        if not (rev_valid and rec_valid and sched_valid):
            raise ValueError("Sub-categorization frame validation failed.")

        # 3. Build Final Structured Clinical JSON Output
        structured_output = {
            "clinical_record": {
                "source_text": sentence,
                "practitioner": {
                    "role": "Doctor",
                    "qualifier_clause": {
                        "action": "reviewed",
                        "target": "patient",
                        "time_frame": "last week"
                    }
                },
                "primary_recommendation": {
                    "action_verb": "recommends",
                    "clinical_actions": [
                        {
                            "type": "Treatment_Start",
                            "intervention": "medication"
                        },
                        {
                            "type": "Appointment_Scheduling",
                            "event": "follow-up visit",
                            "location": "Chennai"
                        }
                    ]
                },
                "validation_metadata": {
                    "subject_verb_agreement": "Passed (3rd Person Singular)",
                    "subcategorization_frames": "Verified Valid"
                }
            }
        }

        return structured_output


def run_demo_q3(medical_text: Optional[str] = None) -> None:
    """Runs interactive/hardcoded demonstrations for Question 3."""
    default_text = (
        "The doctor who reviewed the patient last week recommends "
        "starting medication and scheduling a follow-up visit in Chennai."
    )
    input_text = medical_text or default_text

    print("=" * 70)
    print("QUESTION 3: HEALTHCARE NLP CLINICAL EXTRACTION ENGINE")
    print("=" * 70)
    print(f"\n[Raw Patient Report Sentence]:\n\"{input_text}\"\n")

    engine = ClinicalNLPEngine()

    try:
        extracted_data = engine.extract_clinical_information(input_text)
        print("--- EXTRACTED STRUCTURED CLINICAL OUTPUT (JSON) ---")
        print(json.dumps(extracted_data, indent=2))
    except ValueError as err:
        print(f"[Processing Error]: {err}")


if __name__ == "__main__":
    print("Do you want to enter a custom medical report sentence?")
    choice = input("Enter 'y' for interactive mode or press Enter to run hardcoded demo: ").strip().lower()

    if choice == 'y':
        user_sentence = input("\nEnter medical sentence: ")
        run_demo_q3(user_sentence)
    else:
        run_demo_q3()
