# -*- coding: utf-8 -*-
import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
for f,name in ((rf"{C}\卷一雞.json","卷一"),(rf"{C}\第一章士.json","士")):
    d=json.load(io.open(f,encoding="utf-8")); d["chapterName"]="士"
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
bp=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(bp,encoding="utf-8").read()
if '"cn":' not in t:
    t=t.replace('"cc":d.get("chapterCard",""),','"cc":d.get("chapterCard",""),"cn":d.get("chapterName",""),',1)
    io.open(bp,"w",encoding="utf-8",newline="\n").write(t); print("builder cn")
o="""${b.num===0?(d.chapterCard?('<a href="javascript:void(0)" class="chp" onclick="goCard(\\''+d.chapterCard+'\\')">第'+(d.chapter||'一')+'章</a>'):('第'+(d.chapter||'一')+'章')):('第'+String(b.num||'?')+'部')} ${esc(b.name||'')}"""
n="""${b.num===0?((d.chapterCard?('<a href="javascript:void(0)" class="chp" onclick="goCard(\\''+d.chapterCard+'\\')">第'+(d.chapter||'一')+'章</a>'):('第'+(d.chapter||'一')+'章'))+(d.chapterName?' '+esc(d.chapterName):'')+((b.name||'').indexOf('卷')===0?' · '+esc(b.name):'')):('第'+String(b.num||'?')+'部 '+esc(b.name||''))}"""
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    if o in h:
        h=h.replace(o,n,1); io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"header patched")
    else: print("MISS",f)