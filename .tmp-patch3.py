# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(p,encoding="utf-8").read()
t=t.replace("C=r\"D:\\系统汉字\\web\\public\\cards\"; items=[]","""C=r"D:\\系统汉字\\web\\public\\cards"; items=[]
def _alist(c,d):
    s=set()
    for k in ("simp","trad"):
        v=d.get(k) or ""
        if v and v!=c: s.add(v)
    for v in (d.get("aliases") or []): s.add(v)
    return sorted(x for x in s if x)""",1)
io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("moved def to top")