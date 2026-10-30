# -*- coding: utf-8 -*-
import json,io,os,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
by=z["byName"]; juans={j["no"]:j.get("name") or "" for j in z.get("juan",[])}
vnames=[os.path.basename(f)[:-5] for f in glob.glob(C+r"\卷*.json")]
def jcard(no):
    nm=juans.get(no,"")
    for v in vnames:
        if nm and nm in v: return v
    return None
n=0;skip=0
for f in glob.glob(C+r"\*.json"):
    if f.endswith("index.json"): continue
    d=json.load(io.open(f,encoding="utf-8")); ch=d.get("char")
    secs=d.get("sections")
    if not isinstance(secs,list): skip+=1; continue
    if any(s.get("key")=="suoshu" for s in secs): continue
    info=by.get(ch)
    if not info: continue
    jn=info.get("juanNo"); card=jcard(jn) if jn else None
    if not card: continue
    secs.append({"key":"suoshu","label":"所属卷","text":"","links":[{"ch":card,"label":card}],"cites":[]})
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("补所属卷",n,"跳过异常卡",skip)