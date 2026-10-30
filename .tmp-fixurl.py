# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\index.html"
t=io.open(p,encoding="utf-8").read()
bad="captions.js?v=20261029bon?v='+Date.now()"
good="captions.js?v=20261029b'"
if bad in t:
    t=t.replace(bad,good); print("fixed captions url")
t=t.replace("encodeURI('glyphs/photos/'+d.char+'/'+f)","encodeURI('glyphs/photos/'+d.char+'/'+f)+'?v=20261029d'")
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
s=r"D:\系统汉字\web\server.mjs"
u=io.open(s,encoding="utf-8").read()
u=u.replace("encodeURIComponent(f)))","encodeURIComponent(f))+'?v=20261029d')")
io.open(s,"w",encoding="utf-8",newline="\n").write(u)
print("done")