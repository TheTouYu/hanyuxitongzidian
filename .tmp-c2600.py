# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards")
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷四  弋.docx").paragraphs]
def line(ch):
    for k in range(124,150):
        if ps[k].startswith(ch) or ps[k].startswith(ch+"（"): return ps[k]
    return ""
p=os.path.join(C,"叔.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]!="zizu": continue
    g1,g2,g3=s["groups"][0],s["groups"][1],(s["groups"][2] if len(s["groups"])>2 else None)
    for ch in ("督","惄","錖"):
        if ch not in [r[0] for r in g1["rows"]]:
            g1["rows"].append([ch,"","",line(ch)])
    if g3 is None:
        g3={"title":"③取狀如豆子成熟時光禿的樣子","note":"","rows":[]}
        s["groups"].append(g3)
    for ch in ("𦵦","菽","𤬂","椒"):
        if ch not in [r[0] for r in g3["rows"]]:
            g3["rows"].append([ch,"","",line(ch)])
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 叔族字卡
kids=[("督","dū"),("惄","nì"),("錖","dú"),("𦵦","dí"),("菽","shū"),("𤬂","dǔ"),("椒","jiāo")]
made=0
for ch,py_ in kids:
    f=os.path.join(C,ch+".json")
    if os.path.exists(f): continue
    txt=line(ch)
    card={"char":ch,"head":ch,"pinyin":py_,"level":3,"parent":"叔","bus":[{"num":26,"name":"弋"}],
      "sections":[{"key":"shiyi","label":"释义","text":txt,"cites":[]},
       {"key":"shengmu","label":"声母拟态","text":py_[0]+"「—」：待定","cites":[]},
       {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
    json.dump(card,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); made+=1
print("rows",sum(len(g["rows"]) for s in d["sections"] if s["key"]=="zizu" for g in s["groups"]),"new",made)