# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
D={
"㞷":dict(pinyin="huáng",bus=(517,"王"),benyi="《說文》「艸木妄生也。从之在土上。讀若皇。戶光切」；徐鍇曰：「妄生謂非所宜生。」（原稿注：所析不確，本从止从土）",sm="h「豁活」取「活」：草木非時而妄生，勃然自活。"),
"㠱":dict(pinyin="jì",bus=(391,"丌"),benyi="《說文》「長踞也。从己其聲。讀若杞。暨己切」；《玉篇》「長跪也。或作跽」；《集韻》「古國名」。",sm="j「聚决」取「聚」：盤腳長踞，身聚而不伸。"),
}
for ch,d in D.items():
    card={"char":ch,"pinyin":d["pinyin"],"level":3,"parent":d["bus"][1],"bus":[{"num":d["bus"][0],"name":d["bus"][1]}],
     "sections":[{"key":"benyi","label":"释义","text":d["benyi"],"cites":[]},
                 {"key":"shengmu","label":"声母拟态","text":d["sm"],"cites":[]}]}
    json.dump(card,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("建",ch)