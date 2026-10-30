# -*- coding: utf-8 -*-
import json,io,glob,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for f in glob.glob(C+r"\*.json"):
    if f.endswith("index.json"): continue
    try: d=json.load(io.open(f,encoding="utf-8"))
    except Exception: continue
    for s in d.get("sections",[]):
        g=s.get("groups") or []
        if len(g)==1:
            t=g[0].get("title","")
            t2=re.sub(r"^[①②③④⑤⑥⑦⑧⑨⑩]\s*","",t)
            if t2!=t: g[0]["title"]=t2; n+=1
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("single-group 序号 removed:",n)