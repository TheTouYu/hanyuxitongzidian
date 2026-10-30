import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\弔.json",encoding="utf-8"))
for s in d["sections"]:
    if "{{" in (s.get("text") or ""): print(s["key"], "|", s["text"][:130])