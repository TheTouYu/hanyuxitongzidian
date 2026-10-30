import json,io,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\glyphs\photos"
for n in ("index.json","captions.json"):
    d=json.load(io.open(os.path.join(P,n),encoding="utf-8"))
    k=list(d.keys())[0]; print(n,k,len(d[k]))