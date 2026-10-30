import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\巵.json"
d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s.get("key")=="zizu":
        s["text"]="字族衍義：原稿本字下未列以「巵」為聲符之字（本字自用，無字族）。"
        s["groups"]=[{"title":"（原稿未列以巵為聲符之字）","note":"","rows":[["巵","zhī","匚","酒器，四升；小篆訛勺為卩（原文）"]]}]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")