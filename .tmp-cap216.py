# -*- coding: utf-8 -*-
import io,glob,os,json,sys,collections
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
if "除零聲母外" not in t:
    t=t.rstrip()+"\n- **除零聲母外，每一字都必須有聲母擬態推導**：借聲、名物記音之字同樣要寫（以聲母摹其音／物），只有零聲母者寫「不系（照實）」。\n"
    io.open(p,"w",encoding="utf-8",newline="\n").write(t)
C=r"D:\系统汉字\web\public\cards"; miss=[]
for f in glob.glob(C+r"\*.json"):
    if os.path.basename(f) in ("index.json","variants.json"): continue
    d=json.load(io.open(f,encoding="utf-8"))
    bus=d.get("bus") or []
    num=bus[0].get("num") if bus and isinstance(bus[0],dict) else None
    if not isinstance(num,int) or not(1<=num<=10): continue
    if not any(s.get("key")=="shengmu" for s in d["sections"]): miss.append(d["char"])
print("部1-10 缺声母栏",len(miss),miss[:10])