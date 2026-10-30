# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
bad=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8")); ch=d.get("char")
    refs=set()
    for s in d.get("sections",[]):
        for m in re.finditer(r'glyphs/([^"\s]+?)/(\d+\.(?:png|jpg|jpeg))',s.get("text","")):
            refs.add((m.group(1),m.group(2)))
    miss=[r for r in refs if not os.path.exists(os.path.join(G,r[0],r[1]))]
    if miss: bad.append((ch,len(miss),sorted(miss)[:3]))
print(len(bad))
for b in bad[:10]: print(b[0],b[1],b[2])