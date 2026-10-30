import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def w(ch,py_,bus,secs):
    d={"char":ch,"pinyin":py_,"level":0,"parent":"","bus":[{"num":bus[0],"name":bus[1]}],"sections":secs}
    json.dump(d,open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
B=lambda s:{"key":"buzhu","label":"部属待核","text":s,"cites":[]}
w("發","fā",(424,"癹"),[
 {"key":"benyi","label":"本义","text":"發，fā：从弓癹聲，射箭發出（《說文》「射發也」）；弓弦一响而箭出，是其本义。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"引申为出发、兴起、开掘、显现，又为发放、发达。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"f「附分」取「分」：箭离弦而分（推）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"「发」今兼作「發」（发出）与「髮」（头发）之简化：前者为真简化，后者属同音借用，故發、髮分卡。","cites":[]},
 {"key":"buzhu","label":"部属待核","text":"暂记第424部「癹」部（从弓癹聲），部号待原稿复核。","cites":[]}])
w("鬥","dòu",(468,"鬥"),[
 {"key":"benyi","label":"本义","text":"鬥，dòu：象两人徒手相搏之形，本义为争斗（《說文》「兩士相對，兵杖在後」象鬥之形）。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"引申为竞赛、拼合（斗榫）。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"d「囤动」取「动」：相搏而动（推）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"「斗」本为量器（十升），今借作「鬥」之简化，属同音借用，非本字，故鬥、斗分卡。","cites":[]}])
w("榖","gǔ",(0,"木"),[
 {"key":"benyi","label":"本义","text":"榖，gǔ：从木㱿聲，楮树（构树），树皮可造纸织布；《說文》「楮也」。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"引申为穀物之「穀」的借字（同音）。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"g「隔估」取「估」：树皮剥而估（推）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"今「谷」兼作「穀」之简化，而同音之「榖」（楮树）与「谷」（山谷）各为一字，三者不得混。","cites":[]},
 B("部号待核，暂记「木」部。")])
w("乾","gān",(361,"乙"),[
 {"key":"benyi","label":"本义","text":"乾，gān：《說文》「上出也。从乙，乙，物之達也；倝聲」；本义为向上冒出，引申为干燥。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"干燥（干湿之干）；qián 为卦名（乾坤）。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"g「隔估」取「隔」：水隔而干（推）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"今「干」借作「乾」（干燥）与「幹」（枝干）之简化，皆同音借用，非本字；干本树杈猎具。","cites":[]},
 B("暂记第361部「乙」部，部号待核。")])
w("裏","lǐ",(0,"衣"),[
 {"key":"benyi","label":"本义","text":"裏，lǐ：从衣里聲，衣物的内层（《說文》「衣內也」）。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"引申为内部、里面。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"l「拢离」取「拢」：衣裹而拢（推）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"今「里」借作「裏」之简化，属同音借用：「里」本为乡里（从田从土），非本字，故裏、里分卡。","cites":[]},
 B("部号待核，暂记「衣」部。")])
w("蜡","zhà",(194,"蟲"),[
 {"key":"benyi","label":"本义","text":"蜡，zhà：从虫昔聲，《說文》「蠅膽也」；古又为年终大祭之名（蜡祭，合聚百物而祭）。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"蜡祭；后借为「蠟」（蜂蜡、蜡烛）之简化。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"zh「凿总」取「总」：合聚百物而总（推）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"今「蜡」兼作「蠟」之简化，属同音借用：蜡本蝇胆/祭名，蠟本蜂蜡，非本字。","cites":[]}])
print("ok")