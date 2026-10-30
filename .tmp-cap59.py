import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\家.json",encoding="utf-8"))
for s in d["sections"]:
    print(s["key"], s["label"], "groups", len(s.get("groups") or []))
    for g in s.get("groups") or []: print("  title",g.get("title"),"rows",len(g.get("rows") or []))