# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})(（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)")
g1=[];g2=[];g3=[];cur=None
for k in range(48,77):
    t=ps[k]
    if not t: continue
    if t.startswith("①"): cur=g1; continue
    if t.startswith("②"): cur=g2; continue
    if t.startswith("③"): cur=g3; continue
    if t.startswith(("▲","字族")): continue
    m=pat.match(t)
    if not m or cur is None: continue
    ch,par,py=m.group(1),m.group(3) or "",m.group(4)
    lei=(re.search(r"从([一-龥])",t).group(1) if re.search(r"从([一-龥])",t) else "")
    cur.append([ch,py,lei,t])
print("组",len(g1),len(g2),len(g3))
def S(k,l,t,g=None):
    s={"key":k,"label":l,"text":t,"cites":[]}
    if g is not None: s["groups"]=g
    return s
J={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}
def strip(t):
    for q in ("本義：","轉義：","辯證：","音源："):
        if t.startswith(q): return t[len(q):].lstrip()
    return t
z={"char":"矢","head":"矢（𠂕𠓡𥎨𠤕𥬟）","pinyin":"shǐ","level":1,"parent":"","bus":[{"num":16,"name":"矢"}],
 "sections":[S("benyi","本义",strip(ps[38])),
  S("zhuanyi","转义",strip(ps[40])+strip(ps[41])+strip(ps[42])+strip(ps[43])),
  S("bianzheng","辩证",strip(ps[44])),S("yinyuan","音源",strip(ps[45])),
  S("shengmu","声母拟态","sh「失收」取「失」：箭離弦則一去不返，力盡而收（推）。"),
  S("zizu","字族衍义","原文字族衍義分四組：",
    [{"title":"①指箭鏃之狀","note":"","rows":g1},
     {"title":"②指箭杆的細而直","note":"","rows":g2},
     {"title":"③指射箭的過程","note":"","rows":g3[:5]},
     {"title":"④象意字，指箭矢","note":"","rows":g3[5:]}]),
  {"key":"erji","label":"本部二级字根","text":"知、智、疾、医、至、到、臺、彘（各以其本義立卡）","cites":[]},J],
 "aliases":["箭"]}
json.dump(z,io.open(os.path.join(C,"矢.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for r in g1+g2+g3:
    m=re.search(r"（([^）]*)）",r[0])
    d={"char":re.sub(r"（.*?）","",r[0]),"head":r[0],"pinyin":r[1],"level":3,"parent":"矢","bus":[{"num":16,"name":"矢"}],
       "sections":[S("shiyi","释义",r[3]),S("shengmu","声母拟态",f"{r[1][0]}「—」取一面：箭族之字，取矢之形與用（推）。"),J],
       "aliases":list(m.group(1)) if m else []}
    json.dump(d,io.open(os.path.join(C,d["char"]+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("共卡",1+len(g1+g2+g3))