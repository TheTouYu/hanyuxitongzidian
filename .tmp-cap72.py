# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
src=json.load(io.open(rf"{C}\示.json",encoding="utf-8"))
made=[];skipped=[]
for s in src["sections"]:
    for g in (s.get("groups") or []):
        for r in g["rows"]:
            raw=r[0]; m=re.match(r"^([^（(]+)[（(]([^）)]*)[）)]$",raw)
            ch=m.group(1) if m else raw; al=[c for c in (m.group(2) if m else "") if c.strip()]
            if not ch or os.path.exists(rf"{C}\{ch}.json"): skipped.append(ch); continue
            d={"char":ch,"trad":ch,"simp":"","pinyin":r[1],"level":3,"parent":"示","bus":[{"num":10,"name":"示"}],
               "aliases":al+sorted(set(x for x in al)),
               "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]}]}
            if al: d["head"]=raw
            json.dump(d,io.open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1); made.append(ch)
print("新建",len(made),made,"已有",len(skipped))