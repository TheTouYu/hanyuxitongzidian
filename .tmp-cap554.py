# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
P=r"D:\系统汉字\web\public\glyphs\photos"
owner=None
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})")
for k in range(760,772):
    t=ps[k].text.strip(); m=pat.match(t)
    if m and not t.startswith("▲"): owner=m.group(1)
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if (a.endswith("}embed") or a.endswith("}id")) and v in parts:
                b=parts[v].blob
                if len(b)>8000 and owner:
                    ext=".png" if b[:4]==b"\x89PNG" else (".emf" if b[:4]==b"\x01\x00\x00\x00" else ".jpg")
                    dst=os.path.join(P,owner); os.makedirs(dst,exist_ok=True)
                    open(os.path.join(dst,"01"+ext),"wb").write(b)
                    ix=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=ix.get("photos") or ix
                    ph[owner]=["01"+ext]
                    cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
                    for j in range(k+1,k+3):
                        nt=ps[j].text.strip()
                        if nt.startswith("▲"): cm[owner]=[nt[1:].strip()]; break
                    json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
                    json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
                    print("图->",owner,ext,len(b),cm.get(owner))