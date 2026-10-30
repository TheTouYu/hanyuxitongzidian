# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards"); G=os.path.join(ROOT,"web","public","glyphs"); P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷四  弋.docx"); ps=[p.text.strip() for p in doc.paragraphs]; parts=doc.part.related_parts
def kd(b): return "png" if b[:4]==b"\x89PNG" else ("emf" if b[:4]==b"\x01\x00\x00\x00" else ("jpg" if b[:2]==b"\xff\xd8" else "bin"))
def blobs(k):
    out=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                try: out.append(parts[rid[0]].blob)
                except KeyError: pass
    return out
# 字形行拆分：13 戠 + 1 熾
gb=blobs(299); split=[("戠",gb[:13]),("熾",gb[13:14])]
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chars=idx.get("chars") or idx
for ch,imgs in split:
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    names=[]
    for i,b in enumerate(imgs,1):
        fn="%02d.%s"%(i,kd(b)); open(os.path.join(d,fn),"wb").write(b); names.append(fn)
    e=chars.get(ch) or {"doc":"","variants":[]}; e["files"]=names; chars[ch]=e
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
sec={}
cur=None
for k in range(300,307):
    t=ps[k]
    if not t: continue
    for key,pre in (("benyi","本義"),("zhuanyi","轉義"),("bianzheng","辯證"),("yinyuan","音源")):
        if t.startswith(pre):
            cur=key; sec[cur]=[re.sub(r"^%s[：:]?"%pre,"",t)]; break
    else:
        if cur: sec[cur].append(t)
rows=[("幟（𢂴旘帜志）","chì、zhì","巾","《說文》：「旌旗之屬。从巾戠聲。昌志切。」《集韻》：「旗也。或作織、旘、𢂴。亦作志。」《玉篇》：「巾也。」《康典》：「記也。」《字詁》：「標也。」","zh「凿总」取「总」：旗幟總聚而標識（推）。"),
("識（誌识）","shí、zhì","言","《說文》：「常也。一曰知也。从言戠聲。賞職切。」旗幟。知識。《玉篇》：「認識也。」zhì，《釋名》：「識，幟也。有章幟可按視也。」《集韻》：「誌也。或作識。」加上標記。","sh「失收」取「收」：記而收存於心（推）。"),
("職（职樴𣖿）","zhí、tè","耳","《說文》：「記微也。从耳戠聲。之弋切。」識；記。《爾雅》：「主也。」《增韻》：「職掌也。」主宰；掌管。《廣雅》：「事也。業也。」職務；職業。","zh「凿总」取「凿」：記事鑿定職守（推）。"),
("軄","zhí","身","《玉篇》：「俗職字。」身份，職業。","zh「凿总」取「凿」：同職（推）。"),
("樴（杙）","zhí、yì","木","《說文》：「弋也。从木戠聲。之弋切。」小木樁。《玉篇》：「杙也，所以繋牛。」《集韻》：「杙，《說文》：『劉杙。』或作樴、職。」果木名。","zh「凿总」取「凿」：木樁鑿入地（推）。"),
("織（织𥿮）","zhī","糸","《說文》：「作布帛之緫名也。从糸戠聲。𥿮，樂浪挈令織。从糸从式。之弋切。」紡織。","zh「凿总」取「总」：絲線總聚而織（推）。"),
("膱","zhí","肉","《集韻》：「脯脡也。長尺有二寸。」乾肉。《玉篇》：「肉敗也。」《廣雅》：「臭也。」","zh「凿总」取「凿」：乾肉長條如鑿痕（推）。"),
("熾（𢧾炽）","chì","火","《說文》：「盛也。从火戠聲。，古文熾。昌志切。」火旺盛。指炊煮時，柴薪燃燒的樣子。","ch「刺持」取「刺」：火刺而盛（推）。"),
("蘵（𧄕）","zhī","艸","《爾雅·釋草》：「黃蒢。」郭璞注：「蘵草，葉似酸漿。華小而白，中心黄。江東以作菹食。」《顏氏家訓》：「江南有苦菜，葉似酸漿，花或紫或白，子大如珠，熟時或赤或黑。此菜可以釋勞。」","zh「凿总」取「凿」：草莖直鑿而出（推）。"),
("蟙（𧊖）","zhí","虫","《集韻》：「蟙䘃，蟲名，蝙蝠也。或从式。」《本草》：「（蟹）其殼闊而多黄者名蟙。生南海中，其螯最鋭，斷物如芟刈也。」今指高腳蟹。為世界上最大的蟹。","zh「凿总」取「凿」：螯如鑿斷物（推）。")]
HAN=re.compile(r"[\u3400-\u9fff\U00020000-\U0002A6DF]")
def aliases(head,ch):
    m=re.search(r"（([^）]+)）",head); return sorted({x for x in HAN.findall(m.group(1)) if x!=ch}) if m else []
head={"char":"戠","head":"戠（𧧬）","pinyin":"zhī","level":1,"bus":[{"num":31,"name":"戠"}],
 "aliases":["𧧬"],
 "sections":[{"key":"benyi","label":"本义","text":"\n".join(sec.get("benyi",[])),"cites":[]},
  {"key":"zhuanyi","label":"转义","text":"\n".join(sec.get("zhuanyi",[])),"cites":[]},
  {"key":"bianzheng","label":"辩证","text":"\n".join(sec.get("bianzheng",[])),"cites":[]},
  {"key":"yinyuan","label":"音源","text":"\n".join(sec.get("yinyuan",[])),"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"zh「凿总」取「凿」：戈刻言而生記號（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"",
   "groups":[{"title":"①指印記，表示標記、旗幟、職業","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[:4]]},
             {"title":"②指疤痕，表示乾硬的長條","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[4:]]}]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
# 插图
def photo(par,ch,cap):
    b=[x for x in blobs(par) if len(x)>30000]
    if not b: return
    d=os.path.join(P,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d): os.remove(os.path.join(d,f))
    fn="01."+kd(b[0]); open(os.path.join(d,fn),"wb").write(b[0])
    ip=os.path.join(P,"index.json"); i=json.load(io.open(ip,encoding="utf-8")); ph=i.get("photos") or i; ph[ch]=[fn]
    json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
    cp=os.path.join(P,"captions.json"); c=json.load(io.open(cp,encoding="utf-8")); cm=c.get("captions") or c
    cm[ch]=[cap]; json.dump({"captions":cm},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
    return fn
f1=photo(301,"戠","長條疤痕")
head["photos"]=["01.png"] if f1 else []
head["captions"]=["長條疤痕"] if f1 else []
json.dump(head,io.open(os.path.join(C,"戠.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
made=0
for r in rows:
    bare=HAN.findall(r[0])[0]; f=os.path.join(C,bare+".json")
    d={"char":bare,"head":r[0],"pinyin":r[1],"level":3,"parent":"戠","bus":[{"num":31,"name":"戠"}],"aliases":aliases(r[0],bare),
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
        {"key":"shengmu","label":"声母拟态","text":r[4],"cites":[]},
        {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷四弋","label":"卷四 弋"}]}]}
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); made+=1
photo(320,"蟙","高腳蟹")
print("family",made,"headphoto",f1)