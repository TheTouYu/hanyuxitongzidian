# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷六  鶴.docx"); parts=doc.part.related_parts
def imgs(k):
    out=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                try: out.append(parts[rid[0]].blob)
                except KeyError: pass
    return out
def save(ch,blobs):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d):
        if f.endswith((".png",".jpg")): os.remove(os.path.join(d,f))
    files=[]
    for i,b in enumerate(blobs,1):
        ext="png" if b[:4]==b"\x89PNG" else "jpg"
        n="%02d.%s"%(i,ext); open(os.path.join(d,n),"wb").write(b); files.append(ch+"/"+n)
    return files
b31=imgs(31); b30=imgs(30)
f_hu=save("隺",b31[:3]); f_ma=save("䮤",b31[3:4]) if len(b31)>3 else []
f_huo=save("靃",b30)
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=ix["chars"]
ch["隺"]={"doc":"卷六 鶴","variants":[],"files":f_hu,"photos":["01.jpg"]}
if f_ma: ch["䮤"]={"doc":"卷六 鶴","variants":[],"files":f_ma}
ch["靃"]={"doc":"卷六 鶴","variants":[],"files":f_huo}
json.dump({"chars":ch},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("隺",len(f_hu),"䮤",len(f_ma),"靃",len(f_huo))