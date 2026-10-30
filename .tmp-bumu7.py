# -*- coding: utf-8 -*-
import io,json,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; Z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
CM=json.load(io.open(r"D:\系统汉字\.tmp-charmap.json",encoding="utf-8")) if os.path.exists(r"D:\系统汉字\.tmp-charmap.json") else {}
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
        if s.get("key") in ("benyi","benyi2","shiyi") and s.get("text"):
            t=s["text"]
            t=re.sub(r"^【[^】]*】","",t)
            t=re.sub(r"^《系统汉语》[^：]{0,30}：","",t)
            t=re.sub(r"^[^：，。]{1,10}[，,]\s*[a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]+[，,]\s*","",t)
            return re.split(r"[。；]",t)[0][:40]
    return ""
def family(no,name):
    out=[]
    c=cards.get(name or "")
    if c:
        for s in c.get("sections",[]):
            if s.get("key")=="zizu" and s.get("groups"):
                for g in s["groups"]:
                    for r in g.get("rows",[]): out.append(str(r[0]).split("（")[0])
    for ch,v in CM.items():
        if isinstance(v,dict) and v.get("bu")==no: out.append(ch)
    return "".join(dict.fromkeys([x for x in out if x]))
for j in Z["juan"]:
    nm="卷%s%s"%(cn(j["no"]),j["name"]); p=os.path.join(C,nm+".json"); d=json.load(io.open(p,encoding="utf-8"))
    rows=[];links=[]
    for x in j["bu"]:
        ch=x["name"] or ""; c=cards.get(ch,{})
        rows.append(["%d.%s部"%(x["no"],ch or "？"), ch or "（待定）", center(c) or "—", family(x["no"],ch) or "—"]); links.append(ch)
    for s in d["sections"]:
        if s.get("key")=="zizu":
            s["groups"]=[{"title":"%s 部目（第%d–%d部）"%(nm,j["from"],j["to"]),"note":"","header":["部目","字根","中心义","字族"],"rows":rows,"links":links}]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
d=json.load(io.open(os.path.join(C,"卷八虎.json"),encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        for r in s["groups"][0]["rows"][:2]: print(r[0],"|",r[2],"|",r[3][:24])