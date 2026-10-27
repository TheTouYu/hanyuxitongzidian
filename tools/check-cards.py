# -*- coding: utf-8 -*-
import json,io,glob,sys,collections
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; bad=collections.Counter(); ex={}
for f in glob.glob(C+r"\*.json"):
    if f.endswith("index.json"): continue
    try: d=json.load(io.open(f,encoding="utf-8"))
    except Exception as e: bad["json"]+=1; continue
    ch=d.get("char") or f
    ks=[s.get("key") for s in d.get("sections",[])]
    if len(ks)!=len(set(ks)): bad["dup-section"]+=1; ex.setdefault("dup-section",ch)
    for s in d.get("sections",[]):
        g=s.get("groups")
        if g:
            for gg in g:
                rows=gg.get("rows") or []
                if not rows: bad["empty-rows"]+=1; ex.setdefault("empty-rows",ch)
                for r in rows:
                    if not isinstance(r,list) or len(r)!=4: bad["row-cols"]+=1; ex.setdefault("row-cols",ch)
        if s.get("key")=="zizu" and not g: bad["zizu-no-table"]+=1; ex.setdefault("zizu-no-table",ch)
    if d.get("level")==2 and "zizu" not in ks: bad["lv2-no-zizu"]+=1; ex.setdefault("lv2-no-zizu",ch)
print(dict(bad), ex)