import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\示.json",encoding="utf-8"))
for s in d["sections"]: print(s["key"],"|",s.get("label"),"|",len(s.get("text") or ""),"| groups",len(s.get("groups") or []))