# -*- coding: utf-8 -*-
import os,json,io,sys,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards"); INL=os.path.join(ROOT,"web","public","glyphs","inline")
SRC={"benyi":"benyi","bengen":"benyi","shiyi":"benyi","bianzheng":"bianzheng","zhuanyi":"zhuanyi","yinyuan":"yinyuan"}
n=g=0
for p in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(p)
    if b=="index.json": continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    ch2=False
    for s in d.get("sections",[]):
        src=SRC.get(s.get("key",""))
        if not src: continue
        dd=os.path.join(INL,ch,src)
        if os.path.isdir(dd):
            files=sorted(os.listdir(dd))
            if files:
                s["gimgs"]=[f"inline/{ch}/{src}/{f}" for f in files[:8]]; g+=1; ch2=True
    if ch2:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("回填卡",n,"插图点",g)