# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
W=r"D:\系统汉字\web\public"
m={"钓":["釣","鈟"],"吊":["弔"],
   "鱼":["魚"],"鸟":["鳥"],"马":["馬"],"车":["車"],"门":["門"],"见":["見"],"贝":["貝"],
   "页":["頁"],"风":["風"],"虫":["蟲"],"龙":["龍"],"龟":["龜"],"齿":["齒"],"韦":["韋"],
   "专":["專"],"义":["義"],"乐":["樂"],"乔":["喬"],"产":["產"],"亲":["親"],"仓":["倉"],
   "万":["萬"],"与":["與"],"两":["兩"],"为":["爲"],"丽":["麗"],"举":["舉"],"乡":["鄉"],
   "书":["書"],"买":["買"],"乱":["亂"],"争":["爭"],"亏":["虧"],"云":["雲"],"亚":["亞"],
   "亩":["畝"],"价":["價"],"众":["眾"],"体":["體"],"余":["餘"],"侯":["矦"],"兽":["獸"]}
json.dump(m,io.open(os.path.join(W,"cards","variants.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
json.dump(m,io.open(os.path.join(W,"variants.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cards/variants.json",len(m))