# -*- coding: utf-8 -*-
import json,io,os,sys,glob,re,html
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
SRC=r"web\public\cards"; OUT=os.path.join(SRC,"html")
miss=set()
for f in glob.glob(os.path.join(OUT,"*.html")):
    if "此字暂无独立词条页" in io.open(f,encoding="utf-8").read(): miss.add(os.path.basename(f)[:-5])
info={}
for fp in glob.glob(os.path.join(SRC,"*.json")):
    b=os.path.basename(fp)
    if b in ("index.json","variants.json","captions.json"): continue
    try: d=json.load(io.open(fp,encoding="utf-8"))
    except Exception: continue
    par=d.get("char"); bus=d.get("bus") or []
    for s in d.get("sections",[]):
        for g in (s.get("groups") or []):
            for r in (g.get("rows") or []):
                if not r: continue
                m=re.match(r"^([^\s（(]+)",str(r[0]))
                if not m: continue
                head=m.group(1)
                if head in miss and head not in info:
                    info[head]={"py":r[1] if len(r)>1 else "","lei":r[2] if len(r)>2 else "","yi":r[3] if len(r)>3 else "","parent":par,"bus":bus,"grp":g.get("title","")}
made=0
for c,v in info.items():
    d={"char":c,"pinyin":v["py"],"level":3,"parent":v["parent"],"bus":v["bus"],
       "sections":[{"key":"shiyi","label":"释义","text":v["yi"],"cites":[]},
                   {"key":"shengmu","label":"声母拟态","text":"（未列，按原稿字族表照录）","cites":[]}]}
    json.dump(d,io.open(os.path.join(SRC,c+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); made+=1
print("cards made",made,"of",len(miss))