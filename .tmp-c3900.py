# -*- coding: utf-8 -*-
import json,io,re,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷四  弋.docx").paragraphs]
i=190
secs={"benyi":[], "zhuanyi":[], "bianzheng":[], "yinyuan":[], "shengmu":[], "zizu":[]}
cur=None
groups=[]
for k in range(191,262):
    t=ps[k]
    if not t: continue
    if t.startswith("本義："): cur="benyi"; secs[cur].append(t[3:]); continue
    if t.startswith("轉義："): cur="zhuanyi"; secs[cur].append(t[3:]); continue
    if t.startswith("辯證："): cur="bianzheng"; secs[cur].append(t[4:]); continue
    if t.startswith("音源"): cur="yinyuan"; secs[cur].append(re.sub(r"^音源[：:]?","",t)); continue
    if t.startswith("字族衍義"): cur="zizu"; continue
    if re.match(r"^[①②③④⑤⑥⑦⑧⑨]",t): cur="zizu"; groups.append({"title":t,"note":"","rows":[]}); continue
    if cur=="zizu" and groups:
        m=re.match(r"^([^\s（(]{1,3})(（[^）]*）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)",t)
        if m:
            cat=""
            mm=re.search(r"从([^\s，。；]{1,2})",t)
            if mm: cat=mm.group(1)
            groups[-1]["rows"].append([m.group(1)+ (m.group(2) or ""), m.group(3), cat, t])
    elif cur: secs[cur].append(t)
def txt(k): return "\n".join(secs[k]).strip()
d={"char":"夷","head":"夷（𡗝𡰥𡖴𢎯）","pinyin":"yí","level":1,"bus":[{"num":27,"name":"夷"}],
 "sections":[
  {"key":"benyi","label":"本义","text":txt("benyi"),"cites":[]},
  {"key":"zhuanyi","label":"转义","text":txt("zhuanyi"),"cites":[]},
  {"key":"bianzheng","label":"辩证","text":txt("bianzheng") or "（原文此部无辩證段）","cites":[]},
  {"key":"yinyuan","label":"音源","text":txt("yinyuan") or "（原文此部无音源段）","cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"","groups":groups},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
json.dump(d,io.open(r"D:\系统汉字\web\public\cards\夷.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("组",len(groups),"行",sum(len(g["rows"]) for g in groups))