# -*- coding: utf-8 -*-
import json,glob,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
M=r"D:\字谱智能体"
md=io.open(r"D:\系统汉字\knowledge\hanzi-origin\mulu.md",encoding="utf-8").read()
chaps=[]; vols=[]
for line in md.splitlines():
    m=re.match(r"#+\s*第([一二三四五六七八九十]+)章\s*(\S+?)[：:]\s*卷(\S+?)至卷(\S+?)，第(\d+)–(\d+)部",line)
    if m: chaps.append({"cn":m.group(1),"name":m.group(2)})
    m2=re.match(r"#+\s*卷(\S+?)\s*(\S+?)[：:]\s*第(\d+)–(\d+)部",line)
    if m2: vols.append({"vn":m2.group(1),"name":m2.group(2),"a":int(m2.group(3)),"b":int(m2.group(4))})
print("chaps",len(chaps),"vols",len(vols))
# chapter docs
docs={}
for f in glob.glob(M+r"\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for k in range(0,60):
        if k>=len(ps): break
        m=re.match(r"^第([一二三四五六七八九十]+)章\s*(\S+)$",ps[k])
        if m: docs[m.group(1)]={"f":f,"i":k,"ps":ps}; break
print("docs",len(docs),[k for k in docs])
CN={"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10,"十一":11,"十二":12}
def num(s): return CN.get(s,0)
# volume cards 部目
def vol_rows(v):
    f=rf"D:\系统汉字\web\public\cards\卷{v['vn']}{v['name']}.json"
    if not os.path.exists(f):
        g=glob.glob(rf"D:\系统汉字\web\public\cards\卷*{v['name']}.json")
        f=g[0] if g else None
    if not f: return []
    d=json.load(io.open(f,encoding="utf-8"))
    for s in d.get("sections",[]):
        if s.get("key")=="zizu":
            for g in (s.get("groups") or []):
                if g.get("title","").startswith("部目"):
                    return [[r[0] for r in g["rows"]], f]
    return []
out=[]
for c in chaps:
    n=num(c["cn"]); d=docs.get(c["cn"])
    ys=[]; yl=[]
    if d:
        ps=d["ps"]; i=d["i"]; block=[]
        for k in range(i+1,min(i+40,len(ps))):
            t=ps[k]
            if not t or t.startswith("▲"): continue
            if re.match(r"^卷\S",t) or re.match(r"^\d{1,3}[.．]",t): break
            block.append(t)
        cut=None
        for j,t in enumerate(block):
            if ("音義" in t and "通" in t) or t.startswith("與《") or t.startswith("同《"):
                cut=j; break
        if cut is None: ys=block; yl=[]
        else: ys=block[:cut]; yl=block[cut:]
    rows=[]; links=[]
    for v in vols:
        if v["a"]//1000: pass
    # assign vols by order: chapter n covers vols [(n-1)*8+1 .. ] unknown; use ranges from mulu heading text
    out.append({"cn":c["cn"],"name":c["name"],"ys":len(ys),"yl":len(yl),"rows":rows})
print("built intros",[(o["cn"],o["ys"],o["yl"]) for o in out])