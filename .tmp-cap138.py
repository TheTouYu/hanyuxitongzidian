import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\奚.json",encoding="utf-8"))
for s in d["sections"]:
    for g in (s.get("groups") or []):
        print("==",g["title"])
        for r in g["rows"]: print("  ",r[0],"|",r[1],"|",r[2],"|",str(r[3])[:70])