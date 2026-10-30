# -*- coding: utf-8 -*-
import json,io,glob,os,sys,collections
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
cnt=collections.Counter(); n=0
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    if (d.get("parent") or "") not in ("台","矣"): continue
    sm=[s for s in d["sections"] if s.get("key")=="shengmu"]
    if not sm or "㠯部聲母為零" not in sm[0]["text"]: continue
    cnt[d["parent"]]+=1
    if d["parent"]=="台":
        sm[0]["text"]="台多讀（yí／tái／sì），聲母不系（照實）。"
    else:
        sm[0]["text"]="聲符矣為零聲母（yǐ），緒論七組未列，不系（照實）。"
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print(cnt,"改",n)