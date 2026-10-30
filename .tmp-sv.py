# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"
t=io.open(p,encoding="utf-8").read()
old="    if (d.parent) {"
new="    const _hasZigen=(d.sections||[]).some(x=>x.key==='zigen'||String(x.label||'').startsWith('字根「'));\n    if (d.parent && !_hasZigen) {"
assert old in t
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched")