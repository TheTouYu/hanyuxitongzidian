# -*- coding: utf-8 -*-
import sys,json,io,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
t=ps[391]; print("TAIL:",t[-160:])
p=r"D:\系统汉字\web\public\cards\家.json"; d=json.load(io.open(p,encoding="utf-8"))
groups=[{"title":"①指家居、嫁娶、庄稼等（谐声字）","header":["字","读音","类属","取义落点"],"note":"","rows":[
 ["𢜿","jià","心","《集韻》「居迓切，音嫁。心不安也」；家聲，若有所失之意"],
 ["嫁","jià","女","《說文》「女適人也。从女家聲」；《廣韻》「家也。故婦人謂嫁曰歸」"],
 ["稼","jià","禾","《說文》「禾之秀實為稼……一曰稼，家事也。一曰在野曰稼」"],
 ["幏","jià","巾","《說文》「南郡蠻夷賨布。从巾家聲」，充當賦稅的布匹"],
 ["榢（架枷）","jià","木","《集韻》引《博雅》「杙也，所以舉物也。或作榢、架。亦書作枷」"],
 ["傢","xiàng、jiā","人","《漢典》：xiàng 同「像」；jiā 傢夥、傢伙（器具；指人或牲畜）"]]},
 {"title":"②音譯字","header":["字","读音","类属","取义落点"],"note":"","rows":[
 ["鎵","jiā","金","稀有藍白色三價金屬元素（Ga）；音譯字，金旁定金屬"]]},
 {"title":"③形近字「类」之訛","header":["字","读音","类属","取义落点"],"note":"","rows":[
 ["𩔧（類）","lèi","頁","《龍龕》「𩔧，俗；類，正。音淚」；類之俗寫，形近家聲而訛"]]}]
for s in d["sections"]:
    if s["key"]=="zizu": s["groups"]=groups
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
r=subprocess.run([PY if False else sys.executable, r"D:\系统汉字\tools\check-cards.py"],capture_output=True,text=True)
print(r.stdout.strip()[:200])