import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def w(ch,py_,bus,secs):
    d={"char":ch,"pinyin":py_,"level":0,"parent":"","bus":[{"num":bus[0],"name":bus[1]}],"sections":secs}
    json.dump(d,open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
w("云","yún",(451,"回"),[
 {"key":"benyi","label":"本义","text":"云，yún：象云气回转之形，云气回转（卷九十四「回」部云支）；后加「雨」繁化為「雲」，二字本一字。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"引申为言说（「云」借为曰）；古书「云」多作「曰」用。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"y 为零声母一系（今读 yún），绪论七组未列，不系（照实）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"云与雲本为一字（加雨分化），非同音借用；今「云」兼作「雲」之简化。","cites":[]}])
w("臺","tái",(0,"至"),[
 {"key":"benyi","label":"本义","text":"臺，tái：《說文》「觀，四方而高者。从至从之，从高省」；本指四方而高的台观。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"引申为台阶、官署（台省）、敬辞（台鉴）。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"t「涂突」取「突」：台高出而突（推）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"今「高台、台阶」之「台」系「臺」的简化（同音借用）：臺从至从之从高省，与「台」字形无关，仅因所从「至」与「㠯」音义相近而混（原稿台部已辨）。故臺、台分卡。","cites":[]},
 {"key":"buzhu","label":"部属待核","text":"本部号待按原稿核对（书内部号表），暂记「至」部。","cites":[]}])
w("後","hòu",(0,"夂"),[
 {"key":"benyi","label":"本义","text":"後，hòu：从彳从幺从夂，象足被绳系而落后（原稿以「𡰿」为据：「从夂𡱂聲，行促迫，緊隨人後」），本义为落在后面。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"引申为时间较晚、后代、后妃。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"h「豁活」取「活」：行迟而活（推）。","cites":[]},
 {"key":"jiezi","label":"借字说明","text":"「后」本为君王（后妃、皇后），今借作「後」之简化，属同音借用，非本字，故後、后分卡。","cites":[]},
 {"key":"buzhu","label":"部属待核","text":"部号待核，暂记「夂」部。","cites":[]}])
print("ok")