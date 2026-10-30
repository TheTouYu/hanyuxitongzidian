# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
md=r"D:\系统汉字\knowledge\hanzi-yinyuan\02y-zika.md"
t=io.open(md,encoding="utf-8").read()
blocks=re.split(r"<!-- CLAIM:START ",t)
m={}
for b in blocks[1:]:
    mm=re.search(r"###\s*(.+?)\n",b)
    bb=re.search(r"第\s*(\d+)\s*部「(.+?)部」",b)
    if not mm or not bb: continue
    title=mm.group(1).strip()
    ch=title[0]
    if ch in m: continue
    m[ch]=(int(bb.group(1)), bb.group(2))
print("claims",len(blocks)-1,"chars",len(m))
cards={}
for f in os.listdir(C):
    if f.endswith(".json") and f not in ("index.json","variants.json"):
        try: cards[f[:-5]]=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
        except Exception: pass
def busnum(d):
    b=d.get("bus")
    if isinstance(b,list) and b and isinstance(b[0],dict): return b[0].get("num")
    if isinstance(b,dict): return b.get("num")
    return None
fixed=0
for ch,d in cards.items():
    if d.get("level")!=3 or busnum(d): continue
    v=m.get(ch)
    if not v: continue
    d["bus"]=[{"num":v[0],"name":v[1]}]
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    fixed+=1
print("fixed",fixed)