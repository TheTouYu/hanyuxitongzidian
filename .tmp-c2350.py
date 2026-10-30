# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=doc.paragraphs; parts=doc.part.related_parts
# 1) 尗 字形（p101 段）
G=os.path.join(ROOT,"web","public","glyphs","尗")
os.makedirs(G,exist_ok=True)
for f in os.listdir(G): os.remove(os.path.join(G,f))
n=0
for k in (101,102):
    for el in ps[k]._p.iter():
        for a,v in el.attrib.items():
            if a.endswith("}embed") or a.endswith("}id"):
                try: b=parts[v].blob
                except KeyError: continue
                if len(b)<800: continue
                ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
                n+=1; open(os.path.join(G,f"{n:02d}{ext}"),"wb").write(b)
# 2) 花椒 照片改挂 茮
P=os.path.join(ROOT,"web","public","glyphs","photos")
src=os.path.join(P,"尗"); dst=os.path.join(P,"茮")
os.makedirs(dst,exist_ok=True)
files=sorted(os.listdir(src)) if os.path.isdir(src) else []
for f in files: shutil.move(os.path.join(src,f),os.path.join(dst,f))
if os.path.isdir(src) and not os.listdir(src): os.rmdir(src)
idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); ph=idx.get("photos") or idx
cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
if "尗" in ph: ph.pop("尗")
ph["茮"]=files
if "尗" in cm: cm.pop("尗")
cm["茮"]=["花椒"]
json.dump({"photos":ph},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
# 3) 尗 卡：去照片，写字形
C=os.path.join(ROOT,"web","public","cards")
d=json.load(io.open(os.path.join(C,"尗.json"),encoding="utf-8"))
d.pop("photos",None); d.pop("captions",None)
gj=json.load(io.open(os.path.join(ROOT,"web","public","glyphs","index.json"),encoding="utf-8"))
chars=gj.get("chars") or gj
chars["尗"]={"doc":"卷四  弋.docx","files":[f"尗/{i:02d}{os.path.splitext(sorted(os.listdir(G))[i-1])[1]}" for i in range(1,len(os.listdir(G))+1)]} if False else chars.get("尗")
files_sorted=sorted(os.listdir(G))
chars["尗"]={"doc":"卷四  弋.docx","files":[f"尗/{f}" for f in files_sorted],"variants":""}
json.dump({"chars":chars},io.open(os.path.join(ROOT,"web","public","glyphs","index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump(d,io.open(os.path.join(C,"尗.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("尗形",len(files_sorted),"花椒→茮",files)