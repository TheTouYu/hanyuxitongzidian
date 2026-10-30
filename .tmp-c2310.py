# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
P=r"D:\系统汉字\web\public\glyphs\photos"
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
b=parts["rId60"].blob
ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
D=os.path.join(P,"尗"); os.makedirs(D,exist_ok=True)
for f in os.listdir(D): os.remove(os.path.join(D,f))
fn="01"+ext; open(os.path.join(D,fn),"wb").write(b)
cap=""
for k in (118,119):
    t=ps[k].text.strip()
    if t.startswith("▲"): cap=t[1:].strip()
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
ph["尗"]=[fn]; json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(C+r"\尗.json",encoding="utf-8"))
d["photos"]=[fn]; d["captions"]=[cap] if cap else []
for s in d["sections"]:
    if s["key"]=="shengmu":
        s["text"]="sh「失收」取「收」：弋獲小物而收之（推）。"
json.dump(d,io.open(C+r"\尗.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("尗 图",fn,len(b),"cap",cap)