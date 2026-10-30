import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\支.json",encoding="utf-8"))
for g in d["sections"][-2]["groups"]:
    print(g["title"],len(g["rows"]),[r[0] for r in g["rows"]][:8])