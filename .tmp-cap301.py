import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\秭.json",encoding="utf-8"))
print(d.get("head"),d.get("level"),d.get("parent"),d.get("bus"))
for s in d["sections"]: print(s["key"],"|",(s.get("text") or "")[:70])