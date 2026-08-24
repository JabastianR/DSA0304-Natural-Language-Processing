"""
Question 3: CFG vs PCFG vs Neural Ambiguity Handling
"""
import math

# 1. CFG: Unranked ambiguous parses
cfg_parses = ["Tree_1 (PP attached to VP)", "Tree_2 (PP attached to NP)"]

# 2. PCFG: Probability-based ranking
pcfg_rules = {
    "VP -> VP PP": 0.40,  # Saw using telescope
    "NP -> NP PP": 0.15   # Man holding telescope
}

# 3. Neural Parser: Context-aware vector scoring
def neural_parse_scorer(context_vector: list) -> dict:
    # Simulated neural dense layer scoring logits
    score_vp_attach = sum(context_vector) * 1.85 
    score_np_attach = sum(context_vector) * 0.42
    return {"VP_Attachment": score_vp_attach, "NP_Attachment": score_np_attach}

print("CFG Parses (Unranked):", cfg_parses)
print("PCFG Rule Probabilities:", pcfg_rules)
context_emb = [0.25, 0.88, 0.91] # Input context representation
print("Neural Model Scores:", neural_parse_scorer(context_emb))
