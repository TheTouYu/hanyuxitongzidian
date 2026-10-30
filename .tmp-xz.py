# -*- coding: utf-8 -*-
import json,io,os,shutil,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
for ch in ("訢",):
    p=os.path.join(C,ch+".json")
    if os.path.exists(p): os.remove(p); print("removed card",ch)
    gd=os.path.join(G,ch)
    if os.path.isdir(gd): print("glyph dir exists",ch,os.listdir(gd))
    p2=os.path.join(G,"index.json"); gg=json.load(io.open(p2,encoding="utf-8"))
    if ch in gg["chars"]: gg["chars"].pop(ch); print("removed glyph entry",ch)
    json.dump({"chars":gg["chars"]},io.open(p2,"w",encoding="utf-8"),ensure_ascii=False)
# 确保 欣 的 aliases 含 訢
p=os.path.join(C,"欣.json"); d=json.load(io.open(p,encoding="utf-8"))
al=set(d.get("aliases") or []); al.add("訢"); d["aliases"]=sorted(al)
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("aliases",d["aliases"])