# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-rel2.py"
t=io.open(p,encoding="utf-8").read()
old='"pr":d.get("parent",""),'
new='"pr":(d.get("parent") or (d.get("trad") or d.get("char","") if d.get("level")==1 else "")),'
if old in t and new not in t:
    io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1)); print("patched rel2")
else:
    print("skip", old in t, new in t)