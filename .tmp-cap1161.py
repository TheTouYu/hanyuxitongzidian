import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\尺.json"; d=json.load(io.open(p,encoding="utf-8"))
secs=[s for s in d["sections"] if s.get("key")!="suoshujuan"]
secs.append({"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷三矢","label":"卷三 矢"}]})
d["sections"]=secs
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print([s for s in d["sections"] if s["key"]=="suoshujuan"])