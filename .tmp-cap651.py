# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})(（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)")
M={"膣":"zh「凿总」取「凿」：肉生而窒塞如鑿（推）。","胵":"ch「刺持」取「持」：鳥胃盛食而持（推）。",
"姪":"zh「凿总」取「凿」：兄之女，血脈鑿定（推）。","侄":"zh「凿总」取「凿」：堅固可依，鑿然不移（推）。",
"𦳙":"zh「凿总」取「总」：艸大而總茂（推）。","螲":"zh「凿总」取「凿」：螻蛄穴土如鑿（推）。",
"駤":"zh「凿总」取「凿」：馬躊躕而鑿定不前（推）。","洷":"zh「凿总」取「凿」：水名，鑿地出泉（推）。",
"輊":"zh「凿总」取「凿」：車前重後低，鑿然傾下（推）。","祬":"zh「凿总」取「凿」：敬而鑿然（推）。",
"䞃":"zh「凿总」取「凿」：抵押而鑿定（推）。","𥎹":"zh「凿总」取「凿」：短而鑿定（推）。",
"絰":"d「囤动」取「囤」：喪首戴絰，囤繞於首（推）。","𪀒":"d「囤动」取「囤」：布穀呼而囤聚（推）。",
"鵄":"ch「刺持」取「持」：鳶盤旋而持物（推）。","蛭":"zh「凿总」取「凿」：螞蟥吸盤鑿入人畜（推）。",
"銍":"zh「凿总」取「凿」：短鎌截穎如鑿（推）。","秷":"zh「凿总」取「凿」：刈禾之聲鑿然（推）。",
"挃":"zh「凿总」取「凿」：獲禾之聲鑿鑿（推）。","㨖":"zh「凿总」取「凿」：刺也，鑿而入（推）。",
"𪗻":"zh「凿总」取「凿」：齒堅相鑿（推）。","𦥊":"ch「刺持」取「持」：忿戾而持（推）。",
"咥":"x「续消」取「续」：大笑續出（推）。","𧩼":"zh「凿总」取「凿」：言語鑿然（推）。",
"眰":"d「囤动」取「囤」：目出而囤（推）。","恎":"d「囤动」取「囤」：惡性囤積（推）。",
"𩹈":"zh「凿总」取「凿」：魚名，借聲（推）。","荎":"ch「刺持」取「持」：艸名，持生（推）。"}
n=0; miss=[]
for k in range(195,225):
    t=ps[k]
    m=pat.match(t) if t else None
    if not m: continue
    ch=m.group(1)
    if ch not in M: miss.append(ch); continue
    par=re.search(r"（([^）]*)）",ch)
    d={"char":re.sub(r"（.*?）","",ch),"head":ch,"pinyin":m.group(4),"level":3,"parent":"至","bus":[{"num":16,"name":"矢"}],
       "sections":[{"key":"shiyi","label":"释义","text":t,"cites":[]},
         {"key":"shengmu","label":"声母拟态","text":M[ch],"cites":[]},
         {"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}],
       "aliases":list(par.group(1)) if par else []}
    json.dump(d,io.open(os.path.join(C,d["char"]+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("建",n,"未匹配",miss)