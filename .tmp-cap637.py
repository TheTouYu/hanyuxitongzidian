# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})(（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)")
def strip(t):
    for q in ("本義：","轉義：","辯證：","音源："):
        if t.startswith(q): return t[len(q):].lstrip()
    return t
g=[("①指柔順、羸弱",[]),("②指遮蔽、隱藏",[])]
cur=None
for k in range(142,163):
    t=ps[k]
    if not t: continue
    if t.startswith("①"): cur=0; continue
    if t.startswith("②"): cur=1; continue
    if t.startswith("▲"): continue
    m=pat.match(t)
    if not m or cur is None: continue
    lei=(re.search(r"从([一-龥])",t).group(1) if re.search(r"从([一-龥])",t) else "")
    g[cur][1].append([m.group(1),m.group(4),lei,t])
print([len(x[1]) for x in g])
VOL={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}
SH={"key":"shangji","label":"上级字根","text":"一级字根：矢；本字医为矢部二级字根。","cites":[],
    "links":[{"ch":"矢","label":"矢（一级）"}]}
z={"char":"医","head":"医（𠣗）","pinyin":"yì","level":2,"parent":"矢","bus":[{"num":16,"name":"矢"}],"rootLevel":2,
 "sections":[{"key":"benyi","label":"本义","text":strip(ps[139]),"cites":[]},
  {"key":"zhuanyi","label":"转义","text":strip(ps[141]),"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"y 為零聲母一系，緒論七組未列，不系（照實）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"原文字族衍義分兩組：","cites":[],
   "groups":[{"title":t,"note":"","rows":rows} for t,rows in g]},SH,VOL],"aliases":[]}
json.dump(z,io.open(os.path.join(C,"医.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
n=0
for t,rows in g:
    for ch,py_,lei,txt in rows:
        d={"char":ch,"head":ch,"pinyin":py_,"level":3,"parent":"医","bus":[{"num":16,"name":"矢"}],
           "sections":[{"key":"shiyi","label":"释义","text":txt,"cites":[]},
             {"key":"shengmu","label":"声母拟态","text":"y 為零聲母一系，緒論七組未列，不系（照實）。","cites":[]},VOL],"aliases":[]}
        json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("子卡",n)