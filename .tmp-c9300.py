# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
src=os.path.join(G,"戠","13.png")
if os.path.exists(src):
    d=os.path.join(G,"熾"); os.makedirs(d,exist_ok=True)
    os.replace(src,os.path.join(d,"02.png"))
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chars=idx.get("chars") or idx
chars["戠"]["files"]=[f for f in chars["戠"]["files"] if f!="13.png"]
fh=chars.get("熾") or {}; files=[f for f in (fh.get("files") or []) if f!="02.png"]+["02.png"]
fh["files"]=sorted(set(files), key=lambda x:int(x.split(".")[0])); chars["熾"]=fh
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("戠",len(chars["戠"]["files"]),"熾",chars["熾"]["files"])