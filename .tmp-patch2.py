# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(p,encoding="utf-8").read()
t=t.replace('"a":d.get("simp",""),','"a":_alist(d.get("trad") or d.get("char",""),d),',1)
if "def _alist" not in t:
    t=t.replace("IDX=[]",'''def _alist(c,d):
    s=set()
    for k in ("simp","trad"):
        v=d.get(k) or ""
        if v and v!=c: s.add(v)
    for v in (d.get("aliases") or []): s.add(v)
    return sorted(x for x in s if x)
IDX=[]''',1)
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read()
    h2=h.replace('x.a===q','((x.a||[]).includes(q))').replace('x.a.includes(q)','((x.a||[]).includes(q))')
    if h2!=h: io.open(f,"w",encoding="utf-8",newline="\n").write(h2); print("html patched",f.split("\\")[-1])
print("ok")