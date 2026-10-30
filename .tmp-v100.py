# -*- coding: utf-8 -*-
import io,json,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for f in glob.glob(C+r"\*.json"):
    b=f.split("\\")[-1]
    if b.startswith("卷") or b in ("index.json","variants.json"): continue
    try: d=json.load(io.open(f,encoding="utf-8"))
    except Exception: continue
    ch=d.get("char"); hit=False
    for s in d.get("sections",[]):
        if s.get("label")=="所属卷" and s.get("links"):
            L=[x for x in s["links"] if not str(x.get("ch","")).startswith("卷") and x.get("ch")!=ch]
            if len(L)!=len(s["links"]): s["links"]=L; hit=True
    if hit: json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("所属卷去卷链与自身",n)
d=json.load(io.open(C+r"\奚.json",encoding="utf-8"))
print([x["label"] for s in d["sections"] if s.get("label")=="所属卷" for x in s["links"]])