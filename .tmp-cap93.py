# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\glyphs\index.json"
ix=json.load(io.open(p,encoding="utf-8"))
print("chars",len(ix.get("chars",{})))
e=ix["chars"].get("䒬")
print("before",e and len(e.get("files",[])))
if e:
    e["files"]=[]; e.pop("alias",None)
json.dump(ix,io.open(p,"w",encoding="utf-8",newline="\n"),ensure_ascii=True)
print("written")