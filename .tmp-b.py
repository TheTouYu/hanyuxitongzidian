import json,os,re
d=json.load(open(r"web\public\docx-index.json",encoding="utf-8"))["chars"]
for e in d.get("笨",[])[:2]: print("笨 p",e["p"],e["f"],"|",e["t"][:160])
print("photo:", os.path.isdir(r"web\public\glyphs\photos\笨"))
t=io.open(r"knowledge\hanzi-yinyuan\24a-bei.md",encoding="utf-8").read() if os.path.exists(r"knowledge\hanzi-yinyuan\24a-bei.md") else ""
m=[x for x in re.findall(r"### (.+?)\n(.*?)#### 适用边界", t, re.S) if "笨" in x[0]+x[1]][:2]
for a,b in m: print("CLAIM",a.strip(),"|",b.strip()[:200])