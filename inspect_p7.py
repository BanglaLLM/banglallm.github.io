import os

tex_path = "/Users/escobarsmacbook/Workspace/bengalisafe/paper/naymul_overleaf_acl_latex.tex"
with open(tex_path, "r", encoding="utf-8") as f:
    tex_content = f.read()

# find \label{tab:related_comparison} and print 15 lines before and after
pos = tex_content.find("label{tab:related_comparison}")
if pos != -1:
    print(tex_content[pos-300:pos+1000])
else:
    print("Not found label")
