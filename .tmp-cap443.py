# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from PIL import Image
p=r"D:\系统汉字\web\public\glyphs\photos\屐\01.jpg"
im=Image.open(p); im.thumbnail((1400,1400)); im.convert("RGB").save(p,quality=85)
print("resized",os.path.getsize(p))
C=r"D:\系统汉字\web\public\cards"
V=json.load(io.open(C+r"\variants.json",encoding="utf-8")); inv={}
for s,ts in V.items():
    for t in ts: inv.setdefault(t,[]).append(s)
n=0
for ch in ["支"]+[x[:-5] for x in os.listdir(C) if x.endswith(".json") and x!="index.json"]:
    fp=os.path.join(C,ch+".json")
    d=json.load(io.open(fp,encoding="utf-8"))
    if d.get("bus",[{}])[0].get("num")!=13: continue
    h=d.get("head") or ""
    al=set(d.get("aliases") or [])
    m=re.search(r"（(.+?)）",h)
    if m: al.update(list(m.group(1)))
    simp=None
    for a in list(al):
        if a in V and ch in V[a]: simp=a
    if ch in inv: simp=inv[ch][0]; al.update(inv[ch])
    if simp: d["simp"]=simp
    d["aliases"]=sorted(al)
    json.dump(d,io.open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("支部补齐别名",n)