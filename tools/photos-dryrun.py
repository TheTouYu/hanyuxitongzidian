# -*- coding: utf-8 -*-
import sys,os,json,glob,hashlib,re,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; PH=os.path.join(ROOT,"web","public","glyphs","photos")
CM=json.load(io.open(os.path.join(ROOT,".tmp-charmap.json"),encoding="utf-8"))
CUR=json.load(io.open(os.path.join(PH,"index.json"),encoding="utf-8")).get("photos") or {}
CAP=json.load(io.open(os.path.join(PH,"captions.json"),encoding="utf-8")).get("captions") or {}
W="{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
def ishead(t):
    t=t.strip()
    if len(t)<1: return None
    for k in (1,2):
        c=t[:k]
        if c in CM:
            rest=t[k:]
            if rest[:1] in "（(" : return c
            py=(CM[c].get("py") or "")
            if py and rest.startswith(py[:2]): return c
            if rest[:1] in "《：" and k==1 and len(rest)>1: return c
    return None
def imgs(p,parts):
    out=[]
    for bl in p.iter():
        for a,v in bl.attrib.items():
            if a.endswith('}embed') or a.endswith('}id'):
                try:
                    q=parts[v]
                    if hasattr(q,"blob") and q.content_type.startswith("image"): out.append(q.blob)
                except KeyError: pass
    return out
bad=[]; NEW={}; NEWC={}; files=0
for doc in sorted(glob.glob(os.path.join(r"D:\字谱智能体","*.docx"))):
    d=Document(doc); files+=1
    for s in d.sections:
        cols=[c for c in s._sectPr.iter() if c.tag.endswith('}cols')]
        for c in cols:
            n=c.get(W+"num")
            if n not in (None,"1","0"): bad.append((os.path.basename(doc),n))
    parts=d.part.related_parts; cur=None; lastimg=None
    for p in d.paragraphs:
        t=p.text.strip(); h=ishead(t)
        if h: cur=h
        if not cur: continue
        ims=[b for b in imgs(p._p,parts) if len(b)>=20000]
        for b in ims:
            NEW.setdefault(cur,[]).append(hashlib.sha1(b).hexdigest()[:10]); lastimg=cur
        if t.startswith("▲") and lastimg:
            NEWC.setdefault(lastimg,[]).append(t.lstrip("▲ ").strip()); lastimg=None
print("docx",files,"非单栏",bad[:5],"共",len(bad))
print("新映射字头",len(NEW),"有注字头",len(NEWC),"旧映射",len(CUR))
def L(x): return len(x or [])
diff=[c for c in set(NEW)|set(CUR) if sorted(NEW.get(c,[]))!=sorted(CUR.get(c,[]))]
print("归属有变化字头",len(diff))
for c in ("帝","啇","蒂","示","市","祟","款","柰"):
    print(" ",c,"旧",L(CUR.get(c)),"新",L(NEW.get(c)),"旧注",CAP.get(c),"新注",NEWC.get(c))
json.dump({"new":{k:v for k,v in NEW.items()},"newc":NEWC,"diff":diff},io.open(os.path.join(ROOT,".tmp-photo-dry.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("样例变化",[(c,L(CUR.get(c)),L(NEW.get(c))) for c in diff[:12]])