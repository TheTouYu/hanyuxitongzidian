# -*- coding: utf-8 -*-
import json,io,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
P=r"D:\系统汉字\web\public\cards\秭.json"
d=json.load(io.open(P,encoding="utf-8"))
d["head"]="𥞑（秭）"; d["aliases"]=["秭"]
d["sections"][0]["text"]=("𥞑（秭）zǐ《龍龕》：“將幾反。千億也。又𥞑㷌（歸），縣名。”《漢典》：“同秭。”\n"
 "秭（正體字），从禾市聲。")
json.dump(d,io.open(P,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(d["head"])