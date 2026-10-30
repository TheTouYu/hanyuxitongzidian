# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
for el in doc.paragraphs[446]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob; d=os.path.join(P,"羲"); os.makedirs(d,exist_ok=True)
            for f in os.listdir(d): os.remove(os.path.join(d,f))
            ext="png" if b[:4]==b"\x89PNG" else "jpg"; open(os.path.join(d,"01."+ext),"wb").write(b)
            for name,key,val in (("index.json","photos",["01."+ext]),("captions.json","captions",["（原稿此圖無▲圖注）"])):
                p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); m=x.get(key) or x
                m["羲"]=val; json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
            print("ok",len(b),ext); break