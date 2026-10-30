# -*- coding: utf-8 -*-
import json,io,os,re,sys,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
def strip(t):
    for q in ("本義：","轉義：","辯證：","音源："):
        if t.startswith(q): return t[len(q):].lstrip()
    return t
p=os.path.join(C,"斦.json"); d=json.load(io.open(p,encoding="utf-8"))
t={s["key"]:s for s in d["sections"]}
t["benyi"]["text"]=strip(ps[750])
t["zhuanyi"]["text"]=strip(ps[751])+strip(ps[752])+strip(ps[753])+strip(ps[754])+strip(ps[755])
t["bianzheng"]["text"]=strip(ps[757])
t["yinyuan"]["text"]=strip(ps[758])
d["glyphChar"]="質"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 复制 質 字形到 斦
src=os.path.join(G,"質"); dst=os.path.join(G,"斦")
os.makedirs(dst,exist_ok=True)
files=sorted([f for f in os.listdir(src) if f.lower().endswith((".png",".jpg",".jpeg"))])
for i,f in enumerate(files,1):
    shutil.copy(os.path.join(src,f),os.path.join(dst,f"{i:02d}"+os.path.splitext(f)[1]))
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=ix.get("chars") or ix
ch["斦"]={"doc":"卷二 㠯","files":[f"{i:02d}"+os.path.splitext(f)[1] for i,f in enumerate(files,1)]}
json.dump(ix,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("字形",len(files),"本义头",t["benyi"]["text"][:26])