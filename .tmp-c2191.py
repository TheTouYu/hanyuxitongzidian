import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\弋.json"; d=json.load(io.open(p,encoding="utf-8"))
if not any(s["key"]=="erji" for s in d["sections"]):
    i=[k for k,s in enumerate(d["sections"]) if s["key"]=="zizu"][0]
    d["sections"].insert(i+1,{"key":"erji","label":"本部二级字根","text":"","links":[{"ch":"式","label":"式"}],"cites":[]})
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("弋 加二级链接 式")