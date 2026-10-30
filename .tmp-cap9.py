# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\photos\captions.json"
cap=json.load(io.open(p,encoding="utf-8"))
cap["野"]=["《野合圖》（東漢畫像石）",""]
json.dump(cap,io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("ok")