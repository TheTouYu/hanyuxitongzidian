# -*- coding: utf-8 -*-
import sys,os,json,io,re,glob,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards"); INL=os.path.join(ROOT,"web","public","glyphs","inline")
CM=json.load(io.open(os.path.join(ROOT,".tmp-charmap.json"),encoding="utf-8"))
Z=json.load(io.open(os.path.join(ROOT,"web","public","zigen.json"),encoding="utf-8"))
HEADS=set(Z.get("byName",{})) | set(CM)
BU=re.compile(r"^(\d{1,3})[.．]\s*(\S{1,2})部$")
FLD=[("本義","benyi"),("本义","benyi"),("轉義","zhuanyi"),("转义","zhuanyi"),("辯證","bianzheng"),("辩证","bianzheng"),("音源","yinyuan"),("字族衍義","zizu"),("字族衍义","zizu")]
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
def imgs(p,parts):
    out=[]
    for bl in p.iter():
        for a,v in bl.attrib.items():
            if a.endswith('}embed') or a.endswith('}id'):
                try:
                    q=parts[v]
                    if hasattr(q,"blob") and q.content_type.startswith("image/"): out.append(q.blob)
                except KeyError: pass
    return out
if os.path.isdir(INL): shutil.rmtree(INL)
cnt={}
for doc in sorted(glob.glob(os.path.join(r"D:\字谱智能体","*.docx"))):
    d=Document(doc); parts=d.part.related_parts; cur=None; fld=None
    for p in d.paragraphs:
        t=p.text.strip(); m=BU.match(t)
        if m: cur=m.group(2); fld=None; continue
        h=hc(t)
        if h: cur=h; fld=None
        for lab,key in FLD:
            if t.startswith(lab): fld=key; break
        if not cur or not fld: continue
        for b in imgs(p._p,parts):
            if len(b)>=20000 or b[:4]==b"\x89PNG" and False: pass
            if len(b)<1200: continue
            d2=os.path.join(INL,cur,fld); os.makedirs(d2,exist_ok=True)
            k=len(os.listdir(d2))+1
            ext=".png" if b[:4]==b"\x89PNG" else ".jpg"
            open(os.path.join(d2,f"{k:02d}{ext}"),"wb").write(b)
            cnt[cur]=cnt.get(cur,0)+1
print("inline 字头",len(cnt),"图",sum(cnt.values()))
# 卡片回填 gimgs
LAB=re.compile(r"(^|\n)\s*(?:【[^】]*】\s*)?(?:本義|本义|轉義|转义|辯證|辩证|音源|字族衍義|字族衍义)\s*[：:]\s*")
n=g=0
for p in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(p)
    if b=="index.json": continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    ch2=False
    for s in d.get("sections",[]):
        if "text" in s and s["text"]:
            t2=LAB.sub(lambda m:(m.group(1) or "")+"",s["text"])
            if t2!=s["text"]: s["text"]=t2; ch2=True
        dd=os.path.join(INL,ch,s.get("key",""))
        if os.path.isdir(dd):
            files=sorted(os.listdir(dd))
            if files: s["gimgs"]=[f"inline/{ch}/{s['key']}/{f}" for f in files[:8]]; g+=1; ch2=True
    if ch2:
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("回填卡",n,"插图点",g)