import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
ph=json.load(io.open(P+r"\index.json",encoding="utf-8")).get("photos")
for k in ("責","朿","策"):
    print(k, ph.get(k))
print("含朿的键", [k for k in ph if "朿" in k][:5])