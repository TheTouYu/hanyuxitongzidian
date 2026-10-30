# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷七  斤.docx"); ps=[p.text.strip() for p in doc.paragraphs]
CJK=r"\u3400-\u9fff\U00020000-\U0002A6DF"
rowsre=re.compile(r"^(["+CJK+r"]+)(?:（([^）]*)）)?\s*([a-zA-Züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ、，\s]*?)(?=《|：|$)")
groups=[("①指石頭的相關用途",123,129),("②指用石砍砸、投擲",129,138),("③指石頭的硬",138,143),("④指石之大",143,147)]
d=json.load(io.open(os.path.join(C,"石.json"),encoding="utf-8"))
z=d["sections"][4]["groups"]; newgroups=[]; made=0
for (title,a,b),g in zip(groups,z):
    rr=[]
    for k in range(a,b):
        t=ps[k]
        if not t or t[0] in "①②③④": continue
        m=rowsre.match(t)
        if not m: print("SKIP",k,t[:30]); continue
        ch=m.group(1); py=(m.group(3) or "").strip(" 、，")
        rr.append([ch,py,"",t]); made+=1
    g["rows"]=rr; newgroups.append(g)
d["sections"][4]["groups"]=newgroups
json.dump(d,io.open(os.path.join(C,"石.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("rows",made,[(g["title"][:6],len(g["rows"])) for g in newgroups])
# 删旧错名卡
for f in os.listdir(C):
    if not f.endswith(".json"): continue
    ch=f[:-5]
    if ch in ("石","index","variants"): continue
    dd=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    if isinstance(dd,dict) and dd.get("parent")=="石" and re.search(r"[a-zA-Z]",ch):
        os.remove(os.path.join(C,f)); print("del",f)