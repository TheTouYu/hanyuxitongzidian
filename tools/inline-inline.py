# -*- coding: utf-8 -*-
import sys,os,json,io,re,glob,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
from docx.oxml.ns import qn
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards"); INL=os.path.join(ROOT,"web","public","glyphs","inline")
CM=json.load(io.open(os.path.join(ROOT,".tmp-charmap.json"),encoding="utf-8"))
Z=json.load(io.open(os.path.join(ROOT,"web","public","zigen.json"),encoding="utf-8"))
HEADS=set(Z.get("byName",{})) | set(CM)
BU=re.compile(r"^(\d{1,3})[.．]\s*(\S{1,2})部$")
FLD=[("本義","benyi"),("本义","benyi"),("轉義","zhuanyi"),("转义","zhuanyi"),("辯證","bianzheng"),("辩证","bianzheng"),("音源","yinyuan"),("字族衍義","zizu"),("字族衍义","zizu")]
LAB=re.compile(r"^\s*(?:本義|本义|轉義|转义|辯證|辩证|音源|字族衍義|字族衍义)\s*[：:]\s*")
def hc(t):
    t=t.strip()
    for k in (1,2):
        c=t[:k]
        if c in HEADS:
            r=t[k:]
            if r[:1] in "（(：": return c
            py=(CM.get(c,{}) or {}).get("py") or ""
            if py and r[:2]==py[:2]: return c
    return None
def para_marked(p,parts,dirp,name0):
    out=[]; k=name0
    for r in p._p.iter(qn("w:r")):
        for t in r.iter(qn("w:t")):
            out.append(t.text or "")
        for bl in r.iter():
            for a,v in bl.attrib.items():
                if a.endswith("}embed") or a.endswith("}id"):
                    try: q=parts[v]
                    except KeyError: continue
                    if not hasattr(q,"blob") or not q.content_type.startswith("image/"): continue
                    b=q.blob
                    if not (80<=len(b)<20000): continue
                    k+=1; ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
                    open(os.path.join(dirp,f"{k:02d}{ext}"),"wb").write(b)
                    out.append("{{%02d%s}}"%(k,ext))
    return "".join(out),k
if os.path.isdir(INL): shutil.rmtree(INL)
FIELD={}
for doc in sorted(glob.glob(os.path.join(r"D:\字谱智能体","*.docx"))):
    d=Document(doc); parts=d.part.related_parts; cur=None; fld=None; buf=[]; k=0
    def flush():
        global buf
        if cur and fld and buf: FIELD[(cur,fld)]="\n".join(buf).strip()
        buf=[]
    for p in d.paragraphs:
        t=p.text.strip(); m=BU.match(t)
        if m:
            flush(); cur=m.group(2); fld=None; continue
        h=hc(t)
        if h:
            flush(); cur=h; fld=None
        nf=None
        for lab,key in FLD:
            if t.startswith(lab): nf=key; break
        if nf:
            flush(); fld=nf; k=0
            dirp=os.path.join(INL,cur,fld); os.makedirs(dirp,exist_ok=True)
            m2=buf
        if not cur or not fld: continue
        dirp=os.path.join(INL,cur,fld); os.makedirs(dirp,exist_ok=True)
        s,k=para_marked(p,parts,dirp,k)
        if s: buf.append(s)
    flush()
print("字段段",len(FIELD))
SRC={"benyi":"benyi","bengen":"benyi","shiyi":"benyi","bianzheng":"bianzheng","zhuanyi":"zhuanyi","yinyuan":"yinyuan"}
n=g=0
for pth in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(pth)
    if b=="index.json": continue
    d=json.load(io.open(pth,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    ch2=False
    for s in d.get("sections",[]):
        src=SRC.get(s.get("key",""))
        if not src: continue
        txt=FIELD.get((ch,src))
        if not txt or "{{" not in txt: continue
        txt=LAB.sub("",txt)
        s["text"]=txt; s["gdir"]=f"inline/{ch}/{src}"; s.pop("gimgs",None); g+=1; ch2=True
    if ch2:
        json.dump(d,io.open(pth,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改卡",n,"内嵌段",g)