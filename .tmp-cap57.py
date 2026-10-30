# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=rf"{C}\𢑓.json"; d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        g=s["groups"][0]
        have={r[0] for r in g["rows"]}
        add=[["𢜿","jià","心","《集韻》「居迓切，音嫁。心不安也」；家聲，若有所失之意"],
             ["鎵","jiā","金","一種稀有藍白色三價金屬元素（元素符號 Ga）；家聲為音譯字，形旁定金屬"],
             ["𩔧","lèi","頁","《龍龕》「𩔧，俗；類，正。音淚」；類之俗寫，形近家聲而訛（讹字）"]]
        for r in add:
            if r[0] not in have: g["rows"].append(r)
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
t=io.open(r"D:\系统汉字\prompts\exegesis.md",encoding="utf-8").read()
if "音译字与形近讹字" not in t:
    t=t.rstrip()+"\n\n14. **原文字族一个不漏**：字族表必须收原稿族行里的全部字头，包括①常用谐声字②音译字（如鎵，注「音譯」）③形近讹字（如𩔧為類之俗寫，注「訛」）④异体（并入正字行，括号列出并把括号内字进索引）。不得因「解释不了取义」而略去。\n"
    io.open(r"D:\系统汉字\prompts\exegesis.md","w",encoding="utf-8",newline="\n").write(t)
print("ok")