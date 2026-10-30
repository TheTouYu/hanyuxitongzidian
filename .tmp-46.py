# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def W(ch,obj):
    json.dump(obj,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
shuo=W
tuo={
 "char":"乇","head":"乇（𠂌）","pinyin":"zhé/tuō","level":1,"bus":{"num":46,"name":"乇"},
 "sections":[
  {"key":"benyi","label":"本义","text":"甲骨文為“又”字表手腕的部分朝上，表示手掌朝上托举之意。“托（tuō）”的初文，《集韵》：“拓，手推物。或作𢸨、托。”","cites":[]},
  {"key":"zhuanyi","label":"转义","text":"由手托舉時的手掌張開之狀，引申指張開。此義分化如“厇（zhé）”，《集韻》：“張也。”或引申指草木的葉子。zhé，《玉篇》：“草葉也。”\n由對物的托舉，引申指寄託、委託。tuō，《六書正訛》：“乇，借為寄乇、委乇字。”","cites":[]},
  {"key":"bianzheng","label":"辩证","text":"《說文》：“艸葉也。从垂穗，上貫一，下有根。象形。凡乇之屬皆从乇。陟格切。”析形不確。","cites":[]},
  {"key":"yinyuan","label":"音源","text":"借音字。因手掌較硬，而義音同“石”：《集韻》：“拓，手推物。或作𢸨、托。”","cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"zh「凿总」取「凿」：掌上托物，如凿之向上頂托（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"②指托舉，表示負載、挺舉、依憑；②指托掌狀，表示張開；③指手掌，同“石”，表示敲擊、硬實；④形近字“屯、乏”之訛。","cites":[]},
  {"key":"suoshujuan","label":"所属卷","text":"卷七 斤（第46部 乇）","links":[{"ch":"卷七斤","label":"卷七 斤"}]},
 ]}
zhai={
 "char":"宅","head":"宅（𡧪㡯厇垞𡊾𡧜度）","pinyin":"zhái","level":2,"parent":"乇","bus":{"num":46,"name":"乇"},
 "sections":[
  {"key":"benyi","label":"本义","text":"从宀乇聲。“宀”，指房子；“乇”，指托身。象意寄託身軀的地方，即住宅、屋舍。zhái，《釋名》：“宅，擇也，擇吉處而營之也。”《說文》：“所托也。从宀乇聲。，古文宅。，亦古文宅。場伯切。”《玉篇》：“人之居舍曰宅。”","cites":[]},
  {"key":"zhuanyi","label":"转义","text":"由屋宅引申指居住、存身、寄託。《爾雅》：“居也。”或引申指墳墓。《廣雅》：“葬地也。”\n由托身之所，引申指禁錮。zhà，《集韻》：“懲也。”或引申指法度。dù，《集韻》：“度，徒故切。《說文》：‘法制也。’亦姓。或作㡯、宅。”\n“乇”本引申有張開之意，故“宅”也或引申指開裂。chè，《類篇》：“裂也。”","cites":[]},
  {"key":"bianzheng","label":"辩证","text":"因戰國古文“宀”或作“厂”，跟“石”的初文近似，故或混同“度”。“度”本指用手拿石頭揣度，甲骨文作（參見45《石部》）。\n不過，“乇、石”本音義可通。究竟屬于什麼情況，仍待考。","cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"zh「凿总」取「凿」：托身之處如凿穴而居（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"①指托掌，表示張開、裂開；②指托身，表示寄託、托舉；③與“度”同，指揣度。","cites":[]},
  {"key":"suoshujuan","label":"所属卷","text":"卷七 斤（第46部 乇）","links":[{"ch":"卷七斤","label":"卷七 斤"},{"ch":"乇","label":"46 乇"}]},
 ]}
W("乇",tuo); W("宅",zhai)
print("written 乇 宅")