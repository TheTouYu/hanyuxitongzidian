# -*- coding: utf-8 -*-
import json,io,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for f in glob.glob(r"D:\系统汉字\web\public\cards\*.json"):
    if f.endswith("index.json"): continue
    try: d=json.load(io.open(f,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict) or d.get("level")!=2: continue
    ks=[s.get("key") for s in d.get("sections",[])]
    if "zizu" not in ks: print(d.get("char"), d.get("parent"), [s.get("label") for s in d.get("sections",[])])