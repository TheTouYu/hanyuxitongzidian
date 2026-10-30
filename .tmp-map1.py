import json,re
bu=json.load(open(r"D:\系统汉字\.tmp-bu.json",encoding="utf-8"))
# bu: {部号: 部名} or list
if isinstance(bu,dict): items=[(k,v) for k,v in bu.items()]
else: items=[(str(i+1),v) for i,v in enumerate(bu)]
names=["心","青","昷","感","瞿","睪","每","艮","布","去","共","耳","采","尉","康","既","莫","衍","徵","備","易","束","宛","滿","勤","敃","閔","敢","貇","䜌","之","中","己","亡","刃","勿","台","隹","隋","音","禺","茲","彗","相","秋"]
for n in names:
    hit=[(k,v) for k,v in items if str(v).strip().startswith(n)]
    print(n, hit[:2])