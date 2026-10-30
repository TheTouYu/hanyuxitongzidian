# -*- coding: utf-8 -*-
import io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
D=r"D:\系统汉字\web\public"
old="<h4>'+esc(g.title)+'</h4>"
new="<h4>'+esc(g.no||'')+esc(g.title)+'</h4>"
for fn in os.listdir(D):
    if not fn.endswith(".html"): continue
    p=os.path.join(D,fn); t=io.open(p,encoding="utf-8").read()
    if old in t:
        io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new))
        print("patched",fn)