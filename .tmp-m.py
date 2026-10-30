import json
d=json.load(open(r"web\public\docx-index.json",encoding="utf-8"))["chars"]
for ch in ("茁","出"):
    for e in d.get(ch,[])[:2]: print(ch,"p",e["p"],"|",e["t"][:180])