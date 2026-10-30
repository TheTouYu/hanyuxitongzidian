# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); parts=doc.part.related_parts
blobs=[]
for el in doc.paragraphs[286]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid: blobs.append(parts[rid[0]].blob)
print("blobs",len(blobs))
def save(ch,bs):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    names=[]
    for i,b in enumerate(bs,1):
        fn="%02d.png"%i; open(os.path.join(d,fn),"wb").write(b); names.append(fn)
    return names
n1=save("宅",blobs[:9]); n2=save("亳",blobs[9:])
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi["宅"]={"doc":"卷七 斤","files":n1}; gi["亳"]={"doc":"卷七 斤","files":n2}
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
for ch,files in (("宅",n1),("亳",n2)):
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): continue
    d=json.load(io.open(p,encoding="utf-8"))
    if not any(s.get("key")=="zixing" for s in d["sections"]):
        d["sections"].append({"key":"zixing","label":"字形","files":files})
    else:
        for s in d["sections"]:
            if s.get("key")=="zixing": s["files"]=files
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("宅",n1,"亳",n2)