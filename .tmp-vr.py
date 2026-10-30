# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
add={"国":["國"],"圆":["圓"],"园":["園"],"图":["圖"],"团":["團"],"因":["因"],"或":["或"]}
for p in (r"D:\系统汉字\web\public\cards\variants.json", r"D:\系统汉字\web\public\variants.json"):
    d=json.load(io.open(p,encoding="utf-8"))
    for k,v in add.items():
        if k not in d and any(True for _ in [0]): d[k]=v
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=0)
    print(p.split("\\")[-1],len(d))