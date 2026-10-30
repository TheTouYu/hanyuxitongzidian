# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
D=[]
D.append(("脃","cuì","脃，cuì：《說文》「小耎易斷也。从肉从絕省。此芮切。」《集韻》「耎易破也。或作脺。」《正字通》「輕也。」脆弱、易斷；俗作「脆」。","原稿列為「形近字『危、巵、兌、包』之訛」：脃所从與「危」形近而訛，今通行作「脆」。"))
D.append(("𡜆","yuē","𡜆，yuē：《字彙》「同𡡕」。𡡕，《玉篇》「𡜴肥皃」，《廣韻》「嬄𡡕，婦人皃」；《正字通》以為「㛂字之譌」，㛂有弱、好、委皃之義。","原稿列為「形近字『危、巵、兌、包』之訛」：所从形近「包」，當是形訛。"))
D.append(("栬","zuì","栬，zuì：《集韻》「祖芮切。小杙。」小木樁。《正字通》「俗字。小杙不名栬」，疑為「梔」字之訛。","原稿列為「形近字『危、巵、兌、包』之訛」；《正字通》疑為「梔」之訛。"))
D.append(("𧧘","shuì","𧧘，shuì：《正字通》「說字之訛。」即「說」的訛字。","原稿列為「形近字『危、巵、兌、包』之訛」；《正字通》直言「說字之訛」。"))
D.append(("𨋭","páo","𨋭，páo：《廣雅》「軫𨋭，轉戾也」，身子勾曲。《正字通》「譌字」；王念孫疏證：「軳（páo），曹憲音牛力反。各本軳譌作𨋭，自宋時本已然。」","原稿列為「形近字『危、巵、兌、包』之訛」；王念孫謂「軳」之譌。"))
n=0
for ch,py_,benyi,ezi in D:
    d={"char":ch,"trad":ch,"simp":"","pinyin":py_,"level":3,"parent":"色","bus":[{"num":10,"name":"示"}],"sections":[
      {"key":"benyi","label":"本义","text":benyi,"cites":[]},
      {"key":"bianzheng","label":"讹字说明","text":ezi,"cites":[]},
      {"key":"shengmu","label":"声母拟态","text":"形訛字不系声母義：本字既属訛形，不以声母比拟附会（推）。","cites":[]}]}
    json.dump(d,io.open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cards",n)