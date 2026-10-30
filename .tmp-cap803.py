# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\臺.json"; d=json.load(io.open(p,encoding="utf-8"))
d["head"]="臺（台坮㙵䑓㙜𡋛𦤼𡌫𡎲𡐉𡔼𡌬）"
d["aliases"]=["台","坮","㙵","䑓","㙜","𡋛","𦤼","𡌫","𡎲","𡐉","𡔼","𡌬"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("aliases",len(d["aliases"]))