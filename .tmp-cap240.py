# -*- coding: utf-8 -*-
import sys,os,json,io,re,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
LAB=re.compile(r"^\s*(?:【[^】]*】\s*)?(?:本義|本义|轉義|转义|辯證|辩证|音源|字源|字族衍義|字族衍义|說文|说文)\s*[：:]\s*")
n=0; gi=0
for p in glob.glob(os.path.join(C,"*.json")):
    if os.path.basename(p)=="index.json": continue
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    ch=d.get("char") or os.path.basename(p)[:-5]
    if len(ch)>1: continue
    gd=os.path.join(G,ch); files=[]
    if os.path.isdir(gd): files=sorted(f for f in os.listdir(gd) if f.endswith(".png"))
    changed=False
    for s in d.get("sections",[]):
        t=s.get("text") or ""
        t2=LAB.sub("",t)
        if t2!=t: s["text"]=t2; changed=True
        if s.get("key")=="benyi" and files and d.get("level",3)<=2:
            s["gimgs"]=files[:8]; gi+=1; changed=True
    if changed:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改卡",n,"插字形",gi)