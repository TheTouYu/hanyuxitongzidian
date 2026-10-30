import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\祟.json",encoding="utf-8"))
print("head",d.get("head"),"alias",d.get("aliases"))
for s in d["sections"]:
    print(s["key"],"text:",repr(s.get("text"))[:40],"groups:",[(g["title"],len(g["rows"])) for g in (s.get("groups") or [])])
print("keys",list(d.keys()))