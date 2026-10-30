# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
for ch in ("䖒","慮","虛","盧","虜","虖","虢"):
    d=os.path.join(G,ch)
    if not os.path.isdir(d): continue
    fixed=[]
    for f in sorted(os.listdir(d)):
        p=os.path.join(d,f); b=open(p,"rb").read(8)
        ext="png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else ("emf" if b[:4]==b"\x01\x00\x00\x00" else None))
        if ext is None: os.remove(p); continue
        if not f.endswith("."+ext):
            nf=os.path.splitext(f)[0]+"."+ext; os.replace(p,os.path.join(d,nf)); f=nf
        fixed.append(ch+"/"+f)
    gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
    gi["chars"][ch]={"doc":"卷八 虎","files":fixed}
    json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
    print(ch,len(fixed))