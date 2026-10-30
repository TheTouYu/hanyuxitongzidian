# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
from PIL import Image
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
imgs=[]
for el in doc.paragraphs[102]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob
            f=io.BytesIO(b); 
            try: imgs.append(Image.open(f).convert("RGBA"))
            except Exception: pass
print("imgs",len(imgs),[i.size for i in imgs])
W=sum(i.width for i in imgs)+20*(len(imgs)+1); H=max(i.height for i in imgs)+20
canvas=Image.new("RGBA",(W,H),(255,255,255,255)); x=20
for i in imgs:
    canvas.paste(i,(x,10),i if i.mode=="RGBA" else None); x+=i.width+20
D=os.path.join(G,"rows"); os.makedirs(D,exist_ok=True)
out=os.path.join(D,"兮.png"); canvas.convert("RGB").save(out,optimize=True)
print("saved",out,canvas.size)
p=os.path.join(C,"兮.json"); d=json.load(io.open(p,encoding="utf-8"))
secs=[s for s in d["sections"] if s.get("key")!="cankao"]
sec={"key":"cankao","label":"参考","text":"","gimgs":["rows/兮.png"],"cites":[]}
d["sections"]=[sec]+secs
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("sec ok")