# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="const show=sibs.slice(0,24);fam='　同族　'+show.map(ln).join('')+(sibs.length>show.length?'…':'');"
new="fam='　同族　'+sibs.map(ln).join('');"
for f in (r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"):
    t=io.open(f,encoding="utf-8").read(); n=t.count(old)
    if n: io.open(f,"w",encoding="utf-8",newline="\n").write(t.replace(old,new))
    print(f.split("\\")[-1],n)