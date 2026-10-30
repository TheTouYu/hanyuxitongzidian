# -*- coding: utf-8 -*-
import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def W(ch,py_,secs):
    d={"char":ch,"trad":ch,"simp":"","pinyin":py_,"level":2,"parent":"欠","bus":[{"num":5,"name":"欠"}],"sections":secs}
    json.dump(d,open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
W("㤅","ài",[
{"key":"benyi","label":"本义","text":"「愛」與「㤅」本同一字；戰國古文从心旡聲——旡即欠，張著口的樣子，从心指心理活動（《集韻》「㤅，或作愛，古作𢟪、𢛭」）。","cites":[]},
{"key":"zhuanyi","label":"转义","text":"由心裡想得到、據為己有，引申為喜歡、愛好、吝惜（《字彙》「好樂也、吝也」，《正韻》「親也、恩也、惠也、憐也、寵也」）；或專指男女情愛。","cites":[]},
{"key":"bianzheng","label":"辩证","text":"戰國古文或加「夊」，小篆从之，故《說文》「愛，行皃。从夊，㤅聲」所析不確。","cites":[]},
{"key":"shengmu","label":"声母拟态","text":"零聲母（今读 ài）：緒論七組未列，不系——照实。","cites":[]},
{"key":"zizu","label":"字族衍义","text":"多指心中之愛、隱蔽、昏暗、茂盛、珍愛（另卡）。","cites":[]}])
W("疑","yí",[
{"key":"benyi","label":"本义","text":"甲骨文象人站著張開大口，指因驚疑而張口結舌之狀，本與「欠」同源；《廣韻》「不定也、恐也、惑也、嫌也」。","cites":[]},
{"key":"zhuanyi","label":"转义","text":"由疑惑不動，引申為安定、停止、凝聚：níng《正韻》「魚陵切，音凝，定也」，《集韻》「正立自定皃」。","cites":[]},
{"key":"bianzheng","label":"辩证","text":"小篆訛張口之狀為「匕」、人身之狀為「矢」，故《說文》「𠤗，未定也，从𠤎𠤕聲」「疑，惑也，从子止匕，矢聲」析形皆不確。","cites":[]},
{"key":"shengmu","label":"声母拟态","text":"y 零聲母：緒論未列，不系（照实）；níng 一讀 n「纳弄」取「纳」：疑而止、納而定（推）。","cites":[]},
{"key":"zizu","label":"字族衍义","text":"多指疑惑、擬度、高峻、凝定（另卡）。","cites":[]}])
W("贛","gàn",[
{"key":"benyi","label":"本义","text":"从貝从章从欠（或省貝、或省章）：貝指貝類，章指紅色，欠指張著口——本義當指一種外殼呈紅色的蚌，疑即河蚌（三角帆蚌、珍珠蚌）。","cites":[]},
{"key":"zhuanyi","label":"转义","text":"因其狀如鼓，或引申指鼓（pàng《集韻》「𥪴，鼓聲」）；或引申指蠢笨（zhuàng、hòng、gòng《集韻》「呼貢切，與戇同，愚也」）。","cites":[]},
{"key":"bianzheng","label":"辩证","text":"戰國古文「夊、欠」形近，故誤「欠」為「夅」；《說文》「賜也，从貝竷省聲」形義皆不確。","cites":[]},
{"key":"yinyuan","label":"音源","text":"本「欠」聲，故義音同「欠」：《詩·小雅·伐木》「坎坎鼓我」，《釋文》「坎，《說文》作竷」。","cites":[]},
{"key":"shengmu","label":"声母拟态","text":"g「隔估」取「隔」：蚌殼隔閉而藏珠（推）。","cites":[]},
{"key":"zizu","label":"字族衍义","text":"多指紅色蚌、鼓、愚戇、貢賜（另卡）。","cites":[]}])
print("3 二级字根卡已建：㤅/疑/贛")