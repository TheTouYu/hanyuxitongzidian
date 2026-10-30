import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\卷七十一聿.json",encoding="utf-8"))
print(d.get("char"),d.get("chapter"))
for s in d["sections"]: print(repr(s.get("key")),repr(s.get("label")),(s.get("text") or "")[:30])