# -*- coding: utf-8 -*-
import json,io,os,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
by=z["byName"]; juans={j["no"]:j.get("name") or "" for j in z.get("juan",[])}
# 卷卡名来自 cards/卷*.json
vnames=[os.path.basename(f)[:-5] for f in glob.glob(C+r"\卷*.json")]
def jcard(no):
    nm=juans.get(no,"")
    for v in vnames:
        if v.startswith(f"卷{['一','二','三','四','五','六','七','八','九','十'][no-1] if 1<=no<=10 else ''}") and nm and nm in v:
            return v
    for v in vnames:
        if nm and nm in v: return v
    return None
n=0
for f in glob.glob(C+r"\*.json"):
    if f.endswith("index.json"): continue
    d=json.load(io.open(f,encoding="utf-8")); ch=d.get("char")
    if any(s.get("key")=="suoshu" for s in d["sections"]): continue
    info=by.get(ch)
    if not info:
        b=d.get("bus") or []
        if b and b[0].get("num"): 
            # 用部号找不到卷号，跳过
            pass
        continue
    jn=info.get("juanNo"); nm=juans.get(jn,"")
    card=jcard(jn) if jn else None
    if not card: continue
    d["sections"].append({"key":"suoshu","label":"所属卷","text":"","links":[{"ch":card,"label":card}],"cites":[]})
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("补所属卷",n)