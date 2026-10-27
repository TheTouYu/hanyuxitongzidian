# -*- coding: utf-8 -*-
import json,io,os,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
ph=json.load(io.open(P+r"\index.json",encoding="utf-8")); ph=ph.get("photos") or ph
cp=json.load(io.open(P+r"\captions.json",encoding="utf-8")); cp=cp.get("captions") or cp
no_cap=[c for c in ph if not (cp.get(c) or [])]
empty=[(c,i) for c in ph for i,v in enumerate(cp.get(c) or []) if not str(v).strip()]
print("有图字",len(ph),"无图注",len(no_cap),"空图注",len(empty))
print("示例无图注:",no_cap[:8])
print("示:",cp.get("示"))