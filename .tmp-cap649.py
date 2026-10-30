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
groups=[("①指抵達、來到",[]),("②指礙止、堵塞、閉塞",[]),("③指尖利",[])]
cur=None
for k in range(172,225):
    t=ps[k]
    if not t: continue
    if t.startswith("①"): cur=0; continue
    if t.startswith("②"): cur=1; continue
    if t.startswith("③"): cur=2; continue
    if t.startswith("▲"): continue
    m=pat.match(t)
    if not m or cur is None: continue
    lei=(re.search(r"从([一-龥])",t).group(1) if re.search(r"从([一-龥])",t) else "")
    groups[cur][1].append([m.group(1),m.group(4),lei,t])
print([len(g[1]) for g in groups])
VOL={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}
z={"char":"至","head":"至（𦤳𡉰𦤴𡊏𦤵）","pinyin":"zhì","level":2,"parent":"矢","bus":[{"num":16,"name":"矢"}],"rootLevel":2,
 "sections":[{"key":"benyi","label":"本义","text":strip(ps[166]),"cites":[]},
  {"key":"zhuanyi","label":"转义","text":strip(ps[167])+strip(ps[168]),"cites":[]},
  {"key":"bianzheng","label":"辩证","text":strip(ps[169]),"cites":[]},
  {"key":"yinyuan","label":"音源","text":strip(ps[170]),"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"zh「凿总」取「凿」：箭至而鑿入其的，止於所止（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"原文字族衍義分三組：","cites":[],
   "groups":[{"title":t,"note":"","rows":rows} for t,rows in groups]},VOL],"aliases":[]}
json.dump(z,io.open(os.path.join(C,"至.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("至卡建，行",sum(len(g[1]) for g in groups))