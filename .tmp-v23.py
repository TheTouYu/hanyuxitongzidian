# -*- coding: utf-8 -*-
import io,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
HE="""b.num===0?(function(){var L='第'+(d.chapter||'一')+'章'+(d.chapterName?' '+esc(d.chapterName):'');return (d.chapterCard?('<a href="javascript:void(0)" class="chp" onclick="goCard(\\''+d.chapterCard+'\\')">'+L+'</a>'):L)+((b.name||'').indexOf('卷')===0?' · '+esc(b.name):'');}()):('第'+String(b.num||'?')+'部 '+esc(b.name||''))}"""
LI="""x.ch?(function(){var L='第'+x.ch+'章'+(x.cn?' '+x.cn:'');return (x.cc?('<a href="javascript:void(0)" class="chp" onclick="goCard(\\''+x.cc+'\\')">'+L+'</a>'):L);}()):('第'+(x.b||'?')+'部')} ${x.ch?'':(x.n||'')}"""
for f in [r"D:\系统汉字\web\public\test.html",r"D:\系统汉字\web\public\index.html"]:
    h=io.open(f,encoding="utf-8").read()
    a=re.sub(r"b\.num===0\?[\s\S]*?部 '\+esc\(b\.name\|\|''\)\)\}", lambda m:HE, h, count=1)
    b=re.sub(r"x\.ch\?\(x\.cc\?[\s\S]*?部'\)\} \$\{x\.n\|\|''\}", lambda m:LI, a, count=1)
    ok = (b!=h)
    io.open(f,"w",encoding="utf-8",newline="\n").write(b); print(f.split("\\")[-1], "patched", ok, "HELLO" if HE in b else "he?")