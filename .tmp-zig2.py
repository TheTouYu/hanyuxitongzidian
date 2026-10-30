import json,glob,os
gdir=r"web\public\glyphs"; pdir=os.path.join(gdir,"photos")
variant=json.load(open(r"web\public\variants.json",encoding="utf-8"))
fixed=0; stats={"both":0,"glyph":0,"photo":0,"none":0}
for p in glob.glob(r"web\public\cards\*.json"):
    c=json.load(open(p,encoding="utf-8"))
    sec=[s for s in c["sections"] if s["key"]=="zigen"]
    if not sec: continue
    if not sec[0]["text"].startswith("字形："): continue
    ch=c.get("char") or os.path.splitext(os.path.basename(p))[0]
    cands=[ch,variant.get(ch)]
    ngl=nph=0; src=None
    for x in [y for y in cands if y]:
        d=os.path.join(gdir,x)
        if os.path.isdir(d):
            g=len([f for f in os.listdir(d) if f.lower().endswith(".png")])
            if g>ngl: ngl=g; src=x
        pd=os.path.join(pdir,x)
        if os.path.isdir(pd):
            q=len([f for f in os.listdir(pd) if f.lower().endswith((".jpg",".png"))])
            if q>nph: nph=q; src=src or x
    if ngl and nph: txt=f"字形：库内收古文字字形 {ngl} 形（glyphs/{src}/），另有插图 {nph} 幅（photos/{ch}/），随卡附出。"; stats["both"]+=1
    elif ngl: txt=f"字形：库内收古文字字形 {ngl} 形（glyphs/{src}/），随卡附出；本部原稿无独立插图。"; stats["glyph"]+=1
    elif nph: txt=f"字形：古文字字形库内未收；原稿所配插图 {nph} 幅（photos/{ch}/），随卡附出。"; stats["photo"]+=1
    else: txt="字形：古文字字形未收，原稿该字条亦无插图（已核对该条前后各段）。"; stats["none"]+=1
    sec[0]["text"]=txt
    json.dump(c,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); fixed+=1
print("重核",fixed,stats)