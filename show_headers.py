import os

instructions_dir = "/Users/escobarsmacbook/Workspace/bengalisafe/paper/overleaf_instructions"
p_files = [
    "P7_expanded_related_comparison_table.md",
    "P8_case_anchoring_section.md",
    "P8b_case_anchor_appendix.md",
    "P9_asr_definition.md",
    "P10_cross_judge_audit_full_rewrite.md",
    "P11_corpus_coverage_appendix.md",
    "P12_binary_collapse_defense.md",
    "P13_prompt_level_guard_audit.md",
    "P14_journalism_cover_examples.md",
    "P15_per_model_asr_table.md",
    "P16_ssc_suicide_qualitative.md"
]

for pf in p_files:
    path = os.path.join(instructions_dir, pf)
    print(f"=== File: {pf} ===")
    if not os.path.exists(path):
        print("NOT FOUND")
        continue
    with open(path, "r") as f:
        lines = [f.readline() for _ in range(35)]
    print("".join([l for l in lines if l]))
    print("="*60 + "\n")
