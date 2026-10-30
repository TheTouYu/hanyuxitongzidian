# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
D=[
 ("赩","xì","《新附》：「大赤也。从赤、色，色亦聲。許力切。」《玉篇》：「怒皃。」","x「续消」取「续」：赤色延续而消（推）。"),
 ("𨠶","yí","《龍龕》：「𨠶，誤；𨠑，正。音移。飲酒也。」《集韻》：「酡，飲而赭色著面。或作𨠑。」飲酒而臉紅。","y 零声母一系（yí），绪论七组未列，不系（推）。"),
 ("𢙚","xī","《龍龕》：「忚，或作；𢚚，正。呼兮反。欺慢之皃也。」liě，《集韻》：「忚忚，心不欲。」","x「续消」取「消」：慢心渐消（推）。")]
for ch,py_,benyi,sm in D:
    d={"char":ch,"trad":ch,"simp":"","pinyin":py_,"level":3,"parent":"色","bus":[{"num":10,"name":"示"}],
       "sections":[{"key":"benyi","label":"本义","text":benyi,"cites":[]},
                   {"key":"shengmu","label":"声母拟态","text":sm,"cites":[]}]}
    json.dump(d,io.open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cards",len(D))