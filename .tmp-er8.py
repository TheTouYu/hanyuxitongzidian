import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\尔.json"; d=json.load(open(p,encoding="utf-8"))
d2=dict(d); d2["char"]="爾"
json.dump(d2,open(r"D:\系统汉字\web\public\cards\爾.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
ip=r"D:\系统汉字\web\public\cards\index.json"; idx=json.load(open(ip,encoding="utf-8"))
if not any(x["c"]=="爾" for x in idx):
    idx.insert(0,{"c":"爾","p":d["pinyin"],"b":329,"n":"爾","lv":1,"t":[s["text"][:60] for s in d["sections"] if s.get("text")][:3]})
json.dump(idx,open(ip,"w",encoding="utf-8"),ensure_ascii=False,separators=(",",":"))
print("ok")