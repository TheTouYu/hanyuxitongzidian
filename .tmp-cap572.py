# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
targets=["啠","躓","𠘖","𡂒","𧓳"]
for ch in targets:
    pat=re.compile(r"^"+re.escape(ch)+r"(（[^）]*）)?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+")
    hit=next((t for t in ps[745:790] if pat.match(t)),None)
    if not hit: print("still miss",ch); continue
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s["key"]=="shiyi": s["text"]=hit
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print(ch,"->",hit[:30])