# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
P=r"D:\系统汉字\web\public\glyphs\photos"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); parts=doc.part.related_parts
rid=None
for el in doc.paragraphs[321]._p.iter():
    for a,v in el.attrib.items():
        if (a.endswith("}embed") or a.endswith("}id")) and v in parts:
            if len(parts[v].blob)>20000: rid=v
b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
D=os.path.join(P,"朿"); os.makedirs(D,exist_ok=True)
fn="01"+ext; open(os.path.join(D,fn),"wb").write(b)
for name,key,val in (("index.json","photos",[fn]),("captions.json","captions",["皂角刺"])):
    p=os.path.join(P,name); j=json.load(io.open(p,encoding="utf-8")); j[key]["朿"]=val
    json.dump(j,io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
cp=os.path.join(C,"朿.json"); cd=json.load(io.open(cp,encoding="utf-8"))
cd["photos"]=[fn]; cd["captions"]=["皂角刺"]
json.dump(cd,io.open(cp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("朿",fn,len(b))