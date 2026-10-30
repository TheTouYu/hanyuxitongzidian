# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); ps=[p.text.strip() for p in doc.paragraphs]
benyi="\n".join([ps[90].replace("本義：","",1),ps[91],ps[92]])
zhuanyi="\n".join([ps[93].replace("轉義：","",1),ps[94]])
bian="\n".join([ps[95].replace("辯證：","",1)])
rows=[["掀","xiān","手",ps[97]],["𦜓","xìn","肉",ps[98]],["焮","xìn","火",ps[99]],["惞","xīn","心",ps[100]],["俽","xīn","人",ps[101]]]
card={"char":"欣","head":"欣（訢）","pinyin":"xīn","bus":{"num":44,"name":"斤"},"parent":"斤","level":2,"aliases":["訢"],
 "sections":[{"key":"benyi","label":"本义","text":benyi,"cites":[]},
  {"key":"zhuanyi","label":"转义","text":zhuanyi,"cites":[]},
  {"key":"bianzheng","label":"辩证","text":bian,"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"x「续消」取「续」：心喜而續續然，笑意接連（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","groups":[{"no":"","title":ps[96].replace("字族衍義：","",1),"rows":rows}],"cites":[]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
json.dump(card,io.open(os.path.join(C,"欣.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 字形
parts=doc.part.related_parts; d=os.path.join(G,"欣"); os.makedirs(d,exist_ok=True)
files=[]; i=0
for el in doc.paragraphs[89]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob; i+=1; fn="%02d.%s"%(i,"png" if b[:4]==b"\x89PNG" else "jpg")
            open(os.path.join(d,fn),"wb").write(b); files.append("欣/"+fn)
if files:
    p=os.path.join(G,"index.json"); g=json.load(io.open(p,encoding="utf-8")); g["chars"].setdefault("欣",{})["files"]=files
    json.dump({"chars":g["chars"]},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
for ch,py,lei,tx in rows:
    q=os.path.join(C,ch+".json")
    if os.path.exists(q): continue
    c={"char":ch,"head":ch,"pinyin":py,"bus":{"num":44,"name":"斤"},"parent":"欣","level":3,"aliases":[],
       "sections":[{"key":"shiyi","label":"释义","text":tx,"cites":[]},
                   {"key":"shengmu","label":"声母拟态","text":"x「续消」：聲符取義隨文（推）。","cites":[]},
                   {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷七斤","label":"卷七 斤"}]}]}
    json.dump(c,io.open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("files",len(files))