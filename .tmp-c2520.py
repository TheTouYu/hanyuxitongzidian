# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
# 1) 叔 插图（p121 rId78）
b=parts["rId78"].blob
ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
D=os.path.join(ROOT,"web","public","glyphs","photos","叔"); os.makedirs(D,exist_ok=True)
for f in os.listdir(D): os.remove(os.path.join(D,f))
fn="01"+ext; open(os.path.join(D,fn),"wb").write(b)
P=os.path.join(ROOT,"web","public","glyphs","photos")
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
ph["叔"]=[fn]; json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
# 2) 叔 字族行原文补全
full={}
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,3})(（[^）]*）)?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+")
for k in range(124,142):
    t=ps[k].text.strip(); m=pat.match(t)
    if m: full[m.group(1)]=t
C=os.path.join(ROOT,"web","public","cards")
d=json.load(io.open(os.path.join(C,"叔.json"),encoding="utf-8"))
n=0
for s in d["sections"]:
    if s["key"]!="zizu": continue
    for g in s.get("groups",[]):
        for r in g["rows"]:
            ch=r[0].split("（")[0]
            if ch in full: r[3]=full[ch]; n+=1
d["photos"]=[fn]; d["captions"]=[]
json.dump(d,io.open(os.path.join(C,"叔.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("叔图",fn,len(b),"行补全",n,"/",sum(len(g["rows"]) for s in d["sections"] if s["key"]=="zizu" for g in s.get("groups",[])))