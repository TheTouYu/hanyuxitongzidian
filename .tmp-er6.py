import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\尔.json"
d=json.load(open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zigen":
        s["text"]="字形：爾（尔）本一字，古文字字形 22 形，自商代至戰國（見本欄圖）。"
json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 写入体例
q=r"D:\系统汉字\prompts\exegesis.md"; t=open(q,encoding="utf-8").read()
add="\n- 简化字与繁体／初文本为一字者（如「尔」与「爾」），字形直接挂该字，不得写「简化字本身无古文字字形」。\n"
if "本为一字者" not in t:
    t=t.rstrip()+"\n"+add.strip()+"\n"; open(q,"w",encoding="utf-8").write(t)
print("ok")