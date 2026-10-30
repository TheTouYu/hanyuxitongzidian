import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    ph=d.get("photos") or []
    if len(ph)>=6:
        ch=d.get("char")
        miss=[f for f in ph if not os.path.exists(os.path.join(P,ch,f))]
        print(ch,len(ph),len(miss),ph[:3])