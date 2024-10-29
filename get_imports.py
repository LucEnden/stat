# print the version of ALL the libraries I will be using in this study
import os
import json

notebook_path = os.path.abspath("./research.ipynb")
with open(notebook_path, 'r') as f:
    notebook_content = json.loads(f.read())

imports = set()
# we can ignore this code block, which is the first element
for i in list(notebook_content.values())[0][1:]:
    if i["cell_type"] == "code":
        for line in i["source"]:
            if "import" in line and not line.startswith("#"):
                imports.add(line.strip())

for i in imports:
    print(i)