# -*- coding: utf-8 -*-
import sys,os,json,io,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"; PH=os.path.join(ROOT,"web","public","glyphs","photos"); TMP=os.path.join(ROOT,".tmp-photos-new")
B=json.load(io.open(os.path.join(ROOT,".tmp-photoB.json"),encoding="utf-8"))
OWN=B["owners"]; CAPS=B["caps"]
IDX=json.load(io.open(os.path.join(PH,"index.json"),encoding="utf-8")); OLD=IDX.get("photos") or IDX
CAPD=json.load(io.open(os.path.join(PH,"captions.json"),encoding="utf-8")); CAP=CAPD.get("captions") or CAPD
rep=add=0
for ch in OWN:
    d=os.path.join(TMP,ch)
    if not os.path.isdir(d): continue
    files=sorted(f for f in os.listdir(d) if not f.endswith(".emf"))
    if not files: continue
    dst=os.path.join(PH,ch); os.makedirs(dst,exist_ok=True)
    had=bool(OLD.get(ch))
    for f in os.listdir(dst): os.remove(os.path.join(dst,f))
    for f in files: shutil.copyfile(os.path.join(d,f),os.path.join(dst,f))
    OLD[ch]=files
    if CAPS.get(ch): CAP[ch]=CAPS[ch][:len(files)]
    if had: rep+=1
    else: add+=1
json.dump({"photos":OLD},io.open(os.path.join(PH,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
json.dump({"captions":CAP},io.open(os.path.join(PH,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("替换",rep,"新增",add,"总字头",len(OLD),"有图",len([1 for v in OLD.values() if v]))
for c in ("帝","蒂","示","市","款","柰","祟","啇"):
    print(" ",c,OLD.get(c),(CAP.get(c) or [None])[0])