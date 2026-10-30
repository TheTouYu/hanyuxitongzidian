# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
J="j「夹卸」取「夹」：軛夾加於牲口肩頸，夾持而前拉（推）。"
names=["加","駕","嘉","枷","痂","珈","跏","笳","䴥","𨔣","迦","泇","架","𧉪","袈","鉫","𦙺","𢉤"]
for name in names:
    p=os.path.join(C,name+".json")
    if not os.path.exists(p): continue
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="shengmu": s["text"]=J
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# rule text
p=r"D:\系统汉字\prompts\exegesis.md"; t=io.open(p,encoding="utf-8").read()
t=t.replace("**j 取「夹」（夹持）、q 取「泄/切」、x 取「泄/续」**","**j 取「夹」（夹持）、q 取「卸/切」、x 取「卸/续」**")
t=t.replace("j「夹泄」取「夹」","j「夹卸」取「夹」")
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("ok")