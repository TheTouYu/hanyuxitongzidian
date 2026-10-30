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
beny=strip(ps[77+1])  # p78
zhuanyi="".join(strip(ps[k]) for k in range(80,85) if ps[k] and not ps[k].startswith(("▲","字族")))
groups=[("①指報靶，表示來回、反復",[]),("②指靶中矢狀，表示多毛",[]),("③形近字「夭」之訛",[])]
cur=None
for k in range(85,109):
    t=ps[k]
    if not t: continue
    if t.startswith("①"): cur=0; continue
    if t.startswith("②"): cur=1; continue
    if t.startswith("③"): cur=2; continue
    if t.startswith(("▲","字族")): continue
    m=pat.match(t)
    if not m or cur is None: continue
    lei=(re.search(r"从([一-龥])",t).group(1) if re.search(r"从([一-龥])",t) else "")
    groups[cur][1].append([m.group(1),m.group(4),lei,t])
print([len(g[1]) for g in groups])
J={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}
z={"char":"知","head":"知（𢇻𥎵𥎿）","pinyin":"zhī","level":2,"parent":"矢","bus":[{"num":16,"name":"矢"}],
 "sections":[{"key":"benyi","label":"本义","text":beny,"cites":[]},
  {"key":"zhuanyi","label":"转义","text":zhuanyi,"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"zh「凿总」取「凿」：報靶之聲直鑿而出，一鑿而中的（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"原文字族衍義分三組：","cites":[],
   "groups":[{"title":g[0],"note":"","rows":g[1]} for g in groups]},
  {"key":"erji","label":"本部二级字根","text":"矢（本体）；知为本部二级字根，其下 ①報靶往返 ②靶中矢狀多毛 ③形近讹字","cites":[]},J],
 "aliases":["智"]}
json.dump(z,io.open(os.path.join(C,"知.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
n=0
for g in groups:
    for r in g[1]:
        ch=r[0]; m=re.search(r"（([^）]*)）",ch)
        d={"char":re.sub(r"（.*?）","",ch),"head":ch,"pinyin":r[1],"level":3,"parent":"知","bus":[{"num":16,"name":"矢"}],
           "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
             {"key":"shengmu","label":"声母拟态","text":f"{r[1][0]}「—」取一面：報靶往返之義，依其物性定面（推）。","cites":[]},J],
           "aliases":list(m.group(1)) if m else []}
        json.dump(d,io.open(os.path.join(C,d["char"]+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("子卡",n)