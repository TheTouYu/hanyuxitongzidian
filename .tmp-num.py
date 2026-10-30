# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
D=r"D:\系统汉字\web\public\cards"
M="①②③④⑤⑥⑦⑧⑨⑩"
n=0; files=0
for fn in sorted(os.listdir(D)):
    if not fn.endswith(".json") or fn=="index.json" or fn=="variants.json": continue
    p=os.path.join(D,fn)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    ch=False
    for s in d.get("sections") or []:
        gs=s.get("groups") or []
        for i,g in enumerate(gs):
            lab=(g.get("label") or "").strip()
            if not lab: continue
            if re.match(r"^[①②③④⑤⑥⑦⑧⑨⑩]", lab): continue
            g["label"]=M[i] if i<len(M) else "[%d]"%(i+1)
            g["label"]+=lab; ch=True; n+=1
    if ch: json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); files+=1
print("fixed_groups",n,"files",files)