# -*- coding: utf-8 -*-
import io,json,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
Z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
CN="零一二三四五六七八九十"
def cn(n):
    if n<=10: return CN[n]
    if n<20: return "十"+CN[n%10]
    if n<100: return CN[n//10]+"十"+(CN[n%10] if n%10 else "")
    return "一百"
no2juan={}
for j in Z["juan"]:
    nm="卷%s%s"%(cn(j["no"]),j["name"])
    for x in j["bu"]: no2juan[x["no"]]=nm
def num_of(d):
    b=d.get("bus")
    if isinstance(b,dict): b=[b]
    if not isinstance(b,list): return None
    for x in b:
        if isinstance(x,dict) and isinstance(x.get("num"),int): return x["num"]
        if isinstance(x,str) and x.isdigit(): return int(x)
    return None
n=0;miss=[]
for f in glob.glob(C+r"\*.json"):
    b=f.split("\\")[-1]
    if b.startswith("卷") or b in ("index.json","variants.json"): continue
    try: d=json.load(io.open(f,encoding="utf-8"))
    except Exception: continue
    nm=no2juan.get(num_of(d))
    if not nm: miss.append(b); continue
    ch=False
    for s in d.setdefault("sections",[]):
        if s.get("label")=="所属卷":
            s["text"]=""; s["links"]=[{"ch":nm,"label":nm}]; ch=True; break
    if not ch:
        d["sections"].append({"key":"suoshu","label":"所属卷","text":"","links":[{"ch":nm,"label":nm}],"cites":[]})
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改",n,"缺部号",len(miss),miss[:3])
print(json.load(io.open(C+r"\奚.json",encoding="utf-8"))["sections"][-1])