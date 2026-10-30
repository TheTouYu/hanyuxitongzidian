# -*- coding: utf-8 -*-
import os,json,io,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
CM=json.load(io.open(r"D:\系统汉字\.tmp-charmap.json",encoding="utf-8"))
ORDER=["benyi","bengen","zhuanyi","bianzheng","yinyuan","shengmu","zixing","zizu","suoshujuan","suoshu","shiyi"]
n=add_s=add_c=0
for p in glob.glob(os.path.join(C,"*.json")):
    b=os.path.basename(p)
    if b=="index.json": continue
    d=json.load(io.open(p,encoding="utf-8")); ch=d.get("char") or b[:-5]
    if len(ch)>1: continue
    secs=list(d.get("sections") or []); bad=False
    if not secs:
        txt=((CM.get(ch) or {}).get("txt") or "").strip() or "（原稿未收释义）"
        secs=[{"key":"shiyi" if d.get("level",3)>=3 else "benyi","label":"释义" if d.get("level",3)>=3 else "本义","text":txt,"cites":[]}]
        add_c+=1; bad=True
    if not any(s.get("key") in ("suoshujuan","suoshu") for s in secs):
        bus=(d.get("bus") or [{}])[0].get("name") or ""
        secs.append({"key":"suoshujuan","label":"所属卷","text":"","cites":[]}); add_s+=1; bad=True
    new=sorted(secs,key=lambda s: ORDER.index(s["key"]) if s["key"] in ORDER else 99)
    if bad or new!=secs:
        d["sections"]=new
        json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("修卡",n,"补所属卷",add_s,"补内容",add_c)