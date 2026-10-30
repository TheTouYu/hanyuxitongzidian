# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\家.json"; d=json.load(io.open(p,encoding="utf-8"))
rows=[["𢜿","jià","心","《集韻》「居迓切，音嫁。心不安也」；若有所失之意"],
 ["嫁","jià","女","《說文》「女適人也。从女家聲」；女子結婚、出嫁。《廣韻》「家也。故婦人謂嫁曰歸」"],
 ["稼","jià","禾","《說文》「禾之秀實為稼，莖節為禾。一曰稼，家事也。一曰在野曰稼」；禾抽穗的樣子、種植五穀、田中的作物"],
 ["幏","jià","巾","《說文》「南郡蠻夷賨布。从巾家聲」；充當賦稅的布匹"],
 ["榢（架枷）","jià","木","《集韻》引《博雅》「杙也，所以舉物也。或作榢、架。亦書作枷」"],
 ["傢","xiàng、jiā","人","《漢典》：xiàng 同「像」（《龍龕》「舊藏作像」）；jiā 傢夥、傢伙——器具用具；指人或牲畜"]]
for s in d["sections"]:
    if s["key"]=="zizu": s["groups"][0]["rows"]=rows
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("rows now verbatim")