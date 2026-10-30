# -*- coding: utf-8 -*-
import re,json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷四  弋.docx").paragraphs]
pat=re.compile(r"^([^\s（(《▲①-⑳]{1,2})(（[^）]*）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü、]+)\s*[《]")
groups=[(110,117,"尗"),(126,140,"叔"),(155,232,"曳")]
made=[]
for a,b,pari in groups:
    for k in range(a,b):
        t=ps[k]
        if not t or t.startswith(("▲","①","②","③","字族","本義","轉義","辯證","音源","（")): continue
        m=pat.match(t)
        if not m: continue
        ch=m.group(1); py_=m.group(3).split("、")[0]
        if len(ch)>1 or not py_: continue
        head=ch+(m.group(2) or "")
        d={"char":ch,"trad":ch,"pinyin":py_,"level":3,"parent":pari,"bus":[{"num":26,"name":"弋"}],
           "head":head,"aliases":[],
           "sections":[{"key":"shi","label":"释义","text":t,"cites":[]},
             {"key":"shengmu","label":"声母拟态","text":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","cites":[]},
             {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}],"cites":[]}]}
        json.dump(d,io.open(C+"\\"+ch+".json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
        made.append((ch,pari))
print(len(made),made[:6])