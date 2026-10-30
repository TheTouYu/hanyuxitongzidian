# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
# 1) merge 雁 glyphs into 鴈 strip
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chars=ix.get("chars") or ix
y=(chars.get("鴈") or {}); yy=(chars.get("雁") or {})
files=list(y.get("files") or [])
for f in (yy.get("files") or []):
    if f not in files: files.append(f)
y["files"]=files; y.setdefault("variants",[]);
for v in (yy.get("variants") or []):
    if v not in y["variants"]: y["variants"].append(v)
chars["鴈"]=y
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
# 2) six goose photos
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
def imgs(k):
    out=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                try: out.append(parts[rid[0]].blob)
                except KeyError: pass
    return out
blobs=[]
for k in (244,246,248):
    bs=[b for b in imgs(k) if len(b)>5000]
    blobs+=bs[:2]
print("photos found",len(blobs))
d2=os.path.join(P,"鴈"); os.makedirs(d2,exist_ok=True)
for f in os.listdir(d2): os.remove(os.path.join(d2,f))
caps=["白額雁","豆雁","斑頭雁","灰雁","黑雁","鴻雁"]; names=[]
for i,b in enumerate(blobs[:6]):
    fn="%02d.jpg"%(i+1); open(os.path.join(d2,fn),"wb").write(b); names.append(fn)
pix=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); pm=pix.get("photos") or pix
cp=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cp.get("captions") or cp
pm["鴈"]=names; cm["鴈"]=caps[:len(names)]
json.dump({"photos":pm},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("glyph files",len(files),"photos",len(names))