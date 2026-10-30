# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public"
cap=json.load(io.open(os.path.join(P,"glyphs","photos","captions.json"),encoding="utf-8"))
cap=cap.get("captions") or cap
cap["戹"]=["負軛的銅車牛（南北朝）"]
cap["厄"]=cap["戹"]
json.dump({"captions":cap},io.open(os.path.join(P,"glyphs","photos","captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
js=os.path.join(P,"captions.js"); t=io.open(js,encoding="utf-8").read()
m=re.match(r"^[\s\S]*?window\.CAPS\s*=\s*",t)
prefix=m.group(0) if m else "window.CAPS="
io.open(js,"w",encoding="utf-8").write(prefix+json.dumps(cap,ensure_ascii=False)+";\n")
print("caps",len(cap))