# -*- coding: utf-8 -*-
import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\server.mjs"; s=io.open(p,encoding="utf-8").read()
old="const lv=d.level===1?'一级字根':d.level===2?'二级字根':d.level===3?'谐声字':'';"
new="const lv=d.grade||(d.level===1?'一级字根':d.level===2?'二级字根':d.level===3?'谐声字':'');"
if old in s:
    s=s.replace(old,new); io.open(p,"w",encoding="utf-8",newline="").write(s); print("server patched")
else: print("server: pattern not found")
q=r"D:\系统汉字\web\public\cards\慮.json"; d=json.load(io.open(q,encoding="utf-8"))
d["grade"]="三级字根"; json.dump(d,io.open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1); print("慮 grade set")