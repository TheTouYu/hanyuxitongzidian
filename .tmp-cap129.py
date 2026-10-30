# -*- coding: utf-8 -*-
import json,io,os,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
by=z["byName"]; juans={j["no"]:j.get("name") or "" for j in z.get("juan",[])}
no2name={v["no"]:k for k,v in by.items()}
vnames=[os.path.basename(f)[:-5] for f in glob.glob(C+r"\卷*.json")]
def jcard(no):
    nm=juans.get(no,"")
    for v in vnames:
        if nm and nm in v: return v
    return None
n=0
for f in glob.glob(C+r"\*.json"):
    if f.endswith("index.json"): continue
    d=json.load(io.open(f,encoding="utf-8")); secs=d.get("sections")
    if not isinstance(secs,list) or any(s.get("key")=="suoshu" for s in secs): continue
    ch=d.get("char"); jn=None
    if ch in by: jn=by[ch].get("juanNo")
    if not jn:
        b=d.get("bus") or []
        num=None
        if b:
            x=b[0]
            num=x.get("num") if isinstance(x,dict) else None
        if num: 
            nm=no2name.get(num)
            if nm in by: jn=by[nm].get("juanNo")
    if not jn:
        par=d.get("parent")
        if par in by: jn=by[par].get("juanNo")
    card=jcard(jn) if jn else None
    if not card: continue
    secs.append({"key":"suoshu","label":"所属卷","text":"","links":[{"ch":card,"label":card}],"cites":[]})
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("第二轮补所属卷",n)