# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(C+r"\夷.json",encoding="utf-8"))
rows={}
for s in d["sections"]:
    if s["key"]=="zizu":
        for g in s["groups"]:
            for r in g["rows"]: rows[r[0].split("（")[0]]=r
SM={c:"y「零聲母」不系：零聲母，緒論七組未列（照實）。" for c in ["姨","蛦","咦","痍","恞","跠","䧅","羠","侇","桋","眱"]}
SM.update({"荑":"t「涂突」取「突」：茅芽破土而突（推）。","洟":"t「涂突」取「涂」：涕液塗面（推）。","鴺":"t「涂突」取「突」：鵜入水突捕魚（推）。","鮧":"t「涂突」取「涂」：鮎體滑塗（推）。","銕":"t「涂突」取「涂」：黑金鎔而塗範（推）。"})
fix=0
for ch,row in rows.items():
    p=os.path.join(C,ch+".json"); c=json.load(io.open(p,encoding="utf-8"))
    changed=False
    if c.get("parent")!="夷" or c.get("level")!=3: c["parent"]="夷"; c["level"]=3; changed=True
    c["bus"]=[{"num":27,"name":"夷"}]
    secs=[{"key":"shiyi","label":"释义","text":row[3],"cites":[]},
          {"key":"shengmu","label":"声母拟态","text":SM.get(ch,""),"cites":[]},
          {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]
    c["sections"]=secs; c["head"]=row[0]
    json.dump(c,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fix+=1
print("统一",fix)