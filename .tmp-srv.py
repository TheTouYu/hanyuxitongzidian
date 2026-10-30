# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"
t=io.open(p,encoding="utf-8").read()
old="const files = (e && Array.isArray(e.files) ? e.files : []).map((f) => '/glyphs/' + f.split('/').map(encodeURIComponent).join('/'));"
new="const files = (e && Array.isArray(e.files) ? e.files : []).map((f) => '/glyphs/' + (String(f).includes('/') ? String(f) : key + '/' + String(f)).split('/').map(encodeURIComponent).join('/'));"
assert old in t
io.open(p,"w",encoding="utf-8",newline="\n").write(t.replace(old,new,1))
print("patched server")