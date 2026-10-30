# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"
t=io.open(p,encoding="utf-8").read()
old="if (s.label==='所属卷') continue;"
new=("if (s.label==='所属卷'){ h+='<h3>所属卷</h3><p>'+((s.links||[]).map(l=>'<a href=\"/card/'+encodeURIComponent(l.ch)+'\">'+escH(l.label||l.ch)+'</a>').join(' · '))+'</p>'; continue; }")
assert old in t, "anchor missing"
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched")