# -*- coding: utf-8 -*-
import io,json,glob,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for f in glob.glob(C+r"\卷*.json"):
    d=json.load(io.open(f,encoding="utf-8")); S=d.get("sections",[])
    def g(keys):
        for s in S:
            if s.get("key") in keys and (s.get("text") or s.get("groups")): return s
        return None
    tbl=g(("js_音系",)) or g(("zizu",))
    out=[]
    dy=g(("daoyu","js_导语"))
    t=(dy or {}).get("text") or ""
    if not t:
        for s in S:
            if s.get("text"): t="本卷总说见原稿卷首。"; break
    out.append({"key":"daoyu","label":"导语","text":t,"cites":[]})
    for lab,keys in (("音源",("js_音源","yinyuan")),("说物",("js_说物","shuowu")),("文化",("js_文化","wenhua","bianzheng","benyi"))):
        s=g(keys)
        if s: out.append({"key":"js_"+lab,"label":lab,"text":s.get("text",""),"cites":s.get("cites",[])})
        else: out.append({"key":"js_"+lab,"label":lab,"text":"（原稿本卷卷首无此项。）","cites":[]})
    yx={"key":"js_音系","label":"音系","text":(tbl or {}).get("text") or "音系即本卷所属诸部（下表）。","cites":[]}
    if tbl and tbl.get("groups"): yx["groups"]=tbl["groups"]
    out.append(yx)
    d["sections"]=out; json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("重建",n)
d=json.load(io.open(C+r"\卷一雞.json",encoding="utf-8"))
print([s["label"] for s in d["sections"]], bool(d["sections"][-1].get("groups")))