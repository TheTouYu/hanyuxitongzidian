# -*- coding: utf-8 -*-
import io,json,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=rf"{C}\第一章士.json"; d=json.load(io.open(p,encoding="utf-8"))
d["cname"]="第一章 士"; d.pop("simp",None)
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
q=rf"{C}\卷一雞.json"; a=json.load(io.open(q,encoding="utf-8"))
a["cname"]="卷一 雞 · 第一章 士"
json.dump(a,io.open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
old="${esc(ch)}${d.simp?`（${esc(d.simp)}）`:''}"
new="${esc(d.cname||ch)}${(d.simp&&!d.cname)?`（${esc(d.simp)}）`:''}"
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new,1); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"cname patched")
    else: print("MISS",f)