import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
by=z.get("byName") or {}
bad=[]
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    ch=d.get("char")
    if ch in by and d.get("level")!=1: bad.append((ch,d.get("level"),d.get("parent")))
print("部头字但 level≠1 的卡:",len(bad),bad[:15])