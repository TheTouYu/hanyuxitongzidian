import os,sys,io,json
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
for c in ("薙","雉"):
    d=rf"D:\系统汉字\web\public\glyphs\photos\{c}"
    print(c, os.path.isdir(d) and sorted(os.listdir(d)))
capj=json.load(io.open(r"D:\系统汉字\web\public\glyphs\photos\captions.json",encoding="utf-8"))
print({k:capj.get("captions",capj).get(k) for k in ("薙","雉")})