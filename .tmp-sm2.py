# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
A="j「聚决」取「决」：斤刃劈木，一擊而斷（推）。"
B="j「聚决」取「聚」：軛聚束於牲口肩頸，夾持而前拉（推）。"
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    q=os.path.join(C,fn)
    try: d=json.load(io.open(q,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    ch=False
    for s in d.get("sections",[]):
        t=s.get("text") or ""
        if re.match(r"[jqx]「夹卸」",t):
            s["text"]= B if ("牲口肩頸" in t or "夾持而前拉" in t) else A
            ch=True
    if ch: json.dump(d,io.open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("fixed",n)
# 体例 2.1 去掉自造组名
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
t2=t.replace("j「夹卸」/q「卸」/x「卸续」","j「聚决」/q「亲缺」/x「续消」").replace("「加」取「夹」","「加」取「聚」")
if t2!=t: io.open(p,"w",encoding="utf-8",newline="\n").write(t2); print("patched exegesis")