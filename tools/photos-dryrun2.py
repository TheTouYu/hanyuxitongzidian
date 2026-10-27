# -*- coding: utf-8 -*-
import sys,os,json,glob,hashlib,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; PH=os.path.join(ROOT,"web","public","glyphs","photos")
CM=json.load(io.open(os.path.join(ROOT,".tmp-charmap.json"),encoding="utf-8"))
Z=json.load(io.open(os.path.join(ROOT,"web","public","zigen.json"),encoding="utf-8"))
HEADS=set(Z.get("byName",{})) | set(CM)
CUR=json.load(io.open(os.path.join(PH,"index.json"),encoding="utf-8")).get("photos") or {}
CAP=json.load(io.open(os.path.join(PH,"captions.json"),encoding="utf-8")).get("captions") or {}
def ishead(t):
    t=t.strip()
    if not t: return None
    for k in (1,2):
        c=t[:k]
        if c in HEADS:
            rest=t[k:]
            if rest[:1] in "（(：" : return c
            py=(CM.get(c,{}) or {}).get("py") or ""
            if py and rest[:2]==py[:2]: return c
    return None
def imgs(p,parts):
    out=[]
    for bl in p.iter():
        for a,v in bl.attrib.items():
            if a.endswith('}embed') or a.endswith('}id'):
                try:
                    q=parts[v]
                    if hasattr(q,"blob") and q.content_type.startswith("image/"):
                        out.append((q.content_type,q.blob))
                except KeyError: pass
    return out
NEW={};NEWC={};EMF=0
for doc in sorted(glob.glob(os.path.join(r"D:\字谱智能体","*.docx"))):
    d=Document(doc); parts=d.part.related_parts
    cur=None;last=None
    for p in d.paragraphs:
        t=p.text.strip(); h=ishead(t)
        if h: cur=h
        if not cur: continue
        for ct,b in imgs(p._p,parts):
            if len(b)<20000: continue
            if "emf" in ct: EMF+=1; continue
            NEW.setdefault(cur,[]).append(hashlib.sha1(b).hexdigest()[:10]); last=cur
        if t.startswith("▲") and last:
            NEWC.setdefault(last,[]).append(t.lstrip("▲ ").strip()); last=None
print("HEADS",len(HEADS),"新字头",len(NEW),"有注",len(NEWC),"跳过EMF",EMF)
def L(x): return len(x or [])
for c in ("帝","啇","蒂","示","市","款","柰","祟","蹋","麝"):
    print(" ",c,"旧",L(CUR.get(c)),"新",L(NEW.get(c)),"新注",(NEWC.get(c) or [None])[0])
diff=[c for c in set(NEW)|set(CUR) if sorted(NEW.get(c,[]))!=sorted(CUR.get(c,[]))]
print("归属变化",len(diff),"丢失字头",len([c for c in CUR if c not in NEW]),"新增字头",len([c for c in NEW if c not in CUR]))
json.dump({"new":NEW,"newc":NEWC},io.open(os.path.join(ROOT,".tmp-photo-dry2.json"),"w",encoding="utf-8"),ensure_ascii=False)