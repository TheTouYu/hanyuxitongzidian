# -*- coding: utf-8 -*-
import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=rf"{C}\卷一雞.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="juan":
        s["links"]=[l for l in s.get("links",[]) if l.get("ch")!="第一章士"]
d["chapterCard"]="第一章士"
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 索引加 cc
bp=r"D:\系统汉字\.tmp-rel2.py"; t=io.open(bp,encoding="utf-8").read()
if '"cc":' not in t:
    t=t.replace('"ch":d.get("chapter"),','"ch":d.get("chapter"),"cc":d.get("chapterCard",""),',1)
    io.open(bp,"w",encoding="utf-8",newline="\n").write(t); print("builder cc")
# 渲染器：头部章号可点
o_head="""${esc(b.num===0?('第'+(d.chapter||'一')+'章'):('第'+String(b.num||'?')+'部'))}"""
n_head="""${b.num===0?(d.chapterCard?('<a href="javascript:void(0)" class="chp" onclick="goCard(\\''+d.chapterCard+'\\')">第'+(d.chapter||'一')+'章</a>'):('第'+(d.chapter||'一')+'章')):('第'+String(b.num||'?')+'部')}"""
o_list="""${x.ch?('第'+x.ch+'章'):('第'+(x.b||'?')+'部')}"""
n_list="""${x.ch?(x.cc?('<a href="javascript:void(0)" class="chp" onclick="goCard(\\''+x.cc+'\\')">第'+x.ch+'章</a>'):('第'+x.ch+'章')):('第'+(x.b||'?')+'部')}"""
for f in [r"D:\系统汉字\web\public\test.html", r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read(); n=0
    if o_head in h: h=h.replace(o_head,n_head,1); n+=1
    if o_list in h: h=h.replace(o_list,n_list,1); n+=1
    io.open(f,"w",encoding="utf-8",newline="\n").write(h); print(f.split("\\")[-1],"patched",n)