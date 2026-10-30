# -*- coding: utf-8 -*-
import io,json,os,re,sys,shutil
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
Z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
CM=json.load(io.open(r"D:\系统汉字\.tmp-charmap.json",encoding="utf-8")) if os.path.exists(r"D:\系统汉字\.tmp-charmap.json") else {}
PH=json.load(io.open(os.path.join(G,"photos","index.json"),encoding="utf-8")); PH=PH.get("photos") or PH
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
def ben(d):
    for s in d.get("sections",[]):
        if s.get("key") in ("benyi","benyi2","shiyi") and s.get("text"): return s["text"]
    return ""
def center(d):
    t=ben(d)
    t=re.sub(r"^《系统汉语》[^：]{0,30}：","",t)
    t=re.sub(r"^[^：，。]{1,8}[，,]\s*[a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]+[，,]\s*","",t)
    s=re.split(r"[。；]",t)[0]
    return s[:34]
def family(no,name):
    out=[]
    for ch,v in CM.items():
        if isinstance(v,dict) and v.get("bu")==no: out.append(ch)
    if not out:
        c=cards.get(name or "")
        if c:
            for s in c.get("sections",[]):
                if s.get("key")=="zizu" and s.get("groups"):
                    for g in s["groups"]:
                        for r in g.get("rows",[]): out.append(str(r[0]).split("（")[0])
    return "".join(dict.fromkeys(out))
hits=0
for j in Z["juan"]:
    nm="卷%s%s"%(cn(j["no"]),j["name"]); p=os.path.join(C,nm+".json"); d=json.load(io.open(p,encoding="utf-8"))
    rows=[];links=[];src=[]
    for x in j["bu"]:
        ch=x["name"] or ""; c=cards.get(ch,{})
        cen=center(c) if c else ""; fam=family(x["no"],ch)
        rows.append(["%d.%s部"%(x["no"],ch or "？"), ch or "（待定）", cen or "—", fam or "—"]); links.append(ch)
        hits+= bool(cen)
        if ch and ch in PH: src.extend([ (ch,f) for f in PH[ch] ][:3])
    for s in d["sections"]:
        if s.get("key")=="zizu":
            s["groups"]=[{"title":"%s 部目（第%d–%d部）"%(nm,j["from"],j["to"]),"note":"","header":["部目","字根","中心义","字族"],"rows":rows,"links":links}]
    # 插图：拷到 photos/<卷名>/
    if src:
        out=os.path.join(G,"photos",nm); os.makedirs(out,exist_ok=True)
        fs=[]
        for ch,f in src[:8]:
            try:
                shutil.copyfile(os.path.join(G,"photos",ch,f),os.path.join(out,f)); fs.append(f)
            except Exception: pass
        if fs: PH[nm]=fs
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
json.dump({"photos":PH},io.open(os.path.join(G,"photos","index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("中心义",hits,"/608；卷插图已挂",sum(1 for k in PH if k.startswith("卷")))