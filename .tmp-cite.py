# -*- coding: utf-8 -*-
import json,sys,io
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def setg(name,groups):
    p=rf"{C}\{name}.json"; d=json.load(open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")=="zizu": s["groups"]=groups
    json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
z1=[
 ["脂","zhī","肉","《說文》「戴角者脂，無角者膏。从肉旨聲」——有角動物的脂肪（脂膏）"],
 ["𩊝","zhì","革","《說文》「蓋杠絲也。从革旨聲」——車蓋杠柄上圍束的皮繩"],
 ["鴲","zhī","鳥","《說文》「瞑鴲也」；《廣韻》「小靑雀也」——喙光滑如凝脂"],
 ["㞓","qì","尸","《說文》「尻也。从尸旨聲」——臀部，肉質最厚實處"],
 ["鮨","qí","魚","《說文》「魚䏽醬也。出蜀中」——魚醬"],
 ["酯","zhǐ","酉","原稿未標書名：有機化合物的一類，脂肪的主要成分"],
 ["麂","jǐ","鹿","《說文》「大麋也，狗足。从鹿旨聲」——皮毛細軟可制革"]]
z2=[
 ["恉","zhǐ","心","《說文》「意也。从心旨聲」——意圖"],
 ["指","zhǐ","手","《說文》「手指也。从手旨聲」；《廣韻》「又示也、斥也」"],
 ["䭬","qǐ","首","《說文》「下首也。从𩠐旨聲」——叩頭至地"],
 ["詣","yì","言","《說文》「候至也。从言旨聲」——問候、前往"],
 ["栺","yì","木","《廣韻》「枍栺，殿名」；「栺栭，木名」"]]
q1=[
 ["鬐","qí","髟","《新附》「馬鬣也。从髟耆聲」——馬頸長毛"],
 ["蓍","shī","艸","《說文》「蒿屬，生十歲，百莖」"],
 ["榰","zhī","木","《說文》「柱砥。古用木，今以石」——柱腳石、支撐"]]
q2=[["嗜","shì","口","《說文》「嗜欲，喜之也。从口耆聲」——喜歡"]]
q3=[["（原稿未列具體字）","","","此組原稿僅見標題"]]
j=[["䭫","qǐ","首","《字彙》「䭫，通用稽」——叩首"],
   ["嵇","jī","山","《說文》「山名。从山，稽省聲」"]]
setg("旨",[{"title":"①指脂膏，表示光滑、細嫩","note":"","rows":z1},
          {"title":"②指精華，表示指向、分枝","note":"","rows":z2}])
setg("耆",[{"title":"①指老，表示硬挺、支撐","note":"","rows":q1},
          {"title":"②指喜歡，表示愛好、恭順","note":"","rows":q2},
          {"title":"③形近字「者」之訛","note":"","rows":q3}])
setg("稽",[{"title":"多指穀穗的懸垂，表示堅硬、叩首","note":"","rows":j}])
# 本义/转义补出处
def addcite(name,key,tail):
    p=rf"{C}\{name}.json"; d=json.load(open(p,encoding="utf-8"))
    for s in d["sections"]:
        if s.get("key")==key and tail not in s["text"]: s["text"]=s["text"].rstrip()+" "+tail
    json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
addcite("旨","benyi","（原稿原文，見卷一「3.旨部」本義段）")
addcite("旨","zhuanyi","（《說文》「美也。从甘匕聲」，職雉切）")
addcite("耆","benyi","（《說文》「老也。从老省，旨聲」，渠脂切）")
addcite("稽","benyi","（《說文》「留止也」，古兮切）")
p=r"D:\系统汉字\prompts\exegesis.md"; s=io.open(p,encoding="utf-8").read()
old="直接照录原稿该字正条的义项（《說文》《廣韻》等原文）；"
new="直接照录原稿该字正条的义项，并像原文一样写明出处（《說文》《廣韻》《字彙》《新附》等；原稿未标者注明「原稿未標書名」）；"
if old in s: io.open(p,"w",encoding="utf-8",newline="\n").write(s.replace(old,new,1)); print("rule ok")
print("done")