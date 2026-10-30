# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d={"char":"𢑓","trad":"𢑓","simp":"","pinyin":"jiā","level":2,"parent":"士","bus":[{"num":9,"name":"士"}],
"head":"𢑓（豭猳）","aliases":["豭","猳"],
"sections":[
 {"key":"benyi","label":"本义","text":"𢑓（豭猳），jiā：从豕从士（士亦聲），本義為雄豕（公豬），即「豭」之初文。《說文》豭：「牡豕也。」「家」即从宀、𢑓省聲，所从之「𢑓」正是公豬。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"由「雄豕」引申為雄性動物之通稱（《左傳》「見豭豚」）；又借為「家」之聲符，家、嫁、稼等皆由此出。","cites":[]},
 {"key":"bianzheng","label":"辩证","text":"《說文》「从宀，豭省聲」——所省者即「𢑓」，非从「豕」；舊說「家从宀从豕（屋下有豬）」為會意，不確：家是从宀、𢑓聲的形聲（轉注）字。","cites":[]},
 {"key":"yinyuan","label":"音源","text":"音源：借「士」之聲（士、𢑓同音）；家之 jiā 即承𢑓之音。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"j「聚决」取「聚」：公豬聚而決（推）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"","groups":[{"title":"以「家」為聲旁的字族","note":"","rows":[
  ["家","jiā","宀","《說文》「凥也。从宀，豭省聲」；《玉篇》「家人所居通曰家」——从宀（屋）、𢑓省聲，取𢑓（公豬）之聲"],
  ["嫁","jià","女","《說文》「女適人也」；家聲，取「有家（成家）」義"],
  ["稼","jià","禾","《說文》「禾之秀實為稼，莖節為禾。一曰稼，家事也」；家聲，取「家事」義"],
  ["傢","jiā","人","傢伙；家聲記音"],
  ["幏","jià","巾","《說文》「南郡蠻夷賨布」；家聲記音"],
  ["榢","jià","木","木名；家聲記音"],
  ["架","jià","木","《集韻》與「枷」通；家聲，取架屋義（推）"],
  ["枷","jiā","木","《說文》「拂也」；加聲，借家音"]]}]}]}
json.dump(d,io.open(rf"{C}\𢑓.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
p=rf"{C}\家.json"; x=json.load(io.open(p,encoding="utf-8")); x["parent"]="𢑓"; x["level"]=3
json.dump(x,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")