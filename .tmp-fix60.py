# -*- coding: utf-8 -*-
import io,json,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; n=0
for f in os.listdir(C):
    if not f.endswith(".json") or f=="index.json": continue
    p=os.path.join(C,f)
    try: d=json.load(io.open(p,encoding="utf-8"))
    except Exception: continue
    if not isinstance(d,dict): continue
    lk=d.get("links") or []
    if not lk: continue
    for s in d.get("sections",[]):
        if s.get("label")=="所属卷" and not s.get("links"):
            s["links"]=lk; n+=1
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cards patched",n)
for fn in ("index.html","test.html","app.html"):
    p=os.path.join(r"D:\系统汉字\web\public",fn)
    if not os.path.exists(p): continue
    s=io.open(p,encoding="utf-8").read(); o=s
    s=s.replace("(s.links||[])", "((s.links&&s.links.length?s.links:((typeof CARD!=='undefined'&&CARD&&CARD.links)||[]))||[])")
    if s!=o: io.open(p,"w",encoding="utf-8",newline="").write(s); print("patched",fn)