# -*- coding: utf-8 -*-
import json,sys,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def fix(name):
    p=rf"{C}\{name}.json"; d=json.load(open(p,encoding="utf-8")); n=0
    for s in d["sections"]:
        if s.get("key")!="zizu" or not s.get("groups"): continue
        for g in s["groups"]:
            for r in g.get("rows",[]):
                t=r[3] if len(r)>3 else ""
                t=t.split("→")[0]+"→"+t.split("→")[1] if t.count("→")>=2 else t
                r[3]=t.strip(); n+=1
    json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); return n
for x in ["旨","耆","稽"]: print(x,fix(x))
p=r"D:\系统汉字\prompts\exegesis.md"; s=io.open(p,encoding="utf-8").read()
old="①本义是什么 → ②取了声根的哪一面义 → ③形旁定它落在哪一类；推演性的可标（推）。"
new="①本义是什么 → ②取了声根的哪一面义（只写这两段）；（形旁/类属另立一列，落点里不重复）；推演性的可标（推）。"
if old in s: io.open(p,"w",encoding="utf-8",newline="\n").write(s.replace(old,new,1)); print("rule ok")