# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
T=json.load(open(r"D:\系统汉字\.tmp-yixi.json",encoding="utf-8"))
def s(k): return T[str(k)].split("：",1)[1] if "：" in T[str(k)] else T[str(k)]
Z="w「零聲母」不系：疑母字今讀零聲母，緒論七組未列（照實）。"
X="x「续消」取「续」：鵝斂翅不飛而鳴，聲氣續而不絕（推）。"
yi={"char":"義","head":"義（义羛𠌾）","pinyin":"yí","level":2,"parent":"我","bus":[{"num":36,"name":"我"}],
 "aliases":["义","羛","𠌾"],
 "sections":[
  {"key":"benyi","label":"本义","text":s(423)},
  {"key":"zhuanyi","label":"转义","text":s(426)+"\n"+s(427)},
  {"key":"shengmu","label":"声母拟态","text":Z},
  {"key":"zizu","label":"字族衍义","groups":[
    {"no":"①","title":"指儀容，表示好的、美的、法度","rows":[
      ["儀","yí","人",T[""]if False else "《說文》：“度也。从人義聲。魚羈切。”法度，威儀。同“美”。《廣韻》：“儀容。又義也、正也。”《爾雅》：“匹也。”匹配；配偶。《正字通》：“有擬度。”忖度；考慮。"],
      ["𥫃","yí","立","《廣韻》：“儀容。又義也。正也。”“止也。”《集韻》：“儀，容也、度也。亦姓。又州名。或从立。”"],
      ["嬟","yǐ","女","《集韻》：“婍嬟，好皃。”yì，《集韻》：“女字。”"],
      ["議","yì","言","《說文》：“語也。从言義聲。宜寄切。”《廣韻》：“謀也。擇也。評也。”討論。謀劃。選擇。評論。"]]},
    {"no":"②","title":"指義狀，表示角狀豎立","rows":[
      ["蟻（螘𧕶蛾𧔮蟣𧎶）","yǐ","虫","《集韻》：“螘，蟲名。《說文》：‘蚍蜉也。’或作𧕶、蟻、蛾、𧔮。”螞蟻的統稱。jǐ，《集韻》：“蟣，《說文》：‘虱之子。’”"],
      ["轙（钀）","yǐ","車","《說文》：“車衡載轡者。从車義聲。魚綺切。”車衡上貫穿韁繩的大環。整車待發。"],
      ["䣡","yí","邑","《說文》：“臨淮徐地。从邑義聲。魚羈切。”在今安徽泗縣北。"],
      ["鸃","yí","鳥","《說文》：“鵔鸃也。从鳥義聲。秦漢之初，侍中冠鵔鸃冠。魚羈切。”紅色野雞，尾羽長而美，人取以為冠飾。"],
      ["㕒（嶬）","wēi","厂","《說文》：“厜㕒也。从厂義聲。魚為切。”山峯巉岩厜㕒然者。"],
      ["礒","yǐ","石","《玉篇》：“嶔崟崎礒，石巖。”《集韻》：“石皃。”山石高聳、錯落皃。"],
      ["艤","yǐ","舟","《廣韻》：“整舟向岸。”放下船帆，桅杆露出如“義”。"],
      ["檥","yǐ","木","《說文》：“榦也。从木義聲。魚羈切。”築牆時兩端豎起的木柱。使船靠岸。"]]},
    ],
  {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
xi={"char":"羲","head":"羲（𢐱𦏁𢐯𦏡）","pinyin":"xī","level":2,"parent":"我","bus":[{"num":36,"name":"我"}],
 "aliases":["𢐱","𦏁","𢐯","𦏡"],
 "sections":[
  {"key":"benyi","label":"本义","text":s(445)},
  {"key":"zhuanyi","label":"转义","text":s(447)+"\n"+s(448)},
  {"key":"bianzheng","label":"辩证","text":s(449)},
  {"key":"shengmu","label":"声母拟态","text":X},
  {"key":"zizu","label":"字族衍义","groups":[
    {"no":"①","title":"指羲狀，表示勺子、聳立","rows":[
      ["㰕（𣛼𣟵𧕆樝𧔠）","xī","木","《玉篇》：“同𣟵。杓也，蠡爲𣟵也。”《集韻》：“蠡也。或作𧕆、樝、𧔠、㰕。”"],
      ["𢸤（𢹍）","xī","手","《集韻》：“𢹍，《博雅》：‘擊也。’或作𢸤。”"],
      ["𡾞（巇）","xī","山","《正字通》：“同巇。”巇，《玉篇》：“嶮巇，巓危也。”山巔高聳皃。"],
      ["𨏢（轙）","yǐ","車","《爾雅》：“載轡謂之轙。”車衡上貫穿韁繩的大環。"]]},
    {"no":"②","title":"指羲羽的白，表示色純、明亮","rows":[
      ["犧（犠牺戲獻）","xī","牛","《說文》：“宗廟之牲也。从牛羲聲。許羈切。”《玉篇》：“純色牛。”古代供宗廟祭祀用的純色牲。"],
      ["曦（㬢爔）","xī","日","《集韻》：“曦，赫曦，日光。或省。亦从火。”《玉篇》：“曦，日色也。”"],
      ["䂀","xī","目","《集韻》：“虛宜切，音羲。目動也。”"],
      ["𣎮","xī","月","《字彙》：“月光也。”《正字通》：“曦字之譌。”"]]},
    ],
  {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
for d in (yi,xi): json.dump(d,io.open(os.path.join(C,d["char"]+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# family cards
FC={"儀":Z,"𥫃":Z,"嬟":Z,"議":Z,"蟻":Z,"轙":Z,"䣡":Z,"鸃":Z,"㕒":"w「零聲母」不系（照實）。","礒":Z,"艤":Z,"檥":Z,
    "㰕":X,"𢸤":X,"𡾞":X,"𨏢":X,"犧":X,"曦":X,"䂀":X,"𣎮":X}
rows={r[0].split("（")[0]:r for d in (yi,xi) for g in d["sections"] if g["key"]=="zizu" for gg in g["groups"] for r in gg["rows"]}
n=0
for ch,sm in FC.items():
    r=rows.get(ch)
    c={"char":ch,"head":ch,"pinyin":(r[1] if r else ""),"level":3,"parent":("義" if any(ch in [x[0] for x in gg["rows"]] for g in [yi] for gg in g["groups"] if g["key"]=="zizu") else "羲"),
       "bus":[{"num":36,"name":"我"}],
       "sections":[{"key":"shiyi","label":"释义","text":(r[3] if r else "")},{"key":"shengmu","label":"声母拟态","text":sm},
                   {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
    json.dump(c,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
# glyph rows
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
def blobs(k):
    out=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid: out.append(parts[rid[0]].blob)
    return out
def dump(ch,bs):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d):
        if f.lower().endswith((".png",".jpg")): os.remove(os.path.join(d,f))
    out=[]
    for i,b in enumerate(bs):
        ext="png" if b[:4]==b"\x89PNG" else "jpg"
        fn="%02d.%s"%(i+1,ext); open(os.path.join(d,fn),"wb").write(b); out.append(ch+"/"+fn)
    return out
by=dump("義",blobs(422)); bx=dump("羲",blobs(444))
ix=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chs=ix["chars"]
chs["義"]["files"]=by; chs["羲"]["files"]=bx
json.dump({"chars":chs},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("cards",n,"glyphs",len(by),len(bx))