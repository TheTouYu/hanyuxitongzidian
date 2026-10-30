# -*- coding: utf-8 -*-
import io,json,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
a=json.load(io.open(C+r"\愛.json",encoding="utf-8")); a["simp"]="爱"; a["aliases"]=list(set(a.get("aliases",[])+["爱"]))
json.dump(a,io.open(C+r"\愛.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
b=json.load(io.open(C+r"\爱.json",encoding="utf-8")); b["hidden"]=True
json.dump(b,io.open(C+r"\爱.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
p=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(p,encoding="utf-8").read()
if 'd.get("hidden")' not in t:
    t=t.replace('    if not isinstance(d,dict): continue','    if not isinstance(d,dict) or d.get("hidden"): continue',1)
    io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("builder skips hidden")
print("ok")