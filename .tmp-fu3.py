import os, json
ph=r"web\public\glyphs\photos"
dirs=os.listdir(ph)
hit=[d for d in dirs if d in ("孵","孚","卵","雞","鸡","雛","雏","母")]
print("hit dirs:", [(d,len(os.listdir(os.path.join(ph,d)))) for d in hit])
idx=json.load(open(r"web\public\glyphs\index.json",encoding="utf-8"))
ch=idx.get("chars",idx)
withp=[k for k,v in ch.items() if isinstance(v,dict) and v.get("photos")]
print("index photos count:", len(withp))
print("with 卵/孚/孵/雞:", [k for k in withp if k in ("卵","孚","孵","雞","鸡","雛")])
print("sample:", withp[:10])