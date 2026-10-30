import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\市.json",encoding="utf-8"))
for g in d["sections"][-1]["groups"]:
    print("##",g["title"])
    for r in g["rows"]:
        print(" |".join(r)[:120])