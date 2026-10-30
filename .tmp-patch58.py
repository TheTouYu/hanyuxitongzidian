# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"
s=io.open(p,encoding="utf-8").read()
old="((s.links||[]).map(l=>"
new="(((s.links&&s.links.length?s.links:(d.links||[]))).map(l=>"
if old in s:
    s=s.replace(old,new,1); io.open(p,"w",encoding="utf-8",newline="").write(s); print("patched")
else: print("not found")