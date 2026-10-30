# -*- coding: utf-8 -*-
import json,io,os,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for p in glob.glob(r"D:\系统汉字\web\public\**\variants.json",recursive=True):
    v=json.load(io.open(p,encoding="utf-8"))
    print(p,"条",len(v))
    for k in ("薹","擡"):
        print(" ",k,"→",v.get(k))