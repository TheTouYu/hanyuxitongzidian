# -*- coding: utf-8 -*-
import json,io,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; P=os.path.join(C,"秭.json")
d=json.load(io.open(P,encoding="utf-8"))
d["head"]="秭（𥞑）"; d["aliases"]=["𥞑"]; d["trad"]="秭"
B=("𥞑（秭）zǐ《龍龕》：“將幾反。千億也。又𥞑㷌（歸），縣名。”《漢典》：“同秭。”\n"
   "秭，从禾市聲（正體字；𥞑為異體）。")
d["sections"]=[{"key":"benyi","label":"释义","text":B,"cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"z「凿总」取「总」：秭為數名（千億），總聚之數（推）。","cites":[]}]
json.dump(d,io.open(P,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")