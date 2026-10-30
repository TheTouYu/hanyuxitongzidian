import json,os
d=json.load(open(r"web\public\docx-index.json",encoding="utf-8"))["chars"]
for k in ("孚","孵","卵"):
    for e in d.get(k,[])[:2]:
        print(k,"|",e["f"],"p",e["p"],"|",e["t"][:90])
ph=r"web\public\glyphs\photos"
print("photos dirs:", [x for x in os.listdir(ph)][:20] if os.path.isdir(ph) else "none")