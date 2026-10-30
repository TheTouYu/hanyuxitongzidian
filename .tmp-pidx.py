# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
p=os.path.join(P,"index.json"); d=json.load(io.open(p,encoding="utf-8")); m=d.get("photos") or d
m["砨"]=["01.png"]; json.dump({"photos":m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("set", m["砨"])