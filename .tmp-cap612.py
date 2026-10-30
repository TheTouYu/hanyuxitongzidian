# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
n=0; ex=[]
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    ch=d.get("char","")
    if not ch: continue
    txt=""
    for s in d.get("sections",[]):
        if isinstance(s,dict) and s.get("key")=="shiyi": txt=s.get("text",""); break
    m=re.match(rf"^{re.escape(ch)}（([^）]+)）",txt)
    if not m: continue
    al=[c for c in m.group(1) if c.strip()]
    if not al: continue
    d["head"]=txt[:txt.index("）")+1]
    d["aliases"]=sorted(set((d.get("aliases") or [])+al))
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
    if len(ex)<5: ex.append((ch,d["head"],d["aliases"]))
print("补 alias",n); [print(x) for x in ex]