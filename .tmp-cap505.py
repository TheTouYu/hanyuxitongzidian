# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
miss=[];short=[];noform=[];generic=[]
pat=re.compile(r"取「[^」]+」")
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn=="index.json": continue
    d=json.load(io.open(os.path.join(C,fn),encoding="utf-8"))
    if d.get("level")==0 or d.get("chapter") or d.get("hidden"): continue
    sm=[s for s in d.get("sections") or [] if s.get("key")=="shengmu"]
    ch=fn[:-5]
    if not sm: miss.append(ch); continue
    t=(sm[0].get("text") or "").strip()
    if len(t)<8: short.append((ch,t)); continue
    if "零聲母" in t or "零声母" in t: continue
    if not pat.search(t): noform.append((ch,t))
    elif "推" not in t and "照實" not in t: generic.append((ch,t))
print("缺声母栏",len(miss),miss[:10])
print("过短",len(short),short[:5])
print("无取面式",len(noform))
for x in noform[:8]: print("  ",x)
print("无推/照实",len(generic))
for x in generic[:5]: print("  ",x)