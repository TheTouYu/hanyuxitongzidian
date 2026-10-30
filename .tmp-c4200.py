# -*- coding: utf-8 -*-
import json,io,sys,os,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷四  弋.docx").paragraphs]
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(C+r"\夷.json",encoding="utf-8"))
rows={}
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            for r in g["rows"]: rows[r[0].split("（")[0]]=r
# 补漏 𢓡
if "𢓡" not in rows:
    line=""
    for k in range(191,262):
        if ps[k].startswith("𢓡"): line=ps[k]; break
    cat=""; m=re.search(r"从([\u3400-\u9fff])",line)
    if m: cat=m.group(1)
    mm=re.match(r"^([\u3400-\u9fff]{1,3})(（[^）]*）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùü]+)",line)
    row=[mm.group(1)+(mm.group(2) or ""),mm.group(3),cat,line]
    for s in d["sections"]:
        if s["key"]=="zizu": s["groups"][2]["rows"].append(row)
    rows["𢓡"]=row
    json.dump(d,io.open(C+r"\夷.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
SM={"姨":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","蛦":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","咦":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","痍":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","恞":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","跠":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","䧅":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","羠":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","侇":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","桋":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","眱":"y「零聲母」不系：零聲母，緒論七組未列（照實）。",
"荑":"t「涂突」取「突」：茅芽破土而突（推）。","洟":"t「涂突」取「涂」：涕液塗面（推）。","鴺":"t「涂突」取「突」：鵜入水突捕魚（推）。","鮧":"t「涂突」取「涂」：鮎體滑塗（推）。","銕":"t「涂突」取「涂」：黑金鎔而塗範（推）。"}
made=0
for ch,row in rows.items():
    f=os.path.join(C,ch+".json")
    if os.path.exists(f): continue
    card={"char":ch,"head":row[0],"pinyin":row[1],"level":3,"parent":"夷","bus":[{"num":27,"name":"夷"}],
      "sections":[{"key":"shiyi","label":"释义","text":row[3],"cites":[]},
       {"key":"shengmu","label":"声母拟态","text":SM.get(ch,""),"cites":[]},
       {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
    json.dump(card,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); made+=1
print("rows",len(rows),"new",made)