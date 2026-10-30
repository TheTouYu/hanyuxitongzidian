# -*- coding: utf-8 -*-
import json,io,glob,os,sys,html
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
gi=json.load(io.open(r"D:\系统汉字\web\public\glyphs\index.json",encoding="utf-8"))["chars"]
n=0
for p in glob.glob(os.path.join(C,"*.json")):
    if p.endswith("index.json"): continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or os.path.basename(p)[:-5]
    g=gi.get(ch) or {}
    files=[f for f in (g.get("files") or []) if f.lower().endswith(".png")]
    if not files: continue
    figs="".join(f'<figure><img src="glyphs/{html.escape(f)}" alt="{i+1}"><figcaption>{i+1:02d}</figcaption></figure>' for i,f in enumerate(files))
    sec={"key":"zigen","label":"字形","text":f'<div class="gscroll">{figs}</div>',"cites":[]}
    secs=d["sections"]; idx=[i for i,s in enumerate(secs) if s.get("key")=="zigen"]
    if idx: secs[idx[0]]=sec
    else:
        pos=len(secs)
        for i,s in enumerate(secs):
            if s.get("key") in ("zizu","suoshujuan"): pos=i;break
        secs.insert(pos,sec)
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("写入字形栏",n)