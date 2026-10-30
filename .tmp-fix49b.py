# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
ph=json.load(io.open(os.path.join(G,"photos","index.json"),encoding="utf-8")); pm=ph.get("photos") or ph
cp=json.load(io.open(os.path.join(G,"photos","captions.json"),encoding="utf-8")); cm=cp.get("captions") or cp
photos=gi.setdefault("photos",{}); k=0
for ch,files in pm.items():
    if not isinstance(files,list): continue
    caps=cm.get(ch) or []
    arr=[]
    for i,f in enumerate(files):
        if not isinstance(f,str): continue
        cap=caps[i] if isinstance(caps,list) and i<len(caps) and isinstance(caps[i],str) else ""
        arr.append({"file":f,"caption":cap})
    if arr: photos[ch]=arr; k+=1
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("photos merged",k)