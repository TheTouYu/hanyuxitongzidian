# -*- coding: utf-8 -*-
import json,io,os,sys,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
# 庶
d=os.path.join(P,"庶")
for f in os.listdir(d):
    if f!="250_01.png": os.remove(os.path.join(d,f))
os.replace(os.path.join(d,"250_01.png"), os.path.join(d,"01.png"))
# 鷓
d2=os.path.join(P,"鷓"); os.makedirs(d2,exist_ok=True)
for f in os.listdir(d2): os.remove(os.path.join(d2,f))
shutil.move(os.path.join(P,"庶","277_01.jpg") if os.path.exists(os.path.join(P,"庶","277_01.jpg")) else "", os.path.join(d2,"01.jpg")) if False else None
# 277_01 已被删，改从原始重新取
from docx import Document
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); parts=doc.part.related_parts
for el in doc.paragraphs[277]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid: open(os.path.join(d2,"01.jpg"),"wb").write(parts[rid[0]].blob); break
ip=os.path.join(P,"index.json"); x=json.load(io.open(ip,encoding="utf-8")); m=x["photos"]
m["庶"]=["01.png"]; m["鷓"]=["01.jpg"]
json.dump({"photos":m},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
cp=os.path.join(P,"captions.json"); y=json.load(io.open(cp,encoding="utf-8")); c=y["captions"]
c["庶"]=["燒紅的石頭"]; c["鷓"]=["鷓鴣"]
json.dump({"captions":c},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
print("ok",os.listdir(P+"/庶"),os.listdir(P+"/鷓"))