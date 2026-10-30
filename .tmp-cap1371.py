# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
bad={}
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8")); ch=d.get("char")
    for s in d.get("sections",[]):
        for m in re.finditer(r'glyphs/([^"\s]+\.(?:png|jpg|jpeg))',s.get("text","")):
            rel=m.group(1)
            if not os.path.exists(os.path.join(G,rel)): bad.setdefault(ch,[]).append(rel)
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")).get("chars") or {}
for ch,v in idx.items():
    for f in (v.get("files") or []):
        if not os.path.exists(os.path.join(G,f)): bad.setdefault(ch,[]).append(f)
print("仍有坏引用卡数",len(bad))
for k,v in list(bad.items())[:5]: print(k,len(v),v[:3])