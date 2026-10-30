# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
NOTE={"氏":"「氏」即「㠯」從人，沒有省去人形而已，與㠯同字，故亦為一級字根。",
      "了":"「了」即「巳」（「㠯」之倒寫）之變，指男陰；與㠯同字，故亦為一級字根。",
      "巳":"「巳」即「㠯」的倒寫，象陰莖疲軟下垂之狀；與㠯同字，故亦為一級字根。"}
for ch,note in NOTE.items():
    p=rf"{C}\{ch}.json"; d=json.load(io.open(p,encoding="utf-8"))
    d["level"]=1; d["parent"]=""
    done=False
    for s in d["sections"]:
        if s.get("key")=="benyi":
            t=s.get("text") or ""
            if "一級字根" not in t: s["text"]=t+"　辨析："+note
            done=True
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print(ch,"level1",done)
y=json.load(io.open(rf"{C}\㠯.json",encoding="utf-8"))
for s in y["sections"]:
    if s.get("key")=="zizu":
        for g in s["groups"]:
            if g.get("title","").startswith("本部二級字根"):
                g["rows"]=[r for r in g["rows"] if str(r[0]) not in ("氏","了","巳","厶")]
                g["title"]="本部二級字根（各見其卡；氏、了、巳、厶為㠯之異體，已升一級字根）"
json.dump(y,io.open(rf"{C}\㠯.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("㠯 rows now",[ [r[0] for r in g["rows"]] for g in [x for x in y["sections"] if x.get("key")=="zizu"][0]["groups"]][-1])