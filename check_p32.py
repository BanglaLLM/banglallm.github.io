import os

tex_path = "/Users/escobarsmacbook/Workspace/bengalisafe/paper/naymul_overleaf_acl_latex.tex"
with open(tex_path, "r", encoding="utf-8") as f:
    tex_content = f.read()

print("Robustness in tex:", "robustness" in tex_content.lower())
print("Negative results in tex:", "negative results" in tex_content.lower())
