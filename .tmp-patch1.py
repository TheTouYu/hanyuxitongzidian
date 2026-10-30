# -*- coding: utf-8 -*-
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(p,encoding="utf-8").read()
if '"a":' in t and 'alist' not in t:
    t=t.replace('"a":d.get("simp") or "",','"a":alist,',1)
    # insert alias computation before dict build
    t=t.replace('"ch":d.get("chapter",""),' , '"ch":d.get("chapter",""),',1)
    anchor='IDX=[]'
    if anchor in t and 'def _alist' not in t:
        t=t.replace(anchor,'''def _alist(c,d):
    s=set()
    for k in ("simp","trad"):
        v=d.get(k) or ""
        if v and v!=c: s.add(v)
    for k in ("aliases",):
        for v in (d.get(k) or []): s.add(v)
    return sorted(x for x in s if x)
IDX=[]''',1)
    t=t.replace('for f in fs:','for f in fs:\n    pass',1) if False else t
    io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("builder patched")