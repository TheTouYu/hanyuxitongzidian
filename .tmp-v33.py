# -*- coding: utf-8 -*-
import io,json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\卷一雞.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        g=s["groups"][0]
        print("rows before:",g["rows"][:2],len(g["rows"][0]))
        g["title"]="卷一「雞」所辖七部"; g["header"]=["部号","部首","所辖"]
        # 行统一三列：部号/部首/所辖，并给部首做卡链接
        rows=[]; links=[]
        for r in g["rows"]:
            r=list(r)
            if len(r)>=3: rows.append([r[0],r[1],r[2]])
            elif len(r)==2: rows.append([r[0],r[1],""])
            else: rows.append([r[0],"",""])
        g["rows"]=rows
        g["links"]=[("" if c=="" else c) for c in [r[1] for r in rows]]
        g["links"]=["只","奚","旨","匃","欠","乞","桀"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("卷卡部目表：三列 部号/部首/所辖，部首可点")