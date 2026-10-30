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
    for x in j["bu"]: no2juan[x["no"]]=(nm,j["name"])
n=0;miss=0
for f in glob.glob(C+r"\*.json"):
    b=f.split("\\")[-1]
    if b.startswith("卷") or b in ("index.json","variants.json"): continue
    try: d=json.load(io.open(f,encoding="utf-8"))
    except Exception: continue
    bus=(d.get("bus") or [{}])[0]; num=bus.get("num")
    j=no2juan.get(num)
    if not j: miss+=1; continue
    nm,jn=j; ch=False
    for s in d.get("sections",[]):
        if s.get("label")=="所属卷":
            s["text"]=""; s["links"]=[{"ch":nm,"label":nm}]; ch=True; break
    else:
        d.setdefault("sections",[]).append({"key":"suoshu","label":"所属卷","text":"","links":[{"ch":nm,"label":nm}],"cites":[]}); ch=True
    if ch: json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("字卡所属卷改为卷链",n,"无部号",miss)
d=json.load(io.open(C+r"\奚.json",encoding="utf-8"))
print([ (s["label"],s.get("links")) for s in d["sections"][-2:] ])