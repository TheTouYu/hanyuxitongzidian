# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
V=json.load(io.open(C+r"\variants.json",encoding="utf-8"))
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
def pick(a,b):
    out=[]
    for k in range(a,b+1):
        t=ps[k]
        if not t or t[0] in "①②③字音轉本辯" or t.startswith("▲"): continue
        out.append((k,t))
    return out
r1=pick(685,705); r2=pick(707,729)
print(len(r1),len(r2))
def head(t):
    m=re.match(r"^([^\s（(《]{1,2})（?[^）]*?）?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü,，、]+)",t)
    return (m.group(1),m.group(2)) if m else (t[:1],"")
def lei(t):
    m=re.search(r"从([一-龥])",t)
    return m.group(1) if m else ""
def row(k,t):
    ch,py=head(t); return [ch,py,lei(t),t]
g1=[row(k,t) for k,t in r1]; g2=[row(k,t) for k,t in r2]
def S(k,l,t,links=None):
    s={"key":k,"label":l,"text":t,"cites":[]}
    if links: s["links"]=links
    return s
JUAN={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷二㠯","label":"卷二 㠯"}]}
zhi={"char":"支","head":"支（𠦙𡽒𣏃𢺶）","pinyin":"zhī","level":1,"parent":"","bus":[{"num":13,"name":"支"}],
 "sections":[S("benyi","本义",ps[677]),
  S("zhuanyi","转义",ps[678]+ps[679]+ps[680]+ps[681]),
  S("yinyuan","音源",ps[682]),
  S("shengmu","声母拟态","zh「凿总」取「凿」：折竹為枝，斷口如鑿之切（推）。"),
  {"key":"zizu","label":"字族衍义","text":"原文字族衍義兩組：","cites":[],
   "groups":[{"title":"①指分支，表示分散、伸出","note":"","rows":g1},
             {"title":"②指支撐，表示舉起、懸挂、不正","note":"","rows":g2}]},
  JUAN]}
json.dump(zhi,io.open(rf"{C}\支.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
inv={}
for s,ts in V.items():
    for t in ts: inv.setdefault(t,[]).append(s)
n=0
for ch,py,le,txt in g1+g2:
    base=re.sub(r"（.*?）","",ch)
    sm=S("shengmu","声母拟态","零聲母（今讀 %s），绪论七组未列，不系（照實）。"%py if py and py[0] in "yw" else "%s：取绪论拟态义一面（推）。"%((py or "zh")[0]))
    d={"char":base,"head":ch,"pinyin":py,"level":3,"parent":"支","bus":[{"num":13,"name":"支"}],
       "sections":[S("shiyi","释义",txt),sm,JUAN]}
    ss=inv.get(base)
    if ss: d["simp"]=ss[0]; d["aliases"]=ss
    json.dump(d,io.open(os.path.join(C,base+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("支部成卡",n+1)