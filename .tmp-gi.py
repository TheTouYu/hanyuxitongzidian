# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
chars=ix.get("chars") or ix
print("雁 files:",len((chars.get("雁") or {}).get("files",[])), "鴈 files:",len((chars.get("鴈") or {}).get("files",[])))
print("雁 sample:",(chars.get("雁") or {}).get("files",[])[:3])
print("鴈 sample:",(chars.get("鴈") or {}).get("files",[])[:3])