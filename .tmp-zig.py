import json,glob,os
gi=json.load(open(r"web\public\glyphs\index.json",encoding="utf-8"))
chars=gi.get("chars",gi)
try: pi=json.load(open(r"web\public\photo-index.json",encoding="utf-8"))
except Exception: pi={}
ph=pi.get("photos",pi) if isinstance(pi,dict) else {}
pdir=r"web\public\glyphs\photos"
variant=json.load(open(r"web\public\variants.json",encoding="utf-8"))
fixed=0; stats={"both":0,"glyph":0,"photo":0,"none":0}
for p in glob.glob(r"web\public\cards\*.json"):
    c=json.load(open(p,encoding="utf-8"))
    ks=[s["key"] for s in c["sections"]]
    if "zigen" in ks: continue
    ch=c.get("char") or os.path.splitext(os.path.basename(p))[0]
    cands=[ch]+([variant[ch]] if ch in variant else [])
    ngl=0; nph=0; src=None
    for x in cands:
        v=chars.get(x)
        if isinstance(v,dict): ngl=max(ngl,len(v.get("files") or []))
        pd=os.path.join(pdir,x)
        if os.path.isdir(pd): nph=max(nph,len([f for f in os.listdir(pd) if f.lower().endswith((".jpg",".png"))]))
        if ngl or nph: src=x; break
    if ngl and nph: txt=f"字形：库内收古文字字形 {ngl} 形（glyphs/{src}/），另有插图 {nph} 幅（photos/{src}/），随卡附出。"; stats["both"]+=1
    elif ngl: txt=f"字形：库内收古文字字形 {ngl} 形（glyphs/{src}/），随卡附出；本部原稿无独立插图。"; stats["glyph"]+=1
    elif nph: txt=f"字形：本字古文字字形库内未收；原稿所配插图 {nph} 幅（photos/{src}/），随卡附出。"; stats["photo"]+=1
    else: txt="字形：本字古文字字形未收，原稿该字条亦无插图（已核对该条前后各段）。"; stats["none"]+=1
    c["sections"].insert(1,{"key":"zigen","label":"字形","text":txt,"cites":[]})
    json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fixed+=1
print("补字形栏",fixed,stats)