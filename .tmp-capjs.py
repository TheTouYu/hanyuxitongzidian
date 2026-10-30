# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public"
cap=json.load(io.open(os.path.join(P,"glyphs","photos","captions.json"),encoding="utf-8")).get("captions") or {}
idx=json.load(io.open(os.path.join(P,"glyphs","photos","index.json"),encoding="utf-8")).get("photos") or {}
lines=["window.CAPS={"]
for k,v in cap.items():
    lines.append(" %s:%s,"%(json.dumps(k,ensure_ascii=False),json.dumps(v,ensure_ascii=False)))
lines.append("};")
io.open(os.path.join(P,"captions.js"),"w",encoding="utf-8",newline="\n").write("\n".join(lines))
lines=["window.PHOTO={"]
for k,v in idx.items():
    lines.append(" %s:%s,"%(json.dumps(k,ensure_ascii=False),json.dumps(v,ensure_ascii=False)))
lines.append("};")
io.open(os.path.join(P,"photos.js"),"w",encoding="utf-8",newline="\n").write("\n".join(lines))
print("captions",len(cap),"photos",len(idx))