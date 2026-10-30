# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
print("厄.json",os.path.exists(os.path.join(C,"厄.json")))
if os.path.exists(os.path.join(C,"厄.json")):
    os.remove(os.path.join(C,"厄.json"))
d=json.load(io.open(os.path.join(C,"戹.json"),encoding="utf-8"))
a=d.get("aliases") or []
if "厄" not in a: a.append("厄")
d["aliases"]=a
d["head"]="戹（厄𠨳𠂬𢀴𢨩𠂘𠨬𢨤）"
json.dump(d,io.open(os.path.join(C,"戹.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for vp in (os.path.join(C,"variants.json"), r"D:\系统汉字\web\public\variants.json"):
    v={}
    if os.path.exists(vp):
        try: v=json.load(io.open(vp,encoding="utf-8"))
        except Exception: v={}
    v["厄"]=["戹"]; v["戹"]=["厄"]
    json.dump(v,io.open(vp,"w",encoding="utf-8"),ensure_ascii=False)
print("done")