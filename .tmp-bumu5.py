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
def text_of(d,keys):
    for s in d.get("sections",[]):
        if s.get("key") in keys and s.get("text"): return s["text"]
    return ""
def center(d):
    for s in d.get("sections",[]):
        if s.get("key")=="zizu" and s.get("groups") and s["groups"][0].get("rows"):
            t=re.sub(r"^[①-⑳\d.、\s]+","",s["groups"][0].get("title",""))
            t=re.split(r"[（(，,]",t)[0].strip()
            if 2<=len(t)<=16: return t
            break
    t=text_of(d,("zizu","shiyi","benyi","benyi2")) or ""
    t=re.sub(r"^[^：]{0,20}：","",t)
    c=re.split(r"[；;。]",t)[0]
    return c[:16]
def zuzu(d):
    for s in d.get("sections",[]):
        if s.get("key")=="zizu" and s.get("groups"):
            return "".join(str(x[0]).split("（")[0] for x in s["groups"][0]["rows"][:4])
    return ""
hit=0;tot=0
for j in Z["juan"]:
    nm="卷%s%s"%(cn(j["no"]),j["name"]); p=os.path.join(C,nm+".json"); d=json.load(io.open(p,encoding="utf-8"))
    rows=[];links=[]
    for x in j["bu"]:
        ch=x["name"] or ""; c=cards.get(ch,{})
        cen=center(c) if c else ""; zz=zuzu(c) if c else ""
        rows.append(["%d.%s部"%(x["no"],ch or "？"), ch or "（待定）", cen or "—", zz or "—"]); links.append(ch)
        tot+=1; hit+= bool(cen)
    for s in d["sections"]:
        if s.get("key")=="zizu":
            s["groups"]=[{"title":"%s 部目（第%d–%d部）"%(nm,j["from"],j["to"]),"note":"","header":["部目","字根","中心义","字族"],"rows":rows,"links":links}]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("行",tot,"有中心义",hit)