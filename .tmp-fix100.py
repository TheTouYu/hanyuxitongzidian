# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\index.html"
t=io.open(p,encoding="utf-8").read()
old="${zx}${LKR(s)}${(s.cites&&s.cites.length)?`<div class=\"cites\">"
new="${zx}${(s.gimgs||[]).map(f=>`<img class=\"gin\" src=\"glyphs/${encodeURI(f)}\" alt=\"参证字形\">`).join('')}${LKR(s)}${(s.cites&&s.cites.length)?`<div class=\"cites\">"
if old in t:
    t=t.replace(old,new,1); io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("patched(renderCard)")
else:
    print("pattern not found", old[:60])