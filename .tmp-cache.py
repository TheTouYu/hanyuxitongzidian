# -*- coding: utf-8 -*-
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for h in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    s=io.open(h,encoding="utf-8").read()
    s=s.replace("fetch('cards/index.json')","fetch('cards/index.json?v='+Date.now())")
    s=s.replace('fetch("cards/index.json")','fetch("cards/index.json?v="+Date.now())')
    io.open(h,"w",encoding="utf-8",newline="\n").write(s)
s=io.open(r"D:\系统汉字\web\server.mjs",encoding="utf-8").read()
s=s.replace("'cache-control': 'no-cache',","'cache-control': (extname(target).toLowerCase()==='.html'?'no-store':'no-cache'),",1)
io.open(r"D:\系统汉字\web\server.mjs","w",encoding="utf-8",newline="\n").write(s)
print("patched")