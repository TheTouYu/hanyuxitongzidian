import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\至.json",encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            print(g["title"],len(g["rows"]))
            for r in g["rows"]:
                if r[0].startswith("芪"): print("  芪行",r[:4])