# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\卷一雞.json"
d=json.load(io.open(p,encoding="utf-8"))
def fix(o):
    if isinstance(o,dict): return {k:fix(v) for k,v in o.items()}
    if isinstance(o,list): return [fix(x) for x in o]
    if isinstance(o,str): return o.replace("卷「5.欠部」：欠","5.欠部").replace("卷「5.欠部」：","5.欠部")
    return o
d=fix(d)
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")