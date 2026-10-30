# -*- coding: utf-8 -*-
import re,json,sys,glob,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
b=open(r"D:\字谱智能体\汉字简体繁体对照表大全资料.doc","rb").read()
t=b.decode("utf-16-le","ignore")
i=t.find("繁简汉字对照表"); seg=t[i:]
runs=re.findall(r"[\u3400-\u9fff]+",seg)
s="".join(runs[1:]) if len(runs)>1 else ""
pairs=[]
for k in range(0,len(s)-1,2):
    a,bb=s[k],s[k+1]
    if a!=bb: pairs.append((a,bb))
s2t={}; t2s={}
for a,bb in pairs:
    s2t.setdefault(a,[]); 
    if bb not in s2t[a]: s2t[a].append(bb)
    t2s.setdefault(bb,a)
print("pairs",len(pairs),"simp",len(s2t),"trad",len(t2s))
json.dump(s2t,open(r"D:\系统汉字\web\public\cards\variants.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
C=r"D:\系统汉字\web\public\cards"; n=0; miss=[]
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    try: d=json.load(open(f,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    ch=d.get("char") or ""
    if ch in t2s and not d.get("simp"):
        d["simp"]=t2s[ch]; json.dump(d,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cards 补 simp",n)