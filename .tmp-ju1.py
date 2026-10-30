# -*- coding: utf-8 -*-
import json,io,os,shutil,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
def save_glyphs(para,ch,upto=None):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    fs=[];n=0
    for el in doc.paragraphs[para]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                n+=1
                if upto and n>upto: continue
                b=parts[rid[0]].blob; ext="png" if b[:4]==b"\x89PNG" else "jpg"
                fn="%02d.%s"%(n,ext); open(os.path.join(d,fn),"wb").write(b); fs.append(ch+"/"+fn)
    gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
    gi["chars"][ch]={"doc":"卷八 虎","files":fs}; json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
    return len(fs)
nju=save_glyphs(302,"豦",upto=4)
# 遽的 11 形：取 p302 第 5 起
d=os.path.join(G,"遽"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
fs=[];n=0
for el in doc.paragraphs[302]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            n+=1
            if n<=4: continue
            b=parts[rid[0]].blob; ext="png" if b[:4]==b"\x89PNG" else "jpg"
            fn="%02d.%s"%(len(fs)+1,ext); open(os.path.join(d,fn),"wb").write(b); fs.append("遽/"+fn)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi["chars"]["遽"]={"doc":"卷八 虎","files":fs}; json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("豦",nju,"遽",len(fs))