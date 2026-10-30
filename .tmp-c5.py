# -*- coding: utf-8 -*-
import json,glob,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
md=io.open(r"D:\系统汉字\knowledge\hanzi-origin\mulu.md",encoding="utf-8").read()
chaps=[]; vols=[]
for line in md.splitlines():
    m=re.match(r"#+\s*第([一二三四五六七八九十]+)章\s*(\S+?)[：:]\s*卷(\S+?)至卷(\S+?)，第(\d+)–(\d+)部",line)
    if m: chaps.append({"cn":m.group(1),"name":m.group(2),"v1":m.group(3),"v2":m.group(4)})
    m2=re.match(r"#+\s*卷(\S+?)\s*(\S+?)[：:]\s*第(\d+)–(\d+)部",line)
    if m2: vols.append({"vn":m2.group(1),"name":m2.group(2),"a":int(m2.group(3)),"b":int(m2.group(4))})
z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
inv={}
for ch,info in (z.get("byName") or {}).items(): inv[info.get("no")]=ch
# chapter docs
docs={}
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for k in range(0,60):
        if k>=len(ps): break
        m=re.match(r"^第([一二三四五六七八九十]+)章\s*(\S+)$",ps[k])
        if m: docs[m.group(1)]={"ps":ps,"i":k}; break
    if "一" not in docs and ps and ps[0].startswith("卷一"):
        docs["一"]={"ps":ps,"i":0}
json.dump({k:{"i":v["i"]} for k,v in docs.items()},io.open(r"D:\系统汉字\.tmp-docs.json","w"),ensure_ascii=False)
made=0
for c in chaps:
    d=docs.get(c["cn"])
    ys=[];yl=[]
    if d:
        ps=d["ps"]; block=[]
        for k in range(d["i"]+1,min(d["i"]+40,len(ps))):
            t=ps[k]
            if not t or t.startswith("▲"): continue
            if re.match(r"^\d{1,3}[.．]\s*\S{1,2}部$",t): break
            if re.match(r"^卷\S",t) and c["cn"]!="一": break
            block.append(t)
        cut=None
        for j,t in enumerate(block):
            if ("音義" in t and "通" in t) or t.startswith("與《") or t.startswith("同《"):
                cut=j; break
        if cut is None: ys=block
        else: ys=block[:cut]; yl=block[cut:]
    sel=[v for v in vols if True]
    i1=next((i for i,v in enumerate(vols) if v["vn"]==c["v1"]),0)
    i2=next((i for i,v in enumerate(vols) if v["vn"]==c["v2"]),i1)
    rows=[];links=[]
    for v in vols[i1:i2+1]:
        names="、".join(f"{n}.{inv.get(n,'□')}部" for n in range(v["a"],v["b"]+1))
        rows.append([f"卷{v['vn']} {v['name']}", f"第{v['a']}–{v['b']}部", names])
        links.append(f"卷{v['vn']}{v['name']}")
    secs=[
      {"key":"yiyuan","label":"义源","text":"\n".join(ys) or "（原稿本章无总述）","cites":[]},
      {"key":"yilei","label":"义类（声素与通假）","text":"\n".join(yl) or "（原稿本章未列同音通假诸条）","cites":[]},
      {"key":"yinxi","label":"音系表","text":"本章所辖各卷及部目：","cites":[],
       "groups":[{"title":f"第{c['cn']}章 {c['name']} 音系表","note":"","header":["卷","部目范围","部目"],"rows":rows,"links":links}]}]
    cd={"char":f"第{c['cn']}章{c['name']}","chapter":c["cn"],"chapterName":c["name"],"chapterCard":f"第{c['cn']}章{c['name']}",
        "pinyin":"","level":0,"parent":"","bus":[{"num":0,"name":f"第{c['cn']}章 {c['name']}"}],"sections":secs}
    p=rf"{C}\第{c['cn']}章{c['name']}.json"
    json.dump(cd,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); made+=1
    print(c["cn"],c["name"],"义源段",len(ys),"义类段",len(yl),"卷",len(rows))
print("made",made)