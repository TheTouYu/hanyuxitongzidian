# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def mk(ch,py_,benyi,sm,parent="色",lvl=3,trad=None):
    d={"char":ch,"trad":trad or ch,"simp":"","pinyin":py_,"level":lvl,"parent":parent,"bus":[{"num":10,"name":"示"}],
       "sections":[{"key":"benyi","label":"本义","text":benyi,"cites":[]},{"key":"shengmu","label":"声母拟态","text":sm,"cites":[]}]}
    json.dump(d,io.open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
mk("𨛉","jì","《奚韻》：「具義切。山名。」","j「聚决」取「聚」：山聚而立（推）。")
mk("灔","yàn","《集韻》：「瀲灩，水滿皃。或从臽。亦作淡。」「瀲灩，水動皃。」《正字通》：「舊註灎本字，不知六書本作𤅿，灩與灧皆俗增。」水閃閃發光。","y 零声母，不系（推）。")
mk("艷","yàn","《集韻》：「豔，《說文》：『好而長也。从豐，豐，大也。』引《春秋傳》：『美而豔。』隷作艷。」《玉篇》：「美也、好色也。俗作艶。」《增韻》：「歆羨也。」色彩鮮明、羨慕、關于愛情的、美麗，亦指美女。","y 零声母，不系（推）。")
for ch,main,note in [("灩","灔","俗增字"),("滟","灔","簡化字"),("𤅿","灔","本字"),("淡","灔","或作"),("淊","灔","或作"),
                     ("豔","艷","隷作本字"),("豓","艷","異體"),("𡤩","艷","異體"),("艳","艷","簡化字")]:
    mk(ch,"yàn",f"「{main}」的{note}（原稿字頭括注）。《集韻》《玉篇》釋義同「{main}」：色彩鮮明、美豔。","y 零声母，不系（推）。",parent=main,trad=main)
print("done")