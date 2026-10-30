# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
PREFIX=re.compile(r"^(本義|本义|轉義|转义|辯證|辩证|音源|字族衍義)[：:]")
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    ch=d.get("char")
    if ch not in ("禾","科","和","龢","鉌","訸","惒","啝","柇","姀","盉","䒩","蝌","犐","䈖","萪"): continue
    ch2=False
    for s in d.get("sections",[]):
        t=s.get("text") or ""
        t2=PREFIX.sub("",t,count=1)
        if t2!=t: s["text"]=t2; ch2=True
    if ch2: json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("stripped",n)
doc=Document(r"D:\字谱智能体\卷六  鶴.docx")
for k in (363,364,365):
    c=sum(1 for el in doc.paragraphs[k]._p.iter() if el.tag.split("}")[-1]=="blip")
    print(k,c,doc.paragraphs[k].text.strip()[:30])