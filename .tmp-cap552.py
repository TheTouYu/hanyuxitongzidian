# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\系统汉字\web\public\..\..\字谱智能体\卷二  㠯.docx".replace(r"\web\public\..\..","")) .paragraphs]
def S(k,l,t,g=None):
    s={"key":k,"label":l,"text":t,"cites":[]}
    if g is not None: s["groups"]=g
    return s
J={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷二㠯","label":"卷二 㠯"}]}
rows=[["礩","zhì","石","《新附》「柱下石也」柱下石墩，取質之墊底義"],
["躓（胝疷䟡）","zhì","足","《說文》「跲也」被東西絆倒，取質之阻塞義"],
["櫍","zhì","木","《新附》「柎也」鐘鼓架腳，取質之墊底義"],
["劕","zhì","刀","《廣韻》「劕劑，券也」票券，取質之券書義"],
["𧸲","zhì","貝","《篇韻》「當也」抵押，取質之抵押義"],
["鑕","zhì","金","《玉篇》「鐵鑕砧」腰斬刑具墊座，取質之墊底義"],
["懫","zhì","心","《集韻》「忿戾也」憤恨；《玉篇》「止也、塞也」阻塞"],
["䑇","zhì","肉","《玉篇》「刀箭瘡藥」金瘡藥"],
["𨏑","zhì","車","《字彙》「車前重也」車前重載"],
["𩧄","zhì","馬","《集韻》「馬名」"],
["𠘖（𤁩）","zhì","冫","《集韻》「身寒皃」冷得發抖"],
["𡂒（䜠）","zhì","口","《說文》「野人言之」語言粗俗直率"],
["儨","zhì","人","《篇海》「正也」"],
["㜱","zhì","女","《集韻》「女字」"],
["瓆","zhì","玉","《集韻》「人名」"],
["啠（哲）","zhé","口","《龍龕》「啠，俗；哲，正」智也"],
["𧓳（蛭）","zhì","虫","《正字通》「俗蛭字」螞蟥，取斧之鋒利義"]]
g=[{"title":"①指抵押，表示墊底、阻塞","note":"","rows":rows[:11]},
   {"title":"②指質用，表示質樸、明智","note":"","rows":rows[11:16]},
   {"title":"③指斧的鋒利","note":"","rows":rows[16:]}]
z={"char":"斦","head":"斦（質）","pinyin":"zhì","level":1,"parent":"","bus":[{"num":15,"name":"斦"}],
 "sections":[S("benyi","本义",ps[749+1]),
  S("zhuanyi","转义",ps[750]+ps[751]+ps[752]+ps[753]+ps[754]),
  S("bianzheng","辩证",ps[756]),
  S("yinyuan","音源",ps[757]),
  S("shengmu","声母拟态","zh「凿总」取「凿」：二斤相疊，斧刃犀利如鑿（推）。"),
  S("zizu","字族衍义","原文字族衍義三組：",g),J],
 "aliases":["質","质"]}
json.dump(z,io.open(os.path.join(C,"斦.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
def head(s):
    m=re.match(r"^([^\s（(《a-zA-Z]{1,2})(（([^）]*)）)?\s*[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]+",s)
    return m
for r in rows:
    ch=re.sub(r"（.*?）","",r[0]); par=re.search(r"（(.*?)）",r[0])
    body=None
    for k in range(760,790):
        if k<len(ps) and ps[k].startswith(ch): body=ps[k]; break
    d={"char":ch,"head":r[0],"pinyin":re.search(r"[a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+",r[0]) and re.search(r"[a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+",r[0]).group(0) or "",
       "level":3,"parent":"斦","bus":[{"num":15,"name":"斦"}],
       "sections":[S("shiyi","释义",body or r[3]),S("shengmu","声母拟态","zh「凿总」取「凿」：取質之斧刃義一面（推）。"),J],
       "aliases":list(par.group(1)) if par else []}
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("斦部卡 +",len(rows))