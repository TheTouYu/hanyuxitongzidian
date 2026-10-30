# -*- coding: utf-8 -*-
import io,sys,os,subprocess,tempfile
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    n=h.count("esc(s.text)")
    h=h.replace("esc(s.text)","((s.text||'').indexOf('gscroll')>=0?s.text:esc(s.text))")
    io.open(f,"w",encoding="utf-8",newline="\n").write(h)
    print(os.path.basename(f),"repl",n)