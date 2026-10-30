# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
v=json.load(io.open(os.path.join(C,"variants.json"),encoding="utf-8"))
for k in ("薹","擡","臺","檯","韡"):
    print(k,"→",v.get(k))
print("苔有卡",os.path.exists(os.path.join(C,"苔.json")),"薹→苔",os.path.exists(os.path.join(C,"薹.json")))