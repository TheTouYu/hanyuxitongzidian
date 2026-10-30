import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\矢.json",encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="erji" or "二级" in (s.get("label") or ""):
        print(json.dumps(s,ensure_ascii=False))