# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
def S(k,l,t): return {"key":k,"label":l,"text":t,"cites":[]}
J={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷二㠯","label":"卷二 㠯"}]}
data={"技":("jì",ps[730]),"妓":("jì",ps[733]),"䰙":("yǐ",ps[734])}
for ch,(py,txt) in data.items():
    al=[]
    m=re.search(r"（([^）]*)）",txt.split("《")[0])
    if m: al=list(m.group(1))
    d={"char":ch,"head":ch+(f"（{m.group(1)}）" if m else ""),"pinyin":py,"level":3,"parent":"支",
       "bus":[{"num":13,"name":"支"}],
       "sections":[S("shiyi","释义",txt),
                   S("shengmu","声母拟态",f"{py[0].lower()}：取绪论拟态义一面（推）。"),
                   J],
       "aliases":[a for a in al if a!=ch]}
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
z=json.load(io.open(os.path.join(C,"支.json"),encoding="utf-8"))
tbl=[s for s in z["sections"] if s.get("key")=="zizu"][0]
for ch,(py,txt) in data.items():
    tbl["groups"][1]["rows"].append([ch,py,"支",txt])
json.dump(z,io.open(os.path.join(C,"支.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("行数",[len(g["rows"]) for g in tbl["groups"]])