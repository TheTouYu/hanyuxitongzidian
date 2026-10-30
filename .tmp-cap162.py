import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for ch in ("欠","气"):
    d=json.load(io.open(rf"D:\系统汉字\web\public\cards\{ch}.json",encoding="utf-8"))
    print("##",ch)
    for s in d["sections"][:3]: print(" ",s["key"],"|",(s.get("text") or "")[:70])