# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"; p=os.path.join(G,"index.json")
gi=json.load(io.open(p,encoding="utf-8"))
n=0
for ch,arr in (gi.get("photos") or {}).items():
    for it in arr:
        if isinstance(it,dict) and it.get("file") and not it["file"].startswith(("photos/","/")) and "/" not in it["file"]:
            it["file"]="photos/"+ch+"/"+it["file"]; n+=1
json.dump(gi,io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("prefixed",n)