import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
out=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    for s in d.get("sections") or []:
        t=s.get("text") or ""
        if "拟态义一面" in t or "取一面：" in t:
            out.append((fn[:-5], d.get("pinyin",""), next((x.get("text","")[:40] for x in d["sections"] if x["key"] in ("shiyi","benyi")),"")))
            break
out.sort()
for c,p,g in out: print(c,"|",p,"|",g[:34])