import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\夷.json",encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            print(g["title"][:24],len(g["rows"]))
            for r in g["rows"]: print("  ",r[0],"|",r[1],"|",r[2])