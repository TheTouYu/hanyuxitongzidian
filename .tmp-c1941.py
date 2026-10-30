import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=json.load(io.open(r"D:\系统汉字\web\public\cards\射.json",encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu": print("text:",repr(s.get("text")),"groups",len(s.get("groups",[])))