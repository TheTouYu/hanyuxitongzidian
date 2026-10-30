# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
rows=[]
lei={"謝":"言","榭":"木","㓔":"冫","塮":"土","㴬":"水","𧎭":"虫","𧛼":"衣","𩘧":"風","𪋧":"鹿"}
import re
for k in range(727,736):
    t=ps[k]
    m=re.match(r"^([^\s（(（]{1,3})(（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)",t)
    ch=m.group(1); py_=m.group(4)
    rows.append([ch,py_,lei.get(ch,""),t])
p=r"D:\系统汉字\web\public\cards\射.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        s["text"]="字族衍義：多指射箭，表示離、棄、速"
        s["groups"]=[{"title":"","note":"","rows":rows}]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("rows",len(rows))