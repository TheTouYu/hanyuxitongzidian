# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷三  矢.docx").paragraphs]
pat=re.compile(r"^([^\s（(《a-zA-Z]{1,2})(（([^）]*)）)?\s*([a-zA-Zāáǎàēéěèīíǐìōóòūúǔùǖǘǚǜü]+)")
M={"致":"zh「凿总」取「凿」：送詣而直達，如箭鑿至（推）。",
"郅":"zh「凿总」取「凿」：縣邑鑿定其界而至（推）。",
"𨖹":"r「柔锐」取「锐」：近而至，其勢锐入（推）。",
"耋":"d「囤动」取「囤」：年八十而精氣囤聚將終（推）。",
"臷":"d「囤动」取「囤」：年之至而囤聚（推）。",
"𠊷":"zh「凿总」取「总」：會物而總聚（推）。",
"𩋴":"zh「凿总」取「凿」：履底鑿地而承足（推）。",
"晊":"zh「凿总」取「凿」：日出而大明，鑿然可見（推）。",
"垤":"d「囤动」取「囤」：蟻封之土囤聚成堆（推）。",
"室":"sh「失收」取「收」：行所止處，收足而入（推）。",
"庢":"zh「凿总」取「凿」：礙止如鑿定（推）。",
"緻":"zh「凿总」取「总」：細密而總理之（推）。",
"窒":"zh「凿总」取「凿」：塞之如鑿（推）。",
"桎":"zh「凿总」取「凿」：足械鑿定其足（推）。",
"𦤻":"zh「凿总」取「凿」：抵牾如鑿之相拒（推）。",
"㗧":"zh「凿总」取「凿」：咄呵之聲鑿然（推）。",
"峌":"d「囤动」取「囤」：高山樣而其勢囤起（推）。",
"𡼄":"d「囤动」取「囤」：山貌囤聚（推）。",
"跮":"d「囤动」取「囤」：乍前乍卻，囤於進退（推）。",
"𩋡":"sh「失收」取「收」：刀削藏刀，收刃於鞘（推）。"}
n=0
for k in range(173,196):
    t=ps[k]
    m=pat.match(t) if t else None
    if not m: continue
    ch=m.group(1)
    if ch not in M: continue
    lei=(re.search(r"从([一-龥])",t).group(1) if re.search(r"从([一-龥])",t) else "")
    par=re.search(r"（([^）]*)）",ch)
    d={"char":re.sub(r"（.*?）","",ch),"head":ch,"pinyin":m.group(4),"level":3,"parent":"至","bus":[{"num":16,"name":"矢"}],
       "sections":[{"key":"shiyi","label":"释义","text":t,"cites":[]},
         {"key":"shengmu","label":"声母拟态","text":M[ch],"cites":[]},
         {"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷三矢","label":"卷三 矢"}]}],
       "aliases":list(par.group(1)) if par else []}
    json.dump(d,io.open(os.path.join(C,d["char"]+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("至族卡",n)