# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def ishan(c): return len(c)==1 and ("\u3400"<=c<="\u9fff" or "\U00020000"<=c<="\U0002FA1F")
bad=[]
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    try: d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    except: continue
    ch=d.get("char") or fn[:-5]; head=d.get("head") or ""
    m=re.search(r"[（(]([^）)]*)[）)]",head)
    if not m: continue
    need={c for c in m.group(1) if ishan(c) and c!=ch}
    if need-set(d.get("aliases") or []): bad.append((ch,sorted(need-set(d.get("aliases") or []))))
print("仍缺",len(bad),bad[:5])