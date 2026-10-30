import json,os
d=json.load(open(r"web\public\docx-index.json",encoding="utf-8"))["chars"]
for ch in ("鳁","鰮","鰛","昷","溫"):
    for e in d.get(ch,[])[:1]: print(ch,"p",e["p"],"|",e["t"][:150])
ph=r"web\public\glyphs\photos"
print("photos:",[c for c in ("鳁","鰮","鰛","昷") if os.path.isdir(os.path.join(ph,c))])