import os
import re

instructions_dir = "/Users/escobarsmacbook/Workspace/bengalisafe/paper/overleaf_instructions"
tex_path = "/Users/escobarsmacbook/Workspace/bengalisafe/paper/naymul_overleaf_acl_latex.tex"

with open(tex_path, "r", encoding="utf-8") as f:
    tex_content = f.read()

files = sorted(os.listdir(instructions_dir))
p_files = [f for f in files if f.startswith("P") and f.endswith(".md")]

print(f"Found {len(p_files)} P-files.")

for pf in p_files:
    pf_path = os.path.join(instructions_dir, pf)
    with open(pf_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r"^# (.*)", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else pf
    
    # Extract Fix Description
    fix_match = re.search(r"\*\*Fix\*\*:\s*(.*)", content, re.MULTILINE)
    if not fix_match:
        fix_match = re.search(r"\*\*Fix description\*\*:\s*(.*)", content, re.MULTILINE)
    fix_desc = fix_match.group(1).strip() if fix_match else "N/A"
    
    # Extract estimate time
    time_match = re.search(r"\*\*Total paste time\*\*:\s*(.*)", content, re.MULTILINE)
    if not time_match:
        time_match = re.search(r"Total paste time:\s*(.*)", content, re.IGNORECASE)
    time_desc = time_match.group(1).strip() if time_match else "N/A"
    
    # Let's try to see if REPLACE WITH is in the tex content, or FIND is in the tex content
    # We find all "### FIND" and "### REPLACE WITH" blocks
    find_blocks = re.findall(r"### FIND\s*[\r\n]+```(?:latex|bibtex|)\s*([\s\S]*?)```", content)
    replace_blocks = re.findall(r"### REPLACE WITH\s*[\r\n]+```(?:latex|bibtex|)\s*([\s\S]*?)```", content)
    
    # Let's clean block content for matching (remove leading/trailing spaces/newlines, and normalise whitespaces)
    def normalise(text):
        return re.sub(r"\s+", " ", text).strip()
    
    applied_status = "Unknown"
    if replace_blocks:
        all_replaced = True
        all_found_present = True
        for rb in replace_blocks:
            norm_rb = normalise(rb)
            # Check if a significant portion of replace block is in the tex file
            if norm_rb[:50] not in normalise(tex_content):
                all_replaced = False
                break
        
        for fb in find_blocks:
            norm_fb = normalise(fb)
            if norm_fb[:50] not in normalise(tex_content):
                all_found_present = False
                
        if all_replaced:
            applied_status = "Yes (Applied)"
        elif all_found_present:
            applied_status = "No (Not Applied)"
        else:
            applied_status = "Partial / Modified"
    else:
        # Check if there is ADD AFTER or other edit types
        applied_status = "No REPLACE blocks found"
        
    print(f"File: {pf}")
    print(f"Title: {title}")
    print(f"Fix: {fix_desc}")
    print(f"Time: {time_desc}")
    print(f"Status: {applied_status}")
    print("-" * 50)
