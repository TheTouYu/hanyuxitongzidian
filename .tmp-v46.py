# -*- coding: utf-8 -*-
import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
pat=re.compile(r"b\.num===0\?\(function\(\)\{var L=.*?return \(d\.chapterCard\?.*?\):\(L\);\}\(\)\):")
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    n=pat.sub("d.chapterCard?'':",h,count=1)
    io.open(f,"w",encoding="utf-8",newline="\n").write(n)
    print(f.split("\\")[-1],"dup removed:", n!=h)