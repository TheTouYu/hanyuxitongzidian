# -*- coding: utf-8 -*-
import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
old="""${esc(d.cname||ch)}${(d.simp&&!d.cname)?`（${esc(d.simp)}）`:''}"""
new="""${d.chapterCard?('<a href="javascript:void(0)" class="chp" onclick="goCard(\\''+d.chapterCard+'\\')">第'+(d.chapter||'')+'章 '+esc(d.chapterName||'')+'</a>'):esc(d.cname||ch)}${(d.bus&&d.bus[0]&&(d.bus[0].name||'').indexOf('卷')===0)?(' · '+esc(d.cname||ch)):''}${(d.simp&&!d.cname)?`（${esc(d.simp)}）`:''}"""
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if old in h:
        h=h.replace(old,new,1); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"title ok")
    else: print("MISS",f)