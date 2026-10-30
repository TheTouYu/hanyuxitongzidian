# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\web\public\cards\炙.json"
d=json.load(io.open(p,encoding="utf-8"))
G1=[["䂹（𨹾）","suǒ","石","《說文》：“碎石磒聲。从石炙聲。所責切。”碎石墜落的聲音。不確，應同“庶”，指燒紅的石頭，先民在沒有發明出陶器之前，用燒紅的石頭煨煮食物。《正字通》：“按䂹訓石隕聲無義。一說讀若炙，燒石炙物也。”"],
    ["𣇧","zhè","日","《集韻》：“日赫。”"],
    ["𣶋","zhè","肉","《類篇》：“𦞦屬。”肉羹類。"]]
G2=[["𠶨","xī","口","《海篇》：“音希。和聲。”"],
    ["𨂂（蹠）","zhí","足","《字彙》：“與蹠同。又𨂂盭。”腳掌。《篇海》：“足履踐也。”《直音篇》：“蹠，跳也；𨂂，同上。”xuě，石土自隕。即土石被風化而墜落之意。"]]
for s in d["sections"]:
    if s.get("key")=="zizu":
        s.pop("text",None)
        s["groups"]=[{"no":1,"title":"指炙烤之狀","rows":G1},{"no":2,"title":"借聲表音","rows":G2}]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")