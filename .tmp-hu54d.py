# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"謼":"h「豁活」取「豁」：張口大聲號叫，其聲豁然而出（推）。",
"嘑":"h「豁活」取「豁」：張口呼叫，氣豁然而出（推）。",
"歑":"h「豁活」取「豁」：張口呵氣，溫氣豁然敷於物（推）。",
"𢧶":"h「豁活」取「豁」：開口呼喚，聲豁然而達（推）。",
"𤹣":"h「豁活」取「活」：病初起，血氣尚活而乍動（推）。",
"嫭":"h「豁活」取「活」：容色鮮活明麗（推）。",
"㦆":"h「豁活」取「豁」：夸誕大言，口氣豁張（推）。",
"𨝘":"h「豁活」取「豁」：地名，取當地開豁平衍之狀（推）。",
"㙤":"x「续消」取「消」：土自裂開，形體消解（推）。",
"罅":"x「续消」取「消」：陶器燒成而自裂，裂紋延續而消解（推）。",
"滹":"h「豁活」取「豁」：水勢開豁漫流（推）。",
"摢":"h「豁活」取「豁」：堵住決口，使水不再豁開（推）。",
"㻯":"t「涂突」取「突」：玉名，照實記音（推）。",
"𥕕":"x「续消」取「消」：石裂紋延續而消解（推）。",
"𥲉":"h「豁活」取「豁」：竹籠開口，豁然而納物（推）。",
"𧗌":"h「豁活」取「活」：血污漫散，血色尚活（推）。",
"㯉":"ch「刺持」取「刺」：樹皮層層剝裂如刺，持之可為冠為燭（推）。"}
n=0
for ch,txt in M.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): print("miss",ch); continue
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="shengmu": s["text"]=txt
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("updated",n)