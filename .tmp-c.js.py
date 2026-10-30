# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\test.html"
t=io.open(p,encoding="utf-8").read()
old="const exact=IDX.filter(x=>x.c===q||((x.a||[]).includes(q)))"
new="const exact=IDX.filter(x=>x.c===q||((x.a||[]).includes(q))||((x.v||[]).includes(q)))"
n=t.count(old)
if n: t=t.replace(old,new)
old2="||((x.a||[]).some(t=>norm(t).includes(q)))"
new2="||((x.a||[]).some(t=>norm(t).includes(q)))||((x.v||[]).some(t=>norm(t).includes(q)))"
n2=t.count(old2)
if n2: t=t.replace(old2,new2)
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
# 同步 index.html
p2=r"D:\系统汉字\web\public\index.html"
t2=io.open(p2,encoding="utf-8").read(); t2=t2.replace(old,new).replace(old2,new2)
io.open(p2,"w",encoding="utf-8",newline="\n").write(t2)
print("patched",n,n2)