# -*- coding: utf-8 -*-
import io,json,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; Z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
CN="零一二三四五六七八九十"
def cn(n):
    if n<=10: return CN[n]
    if n<20: return "十"+CN[n%10]
    if n<100: return CN[n//10]+"十"+(CN[n%10] if n%10 else "")
    return "一百"
cards={}
for f in os.listdir(C):
    if f.endswith(".json") and f!="index.json":
        try: d=json.load(io.open(os.path.join(C,f),encoding="utf-8"))
        except Exception: continue
        cards[d.get("char")]=d
def center(d):
    for s in d.get("sections",[]):
        if s.get("key")=="zizu" and s.get("groups"):
            t=s["groups"][0].get("title","")
            t=re.sub(r"^[①-⑳\d.、\s]+","",t)
            t=re.split(r"[（(，,]",t)[0].strip()
            if 2<=len(t)<=14: return t
    for s in d.get("sections",[]):
        if s.get("key") in ("benyi","benyi2") and s.get("text"):
            t=re.sub(r"^《系统汉语》[^：]*：","",s["text"])
            return re.split(r"[，。；、]",t)[0][:12]
    return ""
def zuzu(d):
    for s in d.get("sections",[]):
        if s.get("key")=="zizu" and s.get("groups"):
            return "".join(str(x[0]).split("（")[0] for x in s["groups"][0]["rows"][:4])
    return ""
for j in Z["juan"]:
    nm="卷%s%s"%(cn(j["no"]),j["name"]); p=os.path.join(C,nm+".json"); d=json.load(io.open(p,encoding="utf-8"))
    rows=[];links=[]
    for x in j["bu"]:
        ch=x["name"] or ""; c=cards.get(ch,{})
        rows.append(["%d.%s部"%(x["no"],ch or "？"), ch or "（待定）", center(c) or "—", zuzu(c) or "—"]); links.append(ch)
    for s in d["sections"]:
        if s.get("key")=="zizu":
            s["groups"]=[{"title":"%s 部目（第%d–%d部）"%(nm,j["from"],j["to"]),"note":"","header":["部目","字根","中心义","字族"],"rows":rows,"links":links}]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
d=json.load(io.open(os.path.join(C,"卷一雞.json"),encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        for r in s["groups"][0]["rows"][:5]: print(r)