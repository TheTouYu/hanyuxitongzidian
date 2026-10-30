# -*- coding: utf-8 -*-
import json,io,os,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
# 1) label 统一
n=0
for p in glob.glob(os.path.join(C,"*.json")):
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    ch=False
    for s in d.get("sections",[]):
        if s.get("key")=="suoshujuan" and s.get("label")!="所属卷":
            s["label"]="所属卷"; ch=True
    if ch: json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("labels fixed",n)
# 2) photos 合并进 glyph index（带 caption）
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
ph=json.load(io.open(os.path.join(G,"photos","index.json"),encoding="utf-8")); pm=ph.get("photos") or ph
cp=json.load(io.open(os.path.join(G,"photos","captions.json"),encoding="utf-8")); cm=cp.get("captions") or cp
photos=gi.setdefault("photos",{})
k=0
for ch,files in pm.items():
    caps=cm.get(ch) or []
    arr=[]
    for i,f in enumerate(files):
        cap=caps[i] if i<len(caps) else ""
        arr.append({"file":f,"caption":cap})
    photos[ch]=arr; k+=1
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("photos merged",k)