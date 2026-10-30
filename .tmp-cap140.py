import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\奚.json",encoding="utf-8"))
for s in d["sections"]:
    print(s["key"],"|",s.get("label"),"| text:",len(s.get("text") or ""),"| groups:",[(g.get("title"),len(g.get("rows") or [])) for g in (s.get("groups") or [])])