# -*- coding: utf-8 -*-
import json,io,os,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
V=json.load(io.open(r"D:\系统汉字\web\public\cards\variants.json",encoding="utf-8"))
print(type(V), list(V.items())[:5] if isinstance(V,dict) else V[:3])