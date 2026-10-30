# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})(（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)")
g1=[];g3=[]
cur=g1
for k in range(47,77):
    t=ps[k]
    if not t: continue
    if t.startswith("①"): cur=g1; continue
    if t.startswith("②"): cur=None; continue
    if t.startswith("③"): cur=g3; continue
    if t.startswith(("▲","字族")): continue
    m=pat.match(t)
    if not m or cur is None: continue
    ch,par,py=m.group(1),m.group(3) or "",m.group(4)
    lei=(re.search(r"从([一-龥])",t).group(1) if re.search(r"从([一-龥])",t) else "")
    cur.append([ch,py,lei,t])
print("g1",len(g1),"g3",len(g3))
z=json.load(io.open(os.path.join(C,"矢.json"),encoding="utf-8"))
grp=[s for s in z["sections"] if s.get("key")=="zizu"][0]["groups"]
grp[0]["rows"]=g1; grp[2]["rows"]=g3[:5]; grp[3]["rows"]=g3[5:]
json.dump(z,io.open(os.path.join(C,"矢.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for r in g1+g3:
    ch=re.sub(r"（.*?）","",r[0]); m=re.search(r"（([^）]*)）",r[0])
    p=os.path.join(C,ch+".json")
    if os.path.exists(p): continue
    d={"char":ch,"head":r[0],"pinyin":r[1],"level":3,"parent":"矢","bus":[{"num":16,"name":"矢"}],
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
                   {"key":"shengmu","label":"声母拟态","text":f"{r[1][0]}「—」取一面：箭族之字，取矢之形與用（推）。","cites":[]},
                   {"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}],
       "aliases":list(m.group(1)) if m else []}
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("组行",[len(x["rows"]) for x in grp])