import os

tex_path = "/Users/escobarsmacbook/Workspace/bengalisafe/paper/naymul_overleaf_acl_latex.tex"
with open(tex_path, "r", encoding="utf-8") as f:
    tex_content = f.read()

pos = tex_content.find("label{sec:results:audit}")
if pos != -1:
    print(tex_content[pos:pos+1000])
else:
    print("Not found label")
