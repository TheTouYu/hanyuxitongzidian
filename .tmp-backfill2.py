# -*- coding: utf-8 -*-
import json,io,os,re,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs\inline"
DOCS=sorted(glob.glob(r"D:\字谱智能体\*.docx"))
recs=[]   # (docname,k,plain,runs)
for fn in DOCS:
    try: doc=Document(fn)
    except Exception: continue
    parts=doc.part.related_parts
    for k,p in enumerate(doc.paragraphs):
        runs=[]; imgs=0
        for el in p._p.iter():
            tag=el.tag.split("}")[-1]
            if tag=="t": runs.append(("t",el.text or ""))
            elif tag=="blip":
                rid=[v for x,v in el.attrib.items() if x.endswith("}embed") or x.endswith("}id")]
                if rid:
                    try: b=parts[rid[0]].blob
                    except KeyError: continue
                    runs.append(("i",b)); imgs+=1
        if imgs:
            plain="".join(x for t,x in runs if t=="t")
            recs.append((fn,k,plain,runs))
def norm(s): return re.sub(r'\s+','',s)
def strip_lab(s): return re.sub(r'^(本義|轉義|辯證|音源|释义)[：:]','',norm(s))
byplain={}
for i,(fn,k,plain,runs) in enumerate(recs): byplain.setdefault(norm(plain),[]).append(i)
fixed=[]; miss=[]
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    ch=d.get("char") or f[:-5]
    changed=False
    for s in d.get("sections",[]):
        if s.get("key") not in ("benyi","zhuanyi","bianzheng","yinyuan"): continue
        t=s.get("text") or ""
        if s.get("gdir") or ("《說文》" not in t and "《说文》" not in t): continue
        key=s["key"]; cur=strip_lab(t)
        cand=[i for i,(fn,k,plain,runs) in enumerate(recs) if norm(plain).startswith(cur[:20])]
        got=None
        for i in cand:
            fn,k,plain,runs=recs[i]
            if norm(plain)==cur or cur==norm(plain) or norm(plain).endswith(cur) or cur.endswith(norm(plain)):
                got=i; break
        if got is None:
            miss.append((ch,key,cur[:20])); continue
        fn,k,plain,runs=recs[got]
        dd=os.path.join(G,ch,key); os.makedirs(dd,exist_ok=True)
        for old in os.listdir(dd): os.remove(os.path.join(dd,old))
        out=[]; n=0
        for t2,val in runs:
            if t2=="t": out.append(val)
            else:
                n+=1; ext="png" if val[:4]==b"\x89PNG" else ("jpg" if val[:2]==b"\xff\xd8" else "emf")
                fn2="%02d.%s"%(n,ext); open(os.path.join(dd,fn2),"wb").write(val)
                out.append("{{%s/%s}}"%(key,fn2))
        txt=re.sub(r'^(本義|轉義|辯證|音源|释义)[：:]','',"".join(out).strip()).strip()
        s["text"]=txt; s["gdir"]="inline/"+ch; changed=True; fixed.append((ch,key,n))
    if changed: json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("fixed",len(fixed),fixed[:20]); print("miss",len(miss),miss[:10])