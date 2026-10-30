# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
def kd(b): return "png" if b[:4]==b"\x89PNG" else ("emf" if b[:4]==b"\x01\x00\x00\x00" else ("jpg" if b[:2]==b"\xff\xd8" else "bin"))
# glyphs p58
d=os.path.join(G,"虍"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
files=[];n=0
for el in doc.paragraphs[58]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob
            if len(b)>=1200:
                n+=1; fn="%02d.%s"%(n,kd(b)); open(os.path.join(d,fn),"wb").write(b); files.append("虍/"+fn)
print("glyphs",len(files))
# photos
P=os.path.join(G,"photos"); pp=os.path.join(P,"虍"); os.makedirs(pp,exist_ok=True)
for f in os.listdir(pp): os.remove(os.path.join(pp,f))
def grab(k,name):
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                b=parts[rid[0]].blob; open(os.path.join(pp,name),'wb').write(b); return True
    return False
ph=[]
if grab(60,"01.png"): ph.append("01.png")
if grab(95,"02.png"): ph.append("02.png")
print("photos",ph)
# index
ip=os.path.join(G,"index.json"); x=json.load(io.open(ip,encoding="utf-8"))
try: gi=x["glyphs"]
except KeyError: gi=x.setdefault("index",{})
gi["虍"]={"files":files}
json.dump(x,io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
pic=os.path.join(P,"index.json"); y=json.load(io.open(pic,encoding="utf-8"))
mm=y.get("photos") or y; mm["虍"]=ph
json.dump({"photos":mm},io.open(pic,"w",encoding="utf-8"),ensure_ascii=False)
cp=os.path.join(P,"captions.json"); z=json.load(io.open(cp,encoding="utf-8"))
cc=z.get("captions") or z; cc["虍"]=["伏鳥雙尾青銅虎（商）","虎符（戰國）"]
json.dump({"captions":cc},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
print("ok")