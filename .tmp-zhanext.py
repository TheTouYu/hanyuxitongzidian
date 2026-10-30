# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
def blobs(k):
    out=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                try: out.append(parts[rid[0]].blob)
                except KeyError: pass
    return out
# glyphs
d=os.path.join(G,"詹"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d):
    if f.lower().endswith((".png",".jpg")): os.remove(os.path.join(d,f))
files=[]; n=0
for b in blobs(343):
    n+=1; ext="png" if b[:4]==b"\x89PNG" else "jpg"; fn="%02d.%s"%(n,ext)
    open(os.path.join(d,fn),"wb").write(b); files.append("詹/"+fn)
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=ix["chars"]
ch["詹"]={"doc":"卷五  雁.docx","variants":["𦧕"],"files":files}
json.dump({"chars":ch},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
# photos
pdir=os.path.join(G,"photos","詹"); os.makedirs(pdir,exist_ok=True)
for f in os.listdir(pdir): os.remove(os.path.join(pdir,f))
caps=["燕子在屋簷下築巢","有障泥的唐三彩馬","膽囊位置示意圖"]
i=0
for k,cap in zip((348,371,374),caps):
    bs=blobs(k)
    if not bs: print("no img",k); continue
    b=bs[0]; i+=1; ext="png" if b[:4]==b"\x89PNG" else "jpg"
    open(os.path.join(pdir,"%02d.%s"%(i,ext)),"wb").write(b)
pi=os.path.join(G,"photos","index.json"); px=json.load(io.open(pi,encoding="utf-8")); pm=px.get("photos") or px
pm["詹"]=sorted(os.listdir(pdir))
json.dump({"photos":pm},io.open(pi,"w",encoding="utf-8"),ensure_ascii=False)
pc=os.path.join(G,"photos","captions.json"); cx=json.load(io.open(pc,encoding="utf-8")); cmx=cx.get("captions") or cx
cmx["詹"]=caps[:i]
json.dump({"captions":cmx},io.open(pc,"w",encoding="utf-8"),ensure_ascii=False)
print("glyphs",len(files),"photos",i)