import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(open(r"D:\系统汉字\web\public\cards\枳.json",encoding="utf-8"))
print(d.get("level"),d.get("parent"),[ (s["key"],s["label"]) for s in d["sections"]])
print(json.dumps(d["sections"][:3],ensure_ascii=False)[:700])