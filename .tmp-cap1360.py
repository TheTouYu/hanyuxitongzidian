# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
bad=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8")); ch=d.get("char")
    for s in d.get("sections",[]):
        t=s.get("text","")
        for m in re.finditer(r'glyphs/([^/"]+)/(\d+\.(?:png|jpg|jpeg))',t):
            p=os.path.join(G,m.group(1),m.group(2))
            if not os.path.exists(p): bad.append((ch,m.group(1),m.group(2)))
print("坏图引用",len(bad))
for b in bad[:12]: print(b)