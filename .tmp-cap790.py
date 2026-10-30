# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
b=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(b,encoding="utf-8").read()
if '"rl":' not in t:
    t=t.replace('"pr":','"rl":d.get("rootLevel") or 0,\n      "pr":',1)
    io.open(b,"w",encoding="utf-8",newline="\n").write(t)
old="if(t.lv===3&&t.pr){"
new="if(t.lv===3&&t.pr&&!t.rl){"
for f in (r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"):
    h=io.open(f,encoding="utf-8").read(); n=h.count(old); h=h.replace(old,new)
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],n)