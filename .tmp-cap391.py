import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
p=P+r"\index.json"; x=json.load(io.open(p,encoding="utf-8")); k="photos" if "photos" in x else None
(x[k] if k else x)["啇"]=["01.png"]
io.open(p,"w",encoding="utf-8").write(json.dumps(x,ensure_ascii=False,indent=1))
print("ok")