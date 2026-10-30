# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
cards={}
for f in os.listdir(C):
    if not f.endswith(".json") or f in ("index.json","variants.json"): continue
    try: cards[f[:-5]]=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
    except Exception: pass
added=0; miss=[]
for ch,d in cards.items():
    if d.get("level")!=3: continue
    par=d.get("parent")
    pd=cards.get(par)
    src=None
    if pd:
        for s in pd.get("sections",[]):
            if s.get("key")=="suoshujuan" or s.get("label") in ("所属卷","所屬卷"):
                src={"key":"suoshujuan","label":"所属卷"}
                if s.get("links"): src["links"]=s["links"]
                if s.get("text"): src["text"]=s["text"]
                break
    if not src: miss.append(ch); continue
    secs=d.setdefault("sections",[])
    if any(s.get("key")=="suoshujuan" or s.get("label") in ("所属卷","所屬卷") for s in secs): continue
    secs.append(src); added+=1
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("added",added,"no-parent-section",len(miss),miss[:8])