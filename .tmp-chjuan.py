# -*- coding: utf-8 -*-
import io,json,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
Z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
CN="零一二三四五六七八九十"
def cn(n):
    if n<=10: return CN[n]
    if n<20: return "十"+CN[n%10]
    if n<100:
        return CN[n//10]+"十"+(CN[n%10] if n%10 else "")
    return "一百"
CH=[("一","士",1,47,"卷一至卷七"),("二","谷",48,87,"卷八至卷十五"),("三","冓",88,113,"卷十六至卷二十一"),
    ("四","孕",114,204,"卷二十二至卷三十四"),("五","屰",205,261,"卷三十五至卷四十六"),("六","因",262,327,"卷四十七至卷五十七"),
    ("七","兒",328,382,"卷五十八至卷六十三"),("八","子",383,417,"卷六十四至卷六十九"),("九","大",418,442,"卷七十至卷七十三"),
    ("十","卝",443,494,"卷七十四至卷八十"),("十一","兄",495,539,"卷八十一至卷八十九"),("十二","老",540,609,"卷九十至卷一百")]
JU={j["no"]:j for j in Z["juan"]}
# 章卡
for idx,(cno,cname,a,b,jrange) in enumerate(CH,1):
    j1=JU[min(JU,key=lambda x:abs(x-(int(jrange.split("至")[0].replace("卷","").replace("一","1").replace("二","2").replace("三","3").replace("四","4").replace("五","5").replace("六","6").replace("七","7").replace("八","8").replace("九","9").replace("十","10")) if False else 0)))] if False else None
    rows=[];links=[]
    for j in Z["juan"]:
        if a<=j["from"]<=b:
            rows.append(["卷"+cn(j["no"])+j["name"],j["name"],"第%d–%d部（%d部）"%(j["from"],j["to"],j["to"]-j["from"]+1)])
            links.append("卷"+cn(j["no"])+j["name"])
    card={"char":"第%s章%s"%(cno,cname),"cname":"第%s章 %s"%(cno,cname),"chapter":cno,"chapterName":cname,
          "chapterCard":"第%s章%s"%(cno,cname),"level":0,"parent":"","bus":[{"num":0,"name":cname}],
          "sections":[
            {"key":"benyi","label":"章首","text":"第%s章「%s」：辖%s，第%d–%d部（共%d部）。本章以「%s」为音源字，所辖各卷之部多由「%s」得声得义。"%(cno,cname,jrange,a,b,b-a+1,cname,cname),"cites":[]},
            {"key":"zizu","label":"本辖卷目","text":"","groups":[{"title":"%s（第%d–%d部）"%(jrange,a,b),"note":"","header":["卷目","音源","部属"],"rows":rows,"links":links}]}]}
    json.dump(card,io.open(os.path.join(C,"第%s章%s.json"%(cno,cname)),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 卷卡（保留卷一二的卷首正文）
keep={}
for nm in ["卷一雞","卷二㠯"]:
    p=os.path.join(C,nm+".json")
    if os.path.exists(p):
        d=json.load(io.open(p,encoding="utf-8"))
        keep[nm]=[s for s in d["sections"] if s.get("key") in ("benyi","zhuanyi","bianzheng","yinyuan")]
chof={}
for cno,cname,a,b,jr in CH:
    for j in Z["juan"]:
        if a<=j["from"]<=b: chof[j["no"]]=(cno,cname)
for j in Z["juan"]:
    nm="卷%s%s"%(cn(j["no"]),j["name"])
    cno,cname=chof[j["no"]]
    rows=[];links=[]
    for x in j["bu"]:
        n=x["name"] or ""
        rows.append([(n+"部") if n else "（部首未转录）","第%d部"%x["no"],"p%d"%x["p"]]); links.append(n)
    secs=keep.get(nm,[])
    secs=secs+[{"key":"zizu","label":"本卷部目（第%d–%d部）"%(j["from"],j["to"]),"text":"","groups":[{"title":"%s（第%d–%d部）"%(nm,j["from"],j["to"]),"note":"","header":["部首","部号","页码"],"rows":rows,"links":links}]}]
    card={"char":nm,"cname":"卷%s %s"%(cn(j["no"]),j["name"]),"chapter":cno,"chapterName":cname,"chapterCard":"第%s章%s"%(cno,cname),
          "level":0,"parent":"","bus":[{"num":0,"name":"卷%s"%cn(j["no"])}],"sections":secs}
    json.dump(card,io.open(os.path.join(C,nm+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("章卡",len(CH),"卷卡",len(Z["juan"]))