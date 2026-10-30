# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
V=json.load(io.open(C+r"\variants.json",encoding="utf-8")); inv={}
for s,ts in V.items():
    for t in ts: inv.setdefault(t,[]).append(s)
# 1) 删除坏卡（字含拼音字母）
killed=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    ch=fn[:-5]
    if re.search(r"[a-zA-Z]",ch):
        os.remove(os.path.join(C,fn)); killed+=1
print("删除坏卡",killed)
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})(（[^）]*）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)")
rows=[];py_map={}
for k in range(685,730):
    t=ps[k]
    if not t or t[0] in "①②③" or t.startswith(("字族","音源","本義","轉義","辯證","▲")): continue
    m=pat.match(t)
    if not m: continue
    ch,par,pinyin=m.group(1),m.group(2),m.group(3)
    lei=(re.search(r"从([一-龥])",t) or [None,""])[1] if re.search(r"从([一-龥])",t) else ""
    rows.append([ch,pinyin,lei,t]); py_map[ch]=(par,pinyin)
def S(k,l,t,links=None):
    s={"key":k,"label":l,"text":t,"cites":[]}
    if links: s["links"]=links
    return s
JUAN={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷二㠯","label":"卷二 㠯"}]}
g1=rows[:20]; g2=rows[20:]
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
n=0
for ch,pinyin,lei,txt in rows:
    par=py_map[ch][0]
    al=set()
    if par: al.update(par.strip("（）"))
    if ch in inv: al.update(inv[ch])
    d={"char":ch,"head":ch+(par or ""),"pinyin":pinyin,"level":3,"parent":"支","bus":[{"num":13,"name":"支"}],
       "sections":[S("shiyi","释义",txt),
                   S("shengmu","声母拟态",f"{pinyin[0]}：取绪论拟态义一面（推）。"),
                   JUAN],
       "aliases":sorted(a for a in al if a and a!=ch)}
    if ch in inv: d["simp"]=inv[ch][0]
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("重建卡",n+1,"行数",len(rows))