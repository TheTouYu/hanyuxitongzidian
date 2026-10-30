import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
d=r"D:\系统汉字\web\public\glyphs\photos\霾"
for f in os.listdir(d): os.remove(os.path.join(d,f))
os.rmdir(d)
p=r"D:\系统汉字\web\public\glyphs\photos\index.json"
x=json.load(io.open(p,encoding="utf-8")); ph=x.get("photos") or x
ph.pop("霾",None); json.dump({"photos":ph},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("霾 图已删；野合图仍归 野:",ph.get("野"))