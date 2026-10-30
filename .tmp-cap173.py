import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
V=json.load(io.open(r"D:\系统汉字\web\public\cards\variants.json",encoding="utf-8"))
print(type(V), list(V)[:3] if isinstance(V,dict) else V[:3])
k=list(V)[0] if isinstance(V,dict) else None
print(k, type(V[k]) if k else None, (V[k] if k else None) if isinstance(V,dict) else None)