# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
blobs=[]
for el in doc.paragraphs[58]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid: blobs.append(parts[rid[0]].blob)
print("total",len(blobs))
def write(ch,bs):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    fs=[]
    for i,b in enumerate(bs,1):
        ext="png" if b[:4]==b"\x89PNG" else "jpg"
        fn="%02d.%s"%(i,ext); open(os.path.join(d,fn),"wb").write(b); fs.append(ch+"/"+fn)
    return fs
f1=write("虍",blobs[:6]); f2=write("虎",blobs[6:])
ip=os.path.join(G,"index.json"); x=json.load(io.open(ip,encoding="utf-8"))
x["虍"]={"doc":"卷八 虎","files":f1}; x["虎"]={"doc":"卷八 虎","files":f2}
json.dump(x,io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
print("虍",len(f1),"虎",len(f2))