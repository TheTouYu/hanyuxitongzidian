# -*- coding: utf-8 -*-
import io,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"; t=io.open(p,encoding="utf-8").read()
m=re.search(r"  for \(const s of \(d\.sections\|\|\[\]\)\.filter\(x=>x\.key===\"ziatt\"\)\)\{\n(?:.*\n){2}  \}\n", t)
assert m, "block not found"
block=m.group(0); t=t.replace(block,"",1)
anchor="try { const gi=glyphInfo(d.char);"
i=t.index(anchor); j=t.index("\n", t.index("catch(e){}", i))+1
t=t[:j]+block+t[j:]
io.open(p,"w",encoding="utf-8",newline="\n").write(t)
print("moved after glyph strip")