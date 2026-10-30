# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
ix=json.load(io.open(G+r"\index.json",encoding="utf-8"))
e=ix["chars"].get("祡")
print("index:",e)
p=G+r"\祡"
print("dir:",os.path.isdir(p), sorted(os.listdir(p))[:15] if os.path.isdir(p) else None)