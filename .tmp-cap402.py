# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
P=r"D:\系统汉字\web\public\glyphs\photos"
want={635:("𦣞","陝西藍田人牙床骨化石（115萬年前）"),647:("𣐵","戽斗"),652:("䇫","秦代漆繪梳、篦（左）")}
def imgs(p):
    out=[]
    for el in p._p.iter():
        for a,v in el.attrib.items():
            if a.endswith('}embed') or a.endswith('}id'):
                try:
                    pt=parts[v]
                    if hasattr(pt,'blob') and len(pt.blob)>8000: out.append(v)
                except KeyError: pass
    return out
ix=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=ix.get("photos") or ix
cp=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8"))["captions"]
for k,(ch,cap) in want.items():
    rl=imgs(ps[k-1])
    if not rl: print("no img",k); continue
    b=parts[rl[0]].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    d=os.path.join(P,ch); os.makedirs(d,exist_ok=True)
    fn="01"+ext; open(os.path.join(d,fn),"wb").write(b)
    ph[ch]=[fn]; cp[ch]=[cap]; print(ch,fn,len(b))
json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
json.dump({"captions":cp},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)