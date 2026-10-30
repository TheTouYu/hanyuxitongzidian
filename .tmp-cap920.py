# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
def W(ch,d):
    d.setdefault("char",ch); d.setdefault("rootLevel", d.get("rootLevel",3 if d.get("level")==3 else 1))
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
G=[("蚇","chǐ","虫","《唐韻》「蚇蠖，蟲名」；尺蠖蛾幼蟲，行動一屈一伸如量尺，故从虫"),
   ("伬","chǐ","人","古代工尺譜記音符號，相當簡譜「２」的高音；尺聲記音"),
   ("訳","yì","言","同「譯」；尺聲（𥝌省）記音"),
   ("𧺫","qǐ","走","《漢典》「同『起』」；尺聲記音"),
   ("釈","shì","釆","同「釋」；尺聲記音"),
   ("呎","chǐ","口","「英尺」舊稱，英美制長度單位，一呎十二英寸，約合市尺九寸一分四厘；尺聲兼取尺量義")]
W("尺",{"char":"尺","pinyin":"chǐ","level":2,"parent":"尸","bus":[{"num":17,"name":"尸"}],
 "sections":[
  {"key":"benyi","label":"本义","text":"尺：戰國籀文从「尸」足部加標記，象事指膝蓋以下到腳踝這一截「尺骨」，其長度與手腕紋至肘紋相當，故這段骨頭叫「尺骨」，反映先民以人體為度量（臺灣故宮藏商代骨尺長約 16.9 厘米）。","cites":[]},
  {"key":"zhuanyi","label":"转义","text":"由小腿長度引申指量尺度：chǐ，《廣韻》「尺寸也，十寸爲尺」；又引申指工尺譜符號之一，表示音階一級，讀 chě。","cites":[]},
  {"key":"bianzheng","label":"辩证","text":"《說文》「十寸也…从尸从乙」析形不確：从「乙」者非指識記，而是尸足標記之形變；十寸為尺是後起度量，非字理本義。","cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"ch「刺持」取「持」：手持尺骨量物，分寸持定（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"指尺量义：","groups":[{"title":"指尺量义","note":"","rows":[[a,b,c,d] for a,b,c,d in G]}]},
  {"key":"suoshu","label":"所属卷","text":"卷三 矢（第17部 尸）","cites":[]}]})
D={"蚇":("chǐ","尺蠖蛾的幼蟲，爬行時身體一屈一伸，如用尺量物。","《唐韻》「蚇蠖，蟲名」。"),
   "伬":("chǐ","古代工尺譜的記音符號，相當於簡譜「２」的高音。","原文只記工尺譜符號，尺聲記音。"),
   "訳":("yì","同「譯」。","《漢典》「同『譯』」，尺聲記音。"),
   "𧺫":("qǐ","同「起」。","《漢典》「同『起』」，尺聲記音。"),
   "釈":("shì","同「釋」。","《漢典》「同『釋』」，尺聲記音。"),
   "呎":("chǐ","英尺的舊稱，英美制長度單位，一呎十二英寸，約合市尺九寸一分四厘。","尺聲兼取尺量之義，从口者譯音之記號。")}
for ch,(py,shi,yuan) in D.items():
    W(ch,{"char":ch,"pinyin":py,"level":3,"parent":"尺","rootLevel":3 if False else 3,"bus":[{"num":17,"name":"尸"}],
      "sections":[{"key":"shiyi","label":"释义","text":f"{ch}{py}：{yuan}{shi}","cites":[]},
                  {"key":"shengmu","label":"声母拟态","text":"ch「刺持」取「持」：尺量分寸，持而度之（推）。","cites":[]},
                  {"key":"suoshu","label":"所属卷","text":"卷三 矢（第17部 尸）","cites":[]}]})
W("屍",{"char":"屍","pinyin":"shī","level":3,"parent":"尸","bus":[{"num":17,"name":"尸"}],
 "sections":[{"key":"shiyi","label":"释义","text":"屍shī《說文》：「終主。从尸从死。式脂切。」屍體。《玉篇》：「在牀曰屍。」shì，《集韻》：「矢利切。似皴皃。」","cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"sh「失收」取「失」：生機已失，形骸收存（推）。","cites":[]},
  {"key":"suoshu","label":"所属卷","text":"卷三 矢（第17部 尸）","cites":[]}]})
p=os.path.join(C,"尸.json"); d=json.load(io.open(p,encoding="utf-8"))
for s in d["sections"]:
    if s["key"]=="zizu":
        s.setdefault("groups",[]).append({"title":"本部二级字根","note":"尺：量尺，从尸足部标记；字族 6 字（蚇/伬/訳/𧺫/釈/呎）","rows":[["尺","chǐ","尸","膝下至踝之尺骨，引申为量尺"]]})
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")