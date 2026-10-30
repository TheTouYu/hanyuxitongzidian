# -*- coding: utf-8 -*-
import json,io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷七  斤.docx").paragraphs]
GROUPS=[(39,54),(54,65),(65,75),(75,84)]
HAN=r"[\u3400-\u9fff\U00020000-\U0002A6DF]"
groups=[]
for (a,b) in GROUPS:
    title=ps[a]
    rows=[]
    for k in range(a+1,b):
        t=ps[k]
        if not t: continue
        m=re.match(r"^("+HAN+r"+)(?:（([^）]*)）)?\s*([a-zA-Züǖǘǚǜāáǎàēéěèīíǐìōóǒòūúǔùǹń]+)?",t)
        if not m: continue
        ch=m.group(1)
        aliases=[x for x in re.findall(HAN,m.group(2) or "")]
        py=m.group(3) or ""
        gl=re.search(r"从("+HAN+r")",t); lei=gl.group(1) if gl else ""
        rows.append([ch,py,lei,t])
    groups.append({"no":"①②③④"[len(groups)],"title":re.sub(r"^[①-⑨]","",title),"rows":rows})
p=r"D:\系统汉字\web\public\cards\斤.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu": s["groups"]=groups
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([(g["no"],len(g["rows"])) for g in groups], sum(len(g["rows"]) for g in groups))