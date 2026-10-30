# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
P=r"D:\系统汉字\web\public\glyphs\photos"
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
for k,ch,c in ((157,"醫","古代的針灸醫療包"),(164,"翳","《出警圖》中的華蓋（明）")):
    rid=None
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if (a.endswith("}embed") or a.endswith("}id")):
                try:
                    if len(parts[v].blob)>8000: rid=v
                except KeyError: pass
    if not rid: print("noimg",ch); continue
    b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    D=os.path.join(P,ch); os.makedirs(D,exist_ok=True)
    fn="01"+ext; open(os.path.join(D,fn),"wb").write(b)
    ph[ch]=[fn]; cm[ch]=[c]
    print(ch,fn,len(b))
json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)