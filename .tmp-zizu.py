# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for ch in ("禾","科"):
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    gs=d.pop("groups",[])
    for g in gs:
        g["rows"]=[[r["ch"]+("（"+r["alt"]+"）" if r.get("alt") else ""), r.get("py",""), r.get("cat",""), r.get("text","")] for r in g.get("rows",[])]
    secs=[s for s in d["sections"] if s.get("key") not in ("zizu","erji")]
    secs.append({"key":"zizu","label":"字族衍义","text":"","groups":gs})
    if ch=="禾":
        secs.append({"key":"erji","label":"本部二级字根","links":[{"ch":"科","label":"科"}]})
    d["sections"]=secs
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("patched")