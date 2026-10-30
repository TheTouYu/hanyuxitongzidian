# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\鮛.json"
d=json.load(io.open(p,encoding="utf-8"))
t="鮛（鮛）shū《集韻》：“魚名。王鮪也，小者曰鮛。或省不。”《爾雅·釋魚》注：“鮪，鱘屬也。大者名王鮪，小者名鮛鮪。”小鱘魚。應該是指鱘魚卵，黑圓如豆粒。可加工為魚子醬。"
for s in d["sections"]:
    if s["key"]=="shiyi": s["text"]=t
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("鮛 全文已补")