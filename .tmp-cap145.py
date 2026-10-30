# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
M={
"脂":"zh「凿总」取「总」：有角動物的脂肪總聚於肉中，滑而潤。",
"𩊝":"zh「凿总」取「总」：皮繩圍束車蓋杠柄，總束而不散。",
"鴲":"zh「凿总」取「凿」：小靑雀之喙尖而光滑如凝脂，能啄刺。",
"㞓":"q「亲缺」取「缺」：臀部肉厚而中凹成溝（推）。",
"鮨":"q「亲缺」取「缺」：魚醬醃貯發酵，味缺而後鮮（推）。",
"酯":"zh「凿总」取「总」：脂肪主成分，甘油與脂肪酸總合而成。",
"𪊨（麂）":"j「聚决」取「聚」：麂皮毛細軟，毛總聚而密（推）。",
"恉":"zh「凿总」取「总」：意圖總聚於心。",
"指":"zh「凿总」取「凿」：手指指端尖，能指能刺。",
"䭬":"q「亲缺」取「缺」：叩頭至地，首低就下而至缺處（推）。",
"詣":"y 为零声母，绪论七组未列，不系（照实）。",
"栺":"y 为零声母，绪论七组未列，不系（照实）。"}
for raw,txt in M.items():
    ch=raw.split("（")[0]
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): print("缺卡",ch); continue
    d=json.load(io.open(p,encoding="utf-8")); secs=d["sections"]
    if any(s.get("key")=="shengmu" for s in secs):
        for s in secs:
            if s.get("key")=="shengmu": s["text"]=txt
    else: secs.append({"key":"shengmu","label":"声母拟态","text":txt,"cites":[]})
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("已改",len(M))