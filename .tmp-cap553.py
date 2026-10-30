# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
ps=[p.text.strip() for p in Document(r"D:\字谱智能体\卷二  㠯.docx").paragraphs]
def strip(t):
    for q in ("本義：","轉義：","辯證：","音源："):
        if t.startswith(q): return t[len(q):].lstrip()
    return t
def S(k,l,t,g=None):
    s={"key":k,"label":l,"text":t,"cites":[]}
    if g is not None: s["groups"]=g
    return s
J={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷二㠯","label":"卷二 㠯"}]}
rows=[["礩","zhì","石",ps[760]],["躓（胝疷䟡）","zhì","足",ps[761]],["櫍","zhì","木",ps[762]],
["劕","zhì","刀",ps[763]],["𧸲","zhì","貝",ps[764]],["鑕","zhì","金",ps[765]],
["懫","zhì","心",ps[768]],["䑇","zhì","肉",ps[769]],["𨏑","zhì","車",ps[770]],
["𩧄","zhì","馬",ps[771]],["𠘖（𤁩）","zhì","冫",ps[772]],
["𡂒（䜠）","zhì","口",ps[774]],["儨","zhì","人",ps[775]],["㜱","zhì","女",ps[776]],
["瓆","zhì","玉",ps[777]],["啠（哲）","zhé","口",ps[778]],["𧓳（蛭）","zhì","虫",ps[780]]]
g=[{"title":"①指抵押，表示墊底、阻塞","note":"","rows":rows[:11]},
   {"title":"②指質用，表示質樸、明智","note":"","rows":rows[11:16]},
   {"title":"③指斧的鋒利","note":"","rows":rows[16:]}]
z={"char":"斦","head":"斦（質）","pinyin":"zhì","level":1,"parent":"","bus":[{"num":15,"name":"斦"}],
 "sections":[S("benyi","本义",strip(ps[749])),S("zhuanyi","转义",strip(ps[750+0])+strip(ps[751])+strip(ps[752])+strip(ps[753])+strip(ps[754])),
  S("bianzheng","辩证",strip(ps[756])),S("yinyuan","音源",strip(ps[757])),
  S("shengmu","声母拟态","zh「凿总」取「凿」：二斤相疊，斧刃犀利如鑿（推）。"),
  S("zizu","字族衍义","原文字族衍義三組：",g),J],"aliases":["質","质"]}
json.dump(z,io.open(os.path.join(C,"斦.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for r in rows:
    ch=re.sub(r"（.*?）","",r[0]); par=re.search(r"（(.*?)）",r[0])
    d={"char":ch,"head":r[0],"pinyin":r[1],"level":3,"parent":"斦","bus":[{"num":15,"name":"斦"}],
       "sections":[S("shiyi","释义",r[3]),S("shengmu","声母拟态","zh「凿总」取「凿」：取質之斧刃鋒利義一面（推）。"),J],
       "aliases":list(par.group(1)) if par else []}
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("斦部：1 头 +",len(rows),"子")