# -*- coding: utf-8 -*-
import json,io,os,sys,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
def img(k):
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: return parts[rid[0]].blob
    return None
for ch,k,cap in (("義",424,"牛首形杆飾（商）"),("羲",453,"羊首勺（商）")):
    b=img(k); d=os.path.join(P,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    ext="png" if b[:4]==b"\x89PNG" else "jpg"; open(os.path.join(d,"01."+ext),"wb").write(b)
    for name,key,val in (("index.json","photos",["01."+ext]),("captions.json","captions",[cap])):
        p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
        m[ch]=val; json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("photos ok")