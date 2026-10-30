# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
D=[("脃","cuì",[("benyi","本义","脃，cuì：《說文》「小耎易斷也。从肉从絕省。此芮切。」《集韻》「耎易破也。或作脺。」《正字通》「輕也。」脆弱、易斷。俗作「脆」。"),("bianzheng","讹字说明","原稿列為「形近字『危、巵、兌、包』之訛」：脃所从之「危」形近而訛；正字作脃，今通行「脆」。")]),
("𡜆","yuē",[("benyi","本义","𡜆，yuē：《字彙》「同𡡕」。𡡕，《玉篇》「𡜴肥皃」，《廣韻》「嬄𡡕，婦人皃」，《正字通》「㛂字之譌」；㛂，《集韻》「《說文》：婐㛂也。一曰弱也。好也」，《廣韻》「委皃也」。"):(None,None,None)] if False else [("benyi","本义","𡜆，yuē：《字彙》「同𡡕」。𡡕，《玉篇》「𡜴肥皃」，《廣韻》「嬄𡡕，婦人皃」；《正字通》以為「㛂字之譌」，㛂有弱、好、委皃之義。"),("bianzheng","讹字说明","原稿列為「形近字『危、巵、兌、包』之訛」：此字所从形近「包」，當是形訛。")]),
("栬","zuì",[("benyi","本义","栬，zuì：《集韻》「祖芮切。小杙。」小木樁。《正字通》「俗字。小杙不名栬」，疑為「梔」字之訛。"),("bianzheng","讹字说明","原稿列為「形近字『危、巵、兌、包』之訛」；《正字通》疑為「梔」之訛。")]),
("𧧘","shuì",[("benyi","本义","𧧘，shuì：《正字通》「說字之訛。」即「說」的訛字。"),("bianzheng","讹字说明","原稿列為「形近字『危、巵、兌、包』之訛」；《正字通》直言「說字之訛」。")]),
("𨋭","páo",[("benyi","本义","𨋭，páo：《廣雅》「軫𨋭，轉戾也」，身子勾曲。《正字通》「譌字」；王念孫疏證：「軳（páo），曹憲音牛力反。各本軳譌作𨋭，自宋時本已然。」"),("bianzheng","讹字说明","原稿列為「形近字『危、巵、兌、包』之訛」；王念孫謂「軳」之譌。")])]
n=0
for ch,py_,secs in D:
    d={"char":ch,"trad":ch,"simp":"","pinyin":py_,"level":3,"parent":"色","bus":[{"num":10,"name":"示"}],"sections":[]}
    for k,l,t in secs: d["sections"].append({"key":k,"label":l,"text":t,"cites":[]})
    d["sections"].append({"key":"shengmu","label":"声母拟态","text":"形訛字不系声母義：本字既属訛形，不当以声母比拟附会（推）。","cites":[]})
    json.dump(d,io.open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cards",n)