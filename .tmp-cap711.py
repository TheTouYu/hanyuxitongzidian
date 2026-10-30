# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
doc=Document(r"D:\字谱智能体\卷三  矢.docx"); parts=doc.part.related_parts
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
# 到字形 6 形
D=os.path.join(G,"到"); os.makedirs(D,exist_ok=True)
for f in os.listdir(D): os.remove(os.path.join(D,f))
names=[]
for i,rid in enumerate(["rId103","rId104","rId105","rId106","rId107","rId108"],1):
    b=parts[rid].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
    fn=f"{i:02d}{ext}"; open(os.path.join(D,fn),"wb").write(b); names.append("到/"+fn)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
chars=gi.get("chars") or gi
chars["到"]={"doc":"卷三 矢","files":names,"variants":[]}
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("到字形",len(names))
# 刺榆图归荎（荎藸即刺榆，图注▲刺榆）
b=parts["rId102"].blob; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
DD=os.path.join(P,"荎"); os.makedirs(DD,exist_ok=True)
for f in os.listdir(DD): os.remove(os.path.join(DD,f))
fn="01"+ext; open(os.path.join(DD,fn),"wb").write(b)
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
ph["荎"]=[fn]; json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
cm["荎"]=["刺榆"]; json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("荎插图 刺榆")