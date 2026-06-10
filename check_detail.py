import os

tex_path = "/Users/escobarsmacbook/Workspace/bengalisafe/paper/naymul_overleaf_acl_latex.tex"
with open(tex_path, "r", encoding="utf-8") as f:
    tex_content = f.read()

checks = {
    "P7": ("Table 1", "related_comparison", "JailbreakBench", "IndicJR"),
    "P8": ("Case Anchoring Section", "sec:dataset:caseanchor", "Asiya", "Manindra Nath Biswas"),
    "P8b": ("Case Anchor Appendix", "app:case_anchor_distribution", "tcolorbox", "Cumilla Thakurpara"),
    "P9": ("ASR Definition", "Attack success rate (ASR)", "ASR}_{loose}"),
    "P10": ("Cross Judge Audit Full", "app:cross_judge_audit", "0.014", "statistically indistinguishable from zero"),
    "P11": ("Corpus Coverage Appendix", "app:corpus_coverage_details", "ALERT", "StrongREJECT", "80{,}587"),
    "P12": ("Binary Collapse Defense", "tab:judge_iaa", "substantial; \\citealp{landis1977measurement}", "clearing the $\\kappa \\geq 0.65$ threshold"),
    "P13": ("Prompt Level Guard Audit", "tab:guard_prompt_vs_response", "app:prompt_level_guard_audit", "the cover-narrative bypass is specifically a response-side miss"),
    "P14": ("Journalism Cover Examples", "deepseek-v4-pro__c-J-V1-1", "BTEB polytechnic", "certificate forgery scheme"),
    "P15": ("Per Model ASR Table", "app:per_model_asr", "Claude-Haiku-4.5", "Mistral-Medium-3"),
    "P16": ("SSC Suicide Qualitative", "sh-F-V1-1", "TigerLLM-9B-it", "Llama-3.3-70B", "adolescent-suicide")
}

print("=== CHECKING LaTeX FILE FOR EDITS ===")
for p_id, (name, *terms) in checks.items():
    print(f"\nChecking {p_id} ({name}):")
    found_any = False
    all_found = True
    for term in terms:
        is_in = term in tex_content
        print(f"  Term '{term}': {'FOUND' if is_in else 'NOT FOUND'}")
        if is_in:
            found_any = True
        else:
            all_found = False
    if all_found:
        print(f"--> Status: FULLY APPLIED")
    elif found_any:
        print(f"--> Status: PARTIALLY APPLIED")
    else:
        print(f"--> Status: NOT APPLIED")
