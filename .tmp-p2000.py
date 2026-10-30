# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
ip=os.path.join(P,"index.json"); ix=json.load(io.open(ip,encoding="utf-8")); ph=ix.get("photos") or ix
fixed=[]
for fn in sorted(os.listdir(C)):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or fn[:-5]
    dirp=os.path.join(P,ch)
    actual=sorted(os.listdir(dirp)) if os.path.isdir(dirp) else []
    own=d.get("photos") or []
    if own and actual and not all(os.path.exists(os.path.join(dirp,f)) for f in own):
        d["photos"]=actual; json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fixed.append((ch,own,actual))
    if actual and ph.get(ch)!=actual:
        ph[ch]=actual
json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
print("fixed",fixed[:8],"n",len(fixed))