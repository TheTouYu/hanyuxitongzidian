# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"嘅":("q「亲缺」取「缺」","《說文》「嘆也」——氣缺於中，發而為嘆。"),
"唐":("t「涂突」取「突」","唐从口庚聲，大言空大——語大而虛，突口而出。"),
"初":("ch「刺持」取「刺」","从刀从衣——刀刺布而裁之，裁衣之始為初。"),
"刺":("c「刺持」取「刺」","从刀朿聲——刃入物而刺之。"),
"副":("f「附分」取「分」","从刀畐聲，《說文》「判也」——刀分物而為副貳。"),
"劫":("j「聚决」取「聚」","从力去聲——聚力以脅，奪之而去。"),
}
n=0
for ch,(head,rest) in M.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): print("skip",ch); continue
    d=json.load(io.open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="shengmu": s["text"]=head+"："+rest
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("改",n)