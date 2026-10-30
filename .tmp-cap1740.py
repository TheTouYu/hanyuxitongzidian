import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
G=r"D:\系统汉字\web\public\glyphs"
j=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); ch=j.get("chars") or j
for k in ("卽","卩","ㄗ","肥"):
    v=ch.get(k)
    print(k, (v.get("files")[:3] if isinstance(v,dict) and v.get("files") else v), os.path.isdir(os.path.join(G,k)))