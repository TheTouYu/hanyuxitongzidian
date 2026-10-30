import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
for name,key in (("index.json","photos"),("captions.json","captions")):
    p=P+"\\"+name; d=json.load(io.open(p,encoding="utf-8")); m=d.get(key) or d
    m.pop("兮",None); json.dump({key:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("ok")