# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
P=r"D:\系统汉字\web\public\glyphs\photos"
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); parts=doc.part.related_parts
# 1) 删睪 误挂
if os.path.isdir(os.path.join(P,"睪")): shutil.rmtree(os.path.join(P,"睪"))
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx["photos"]
ph.pop("睪",None)
cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap["captions"]
cm.pop("睪",None)
# 2) 三张族字图
for ch,rid in (("凙","rId475"),("蠌","rId476"),("檡","rId477")):
    b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    D=os.path.join(P,ch); os.makedirs(D,exist_ok=True)
    fn="01"+ext; open(os.path.join(D,fn),"wb").write(b); ph[ch]=[fn]
    print(ch,fn,len(b))
json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
# 3) 睪 卡去 photos
p=os.path.join(r"D:\系统汉字\web\public\cards","睪.json"); d=json.load(io.open(p,encoding="utf-8"))
d.pop("photos",None); d.pop("captions",None)
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")