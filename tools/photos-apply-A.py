# -*- coding: utf-8 -*-
import sys,os,json,glob,hashlib,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; PH=os.path.join(ROOT,"web","public","glyphs","photos")
CM=json.load(io.open(os.path.join(ROOT,".tmp-charmap.json"),encoding="utf-8"))
Z=json.load(io.open(os.path.join(ROOT,"web","public","zigen.json"),encoding="utf-8"))
HEADS=set(Z.get("byName",{})) | set(CM)
IDX=json.load(io.open(os.path.join(PH,"index.json"),encoding="utf-8")); OLD=IDX.get("photos") or IDX
CAPD=json.load(io.open(os.path.join(PH,"captions.json"),encoding="utf-8")); CAP=CAPD.get("captions") or CAPD
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
                    if hasattr(q,"blob") and q.content_type.startswith("image/") and "emf" not in q.content_type:
                        out.append(q.blob)
                except KeyError: pass
    return out
NEW={};NEWC={}
for doc in sorted(glob.glob(os.path.join(r"D:\字谱智能体","*.docx"))):
    d=Document(doc); parts=d.part.related_parts; cur=None; last=None
    for p in d.paragraphs:
        t=p.text.strip(); h=ishead(t)
        if h: cur=h
        if not cur: continue
        for b in imgs(p._p,parts):
            if len(b)<20000: continue
            NEW.setdefault(cur,[]).append((hashlib.sha1(b).hexdigest()[:10],b)); last=cur
        if t.startswith("▲") and last:
            NEWC.setdefault(last,[]).append(t.lstrip("▲ ").strip()); last=None
def oldhash(ch):
    d=os.path.join(PH,ch); 
    if not os.path.isdir(d): return []
    return [hashlib.sha1(open(os.path.join(d,f),"rb").read()).hexdigest()[:10] for f in sorted(os.listdir(d))]
changed=[]; kept=[]; added=[]
for ch,lst in NEW.items():
    nh=[h for h,_ in lst]
    if len(nh)<1: continue
    oh=oldhash(ch)
    if sorted(nh)==sorted(oh): continue
    if not oh: added.append(ch)
    elif len(nh)>len(oh)+1: kept.append(ch); continue   # 保守：不走数量暴涨
    else: changed.append(ch)
    d=os.path.join(PH,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    seen=set(); files=[]
    for h,b in lst:
        if h in seen: continue
        seen.add(h)
        ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
        fn=f"{len(files)+1:02d}{ext}"; open(os.path.join(d,fn),"wb").write(b); files.append(fn)
    OLD[ch]=files
    if NEWC.get(ch): CAP[ch]=NEWC[ch][:len(files)]
json.dump({"photos":OLD},io.open(os.path.join(PH,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":CAP},io.open(os.path.join(PH,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("changed",len(changed),"added",len(added),"skip暴涨",len(kept),"总字头",len(OLD))
for c in ("帝","啇","蒂","示","市","款","柰"):
    print(" ",c,OLD.get(c),CAP.get(c))