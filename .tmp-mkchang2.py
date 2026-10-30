# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
BEN=("甲骨文本與“石”同源，象懸崖形。上面突出呈棚狀。西周金文添加聲符“干”，義即下面象干一樣陡直，上面則橫而斜出。"
"hǎn，《說文》：“山石之厓巗，人可居，象形。凡厂之屬皆从厂。，籀文从干。呼旱切。”")
p=os.path.join(C,"厂.json"); d=json.load(io.open(p,encoding="utf-8"))
d["sections"][0]["text"]=BEN
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
ZERO="y「零聲母」不系：零聲母，緒論七組未列（照實）。"
rows=json.load(io.open(r"D:\系统汉字\.tmp-changrows.json",encoding="utf-8"))
fam=[("228","厓"),("229","崖"),("230","涯"),("231","睚"),("232","屵"),("233","娾"),("234","厊"),("235","广"),("236","𠆲"),("237","𢇘"),("238","㚧"),("239","𢇞"),("241","㷳"),("242","贗"),("243","鴈（雁）")]
n=0
for k,ch in fam:
    d={"char":ch,"head":ch,"pinyin":"","level":3,"parent":"厂","bus":["35"],
       "sections":[{"key":"shiyi","label":"释义","text":rows[k]},{"key":"shengmu","label":"声母拟态","text":ZERO}]}
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("fam",n)