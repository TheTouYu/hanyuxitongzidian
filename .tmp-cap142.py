import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\旨.json",encoding="utf-8"))
for s in d["sections"]:
    print("##",s["key"],s.get("label"))
    print((s.get("text") or "")[:200])