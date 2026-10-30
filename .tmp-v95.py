# -*- coding: utf-8 -*-
import io,json,glob,re,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; Z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
CN="零一二三四五六七八九十"
def cn(n):
    if n<=10: return CN[n]
    if n<20: return "十"+CN[n%10]
    if n<100: return CN[n//10]+"十"+(CN[n%10] if n%10 else "")
    return "一百"
H=re.compile(r"^(\d{1,3})[.．]\s*(\S{1,2})部$")
JUNK=re.compile(r"^(第[零一二三四五六七八九十百]+[卷章]|《系统汉语》|目\s*录|\d+$)")
vol={}
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except Exception: continue
    first=None
    for t in ps:
        m=H.match(t)
        if m: first=int(m.group(1)); break
    if first is None: continue
    for j in Z["juan"]:
        if j["from"]<=first<=j["to"]: vol.setdefault(j["no"],(f,ps)); break
def cls(t):
    if re.search(r"音源|音源字|聲符|聲母|音系|聲",t): return "音源"
    if re.search(r"說物|說物字|鳥|獸|草|木|蟲|魚|禽|獸",t): return "说物"
    return "文化"
done=0
for j in Z["juan"]:
    nm="卷%s%s"%(cn(j["no"]),j["name"]); fp=os.path.join(C,nm+".json")
    if not os.path.exists(fp) or j["no"] not in vol: continue
    f,ps=vol[j["no"]]
    head=[]
    for t in ps:
        if not t: continue
        if H.match(t): break
        if JUNK.match(t): continue
        if len(t)<8: continue
        head.append(t)
    if not head: continue
    d=json.load(io.open(fp,encoding="utf-8"))
    old={s.get("key"):s for s in d["sections"]}
    yx=old.get("js_音系") or {}
    out=[{"key":"daoyu","label":"导语","text":head[0],"cites":[]}]
    buckets={"音源":[],"说物":[],"文化":[]}
    for t in head[1:]: buckets[cls(t)].append(t)
    if not buckets["音源"] and len(head)>1: buckets["音源"].append(head[1])
    for k in ("音源","说物","文化"):
        if buckets[k]:
            out.append({"key":"js_"+k,"label":k,"text":"\n\n".join(buckets[k][:6]),"cites":[]})
    yx2={"key":"js_音系","label":"音系","text":"音系即本卷所属诸部（下表）。","cites":[]}
    if yx.get("groups"): yx2["groups"]=yx["groups"]
    out.append(yx2)
    d["sections"]=out; json.dump(d,io.open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1); done+=1
print("卷首按原文写入",done)
d=json.load(io.open(C+r"\卷八虎.json",encoding="utf-8"))
for s in d["sections"]: print(s["label"], (s.get("text") or "")[:40].replace("\n"," "))