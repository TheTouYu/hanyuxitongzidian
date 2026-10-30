# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\㿣.json"
d=json.load(io.open(p,encoding="utf-8"))
d["pinyin"]="hé"; d["level"]=3; d["parent"]="曷"; d["bus"]=[{"num":4,"name":"匃"}]
sec=[]
for s in d["sections"]:
    if s["key"]=="benyi":
        s["text"]="《廣韻》：「白色。」意即乾枯之色。"
    if s["key"]=="shengmu":
        s["text"]="h「豁活」取「豁」：日曝水去，物色轉白而乾豁。"
    sec.append(s)
d["sections"]=sec
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")