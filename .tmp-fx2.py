# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\index.json"
x=json.load(io.open(p,encoding="utf-8"))
rows=x["cards"] if isinstance(x,dict) and "cards" in x else x
json.dump(rows,io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("array",len(rows))