# -*- coding: utf-8 -*-
import json,sys,glob,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; items=[]
import os as _os
_OWN=set(_os.path.splitext(f)[0] for f in _os.listdir(r"D:\系统汉字\web\public\cards") if f.endswith(".json"))
def _alist(c,d):
    s=set()
    for k in ("simp","trad"):
        v=d.get(k) or ""
        if v and v!=c: s.add(v)
    for v in (d.get("aliases") or []): s.add(v)
    return sorted(x for x in s if x)
for f in glob.glob(C+r"\*.json"):
    b=os.path.basename(f)
    if b in ("index.json","variants.json"): continue
    try: d=json.load(open(f,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict) or d.get("hidden"): continue
    bu=d.get("bus"); num=0; nm=""
    if isinstance(bu,dict): num=bu.get("num",0) or 0; nm=bu.get("name","") or ""
    elif isinstance(bu,list) and bu:
        e=bu[0]
        if isinstance(e,dict): num=e.get("num",0) or 0; nm=e.get("name","") or ""
        else: nm=str(e)
    items.append({"ch":d.get("chapter"),"cc":d.get("chapterCard",""),"cn":d.get("chapterName",""),"h":d.get("head") or "",
      "c":d.get("trad") or d.get("char",""),"a":_alist(d.get("trad") or d.get("char",""),d),"p":d.get("pinyin",""),"t":[x.get("label","") for x in d.get("sections",[]) if isinstance(x,dict)],"b":num,"n":nm,"lv":d.get("level",0),"rl":d.get("rootLevel") or 0,
      "pr":(d.get("char") if d.get("level")==2 else d.get("parent","")),"rc":d.get("rootChain",[]),})
items=[x for x in items if x["c"]]
import os as _os, glob as _glob
_by={}
for _f in _glob.glob(C+r"\\*.json"):
    _b=_os.path.basename(_f)[:-5]
    _by[_b]=_f
_seen={}
for x in items:
    k=x["c"]
    cur=_seen.get(k)
    if cur is None: _seen[k]=x; continue
    # 相同 c：优先保留 c 自身为文件名的条目
    if k in _by:
        _seen[k]=x if _os.path.basename(_by[k])[:-5]==k else cur
items=list(_seen.values())
items.sort(key=lambda x:x["c"]); json.dump(items,open(C+r"\index.json","w",encoding="utf-8"),ensure_ascii=False)
items.sort(key=lambda x:x["c"]); json.dump(items,open(C+r"\index.json","w",encoding="utf-8"),ensure_ascii=False)
print("index",len(items),"with parent",sum(1 for x in items if x["pr"]))