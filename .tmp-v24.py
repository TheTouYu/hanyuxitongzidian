# -*- coding: utf-8 -*-
import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    m=re.search(r"\.ch\{[^}]*\}",h)
    print(f.split("\\")[-1], m.group(0) if m else "no .ch")
    n=h.replace("+((b.name||'').indexOf('卷')===0?' · '+esc(b.name):'')","",1)
    if m:
        cur=m.group(0)
        new=re.sub(r"font-size:\s*\d+(\.\d+)?px","font-size:26px",cur)
        n=n.replace(cur,new,1)
    io.open(f,"w",encoding="utf-8",newline="\n").write(n)
print("ok")