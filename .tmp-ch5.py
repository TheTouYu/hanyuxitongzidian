# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
rows=json.load(io.open(r"D:\系统汉字\.tmp-changrows.json",encoding="utf-8"))
os.remove(os.path.join(C,"鴈（雁）.json"))
ZERO="y「零聲母」不系：零聲母，緒論七組未列（照實）。"
d={"char":"鴈","head":"鴈（雁）","pinyin":"yàn","level":3,"parent":"厂","bus":["35"],"aliases":["雁"],
   "sections":[{"key":"shiyi","label":"释义","text":rows["243"]},{"key":"shengmu","label":"声母拟态","text":ZERO}]}
json.dump(d,io.open(os.path.join(C,"鴈.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# photos
from docx import Document
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
def first_img(k,minlen=3000):
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                b=parts[rid[0]].blob
                if len(b)>=minlen: return b
    return None
def kd(b): return "png" if b[:4]==b"\x89PNG" else ("jpg" if b[:2]==b"\xff\xd8" else "bin")
ix=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); pm=ix.get("photos") or ix
cp=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cp.get("captions") or cp
for ch,k,cap in (("厂",215,"北京延慶古崖居"),("鴈",223,"「人」字形雁陣")):
    b=first_img(k)
    if not b: print("no img",ch); continue
    d2=os.path.join(P,ch); os.makedirs(d2,exist_ok=True)
    for f in os.listdir(d2): os.remove(os.path.join(d2,f))
    fn="01."+kd(b); open(os.path.join(d2,fn),"wb").write(b)
    pm[ch]=[fn]; cm[ch]=[cap]; print("img",ch,fn,len(b))
json.dump({"photos":pm},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)