# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
HAN="[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002a6df]"
fixed=[]
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    ch=d.get("char") or f[:-5]
    shi=next((s.get("text","") for s in d.get("sections",[]) if s.get("key")=="shiyi"),"")
    m=re.match("^("+HAN+"+)\s*（([^）]*)）",shi)
    if not m: continue
    inner="".join(re.findall(HAN,m.group(2)))
    if not inner or inner==ch: continue
    al=set(d.get("aliases") or []); before=set(al)
    al.add(inner); d["aliases"]=sorted(al)
    if not d.get("head") or d["head"]==ch: d["head"]=ch+"（"+inner+"）"
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    fixed.append((ch,inner))
print(len(fixed),fixed[:15])