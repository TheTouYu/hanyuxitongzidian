import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\弋.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="erji": s["links"]=[{"ch":c,"label":c} for c in ("式","尗","曳")]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("弋二级：式 尗 曳")