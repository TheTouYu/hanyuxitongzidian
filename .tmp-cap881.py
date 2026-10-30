# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
raw=open(r"D:\字谱智能体\汉字简体繁体对照表大全资料.txt","rb").read().decode("gb18030")
pairs=re.findall(r"([\u3400-\u9fff])=([\u3400-\u9fff])",raw)
f2s={}; s2f={}
for s,f in pairs:
    s2f.setdefault(s,f); f2s.setdefault(f,s)
print("对数",len(pairs),"繁",len(f2s),"简",len(s2f))
V=r"D:\系统汉字\web\public\variants.json"
v=json.load(io.open(V,encoding="utf-8"))
for f,s in f2s.items(): v[f]=s
json.dump(v,io.open(V,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("variants",len(v))
C=r"D:\系统汉字\web\public\cards"
n=0
for fn in os.listdir(C):
    if not fn.endswith(".json") or fn in ("index.json","variants.json"): continue
    p=os.path.join(C,fn); d=json.load(io.open(p,encoding="utf-8"))
    ch=d.get("char") or fn[:-5]
    al=set(d.get("aliases") or [])
    if ch in f2s: al.add(f2s[ch]); d["simp"]=f2s[ch]
    if ch in s2f: al.add(s2f[ch]); d.setdefault("trad",s2f[ch])
    for k in (d.get("simp"),d.get("trad")):
        if k and k in f2s: al.add(f2s[k])
        if k and k in s2f: al.add(s2f[k])
    al.discard(ch)
    if al!=set(d.get("aliases") or []):
        d["aliases"]=sorted(al); json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改卡",n)