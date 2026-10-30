# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"
lines=io.open(p,encoding="utf-8").read().split("\n")
i=next(k for k,l in enumerate(lines) if 'filter(x=>x.key==="ziatt")' in l)
block=lines[i:i+3]
assert 'ziatt' in "".join(block)
del lines[i:i+3]
j=next(k for k,l in enumerate(lines) if "try { const gi=glyphInfo(d.char);" in l)
lines[j+1:j+1]=block
io.open(p,"w",encoding="utf-8",newline="\n").write("\n".join(lines))
print("moved",block[0].strip()[:40])