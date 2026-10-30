# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"㥛":("j「聚决」取「决」","《說文》「疾也」——急速如決水，一往而不可止。"),
"㪆":("d「囤动」取「囤」","《廣韻》「隱也」——隱藏囤聚而不見。"),
"㭒":("s「失收」取「收」","《說文》「臿也」——鍬臿入土，收土而起。"),
"䀈":("q「亲缺」取「亲」","《說文》「視也」——目視所及，親近而察。"),
"㶼":("x「续消」取「续」","《玉篇》「炫也、熱也」——光熱相續而炫。"),
"㾂":("h「豁活」取「活」","《唐韻》「病也」——久病之人，求活而已。"),
}
n=0
for ch,(head,rest) in M.items():
    p=os.path.join(C,ch+".json"); d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="shengmu": s["text"]=head+"："+rest
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改",n)