import json,os
d=json.load(open(r"web\public\docx-index.json",encoding="utf-8"))["chars"]
for ch in ("蠃","蜾","贏"):
    for e in d.get(ch,[])[:1]: print(ch,"p",e["p"],"|",e["t"][:170])
ph=r"web\public\glyphs\photos"
print("photos:",[c for c in ("蠃","蜾","贏") if os.path.isdir(os.path.join(ph,c))])