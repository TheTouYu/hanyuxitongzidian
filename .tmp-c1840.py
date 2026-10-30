# -*- coding: utf-8 -*-
import json,io,os,sys,hashlib,subprocess,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
by=z["byName"].get("己"); print("己:",by)
# 恢复被删图
out=subprocess.run([r"D:\系统汉字\tools\git.cmd","show","cb0f1b217^:web/public/glyphs/photos/配/01.jpg"],capture_output=True)
b=out.stdout
print("recovered",len(b), b[:3])
h=hashlib.sha1(b).hexdigest(); print("sha1",h[:12])
json.dump({"sha1":h,"len":len(b)},io.open(r"D:\系统汉字\.tmp-jibao.json","w"),ensure_ascii=False)
open(r"D:\系统汉字\.tmp-jibao.jpg","wb").write(b)