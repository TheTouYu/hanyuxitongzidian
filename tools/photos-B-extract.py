# -*- coding: utf-8 -*-
import sys,os,json,glob,hashlib,io,re,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; PH=os.path.join(ROOT,"web","public","glyphs","photos")
TMP=os.path.join(ROOT,".tmp-photos-new")
CM=json.load(io.open(os.path.join(ROOT,".tmp-charmap.json"),encoding="utf-8"))
Z=json.load(io.open(os.path.join(ROOT,"web","public","zigen.json"),encoding="utf-8"))
HEADS=set(Z.get("byName",{})) | set(CM)
BU=re.compile(r"^(\d{1,3})[.．]\s*(\S{1,2})部$")
def headchar(t):
    t=t.strip()
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
if os.path.isdir(TMP): shutil.rmtree(TMP)
os.makedirs(TMP,exist_ok=True)
NEW={};CAPT={};emf=[]
for doc in sorted(glob.glob(os.path.join(r"D:\字谱智能体","*.docx"))):
    d=Document(doc); parts=d.part.related_parts
    bu=None; phase="body"; fam=None; lastowner=None
    for p in d.paragraphs:
        t=p.text.strip()
        m=BU.match(t)
        if m: bu=m.group(2); phase="body"; fam=None; lastowner=bu; continue
        if t.startswith("字族衍義") or t.startswith("字族衍义"): phase="family"; fam=None; continue
        if phase=="family":
            h=headchar(t)
            if h: fam=h
            owner=fam or bu
        else:
            h=headchar(t)
            if h: bu=h if bu is None else bu
            owner=bu
        if not owner: continue
        for ct,b in imgs(p._p,parts):
            if len(b)<20000: continue
            lst=NEW.setdefault(owner,[])
            hsh=hashlib.sha1(b).hexdigest()[:10]
            if any(h==hsh for h,_ in lst): continue
            if "emf" in ct:
                fn=f"{len(lst)+1:02d}.emf"; open(os.path.join(TMP,owner+"__"+fn) if False else os.path.join(TMP,f"{owner}@@{fn}"),"wb").write(b); emf.append((owner,fn))
                lst.append((hsh,None))
            else:
                ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
                fn=f"{len(lst)+1:02d}{ext}"; os.makedirs(os.path.join(TMP,owner),exist_ok=True)
                open(os.path.join(TMP,owner,fn),"wb").write(b); lst.append((hsh,fn))
            lastowner=owner
        if t.startswith("▲") and lastowner:
            CAPT.setdefault(lastowner,[]).append(t.lstrip("▲ ").strip()); lastowner=None
print("新字头",len(NEW),"EMF",len(emf),"有注",len(CAPT))
json.dump({"owners":{c:[h for h,_ in v] for c,v in NEW.items()},"caps":CAPT,"emf":emf},io.open(os.path.join(ROOT,".tmp-photoB.json"),"w",encoding="utf-8"),ensure_ascii=False)
for c in ("帝","啇","蒂","示","市","款","柰","祟"):
    print(" ",c,len(NEW.get(c,[])),(CAPT.get(c) or [None])[0])