# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"; C=os.path.join(ROOT,"web","public","cards"); G=os.path.join(ROOT,"web","public","glyphs"); P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); ps=[p.text.strip() for p in doc.paragraphs]; parts=doc.part.related_parts
def kd(b): return "png" if b[:4]==b"\x89PNG" else ("emf" if b[:4]==b"\x01\x00\x00\x00" else ("jpg" if b[:2]==b"\xff\xd8" else "bin"))
def blobs(k):
    o=[]
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid:
                try: o.append(parts[rid[0]].blob)
                except KeyError: pass
    return o
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8")); chars=idx.get("chars") or idx
gb=blobs(128); d=os.path.join(G,"可"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
names=[]
for i,b in enumerate(gb,1):
    fn="%02d.%s"%(i,kd(b)); open(os.path.join(d,fn),"wb").write(b); names.append(fn)
e=chars.get("可") or {"doc":"","variants":[]}; e["files"]=names; chars["可"]=e
json.dump({"chars":chars},io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
b=[x for x in blobs(135) if len(x)>20000]
if b:
    dd=os.path.join(P,"可"); os.makedirs(dd,exist_ok=True)
    for f in os.listdir(dd): os.remove(os.path.join(dd,f))
    fn="01."+kd(b[0]); open(os.path.join(dd,fn),"wb").write(b[0])
    ip=os.path.join(P,"index.json"); i=json.load(io.open(ip,encoding="utf-8")); ph=i.get("photos") or i; ph["可"]=[fn]
    json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
    cp=os.path.join(P,"captions.json"); c=json.load(io.open(cp,encoding="utf-8")); cm=c.get("captions") or c
    cm["可"]=["斧柯"]; json.dump({"captions":cm},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
def row(k,cl,py,sm):
    t=ps[k]
    m=re.match(r"^(\S+?)"+py, t)
    h=re.sub(r"^(\S+?)(?=[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ])","",t)
    return (h.split("（")[0].split("《")[0] or h[:3], py, cl, t, sm)
rows1=[row(k,"言","gē","g「隔估」取「隔」：發聲如隔而唱（推）。") for k in (138,)]
rowsall=[(138,"哥","gē","言"),(139,"歌","gē","欠"),(140,"訶","hē","言"),(141,"哿","gě、jiā","可"),(142,"疴","kē、qià","疒"),(143,"呵","hē","口"),(144,"㱒","hē","可"),(145,"𠳊","hē","口"),(146,"㰤","hē、qiè","欠"),(147,"㗿","hé、xià","口"),
(149,"鴚","gē","鳥"),(150,"𪀉","gē、kě","鳥"),(151,"柯","kē","木"),(152,"苛","kē、hē","艸"),(153,"屙","ē","尸"),(154,"砢","luǒ","石"),(155,"坷","kě、kē","土"),(156,"蚵","hé、kè","虫"),(157,"𥰮","gě","竹"),(158,"牁","kē","片"),(159,"鈳","ē","金"),(160,"抲","hē、hè","手"),(161,"軻","kē、kě","車")]
SM={"哥":"g「隔估」取「隔」：發聲如隔而唱（推）。","歌":"g「隔估」取「隔」：長言如隔而詠（推）。","訶":"h「豁活」取「豁」：怒聲豁出（推）。","哿":"k「口控」取「口」：見可而許（推）。","疴":"k「口控」取「控」：病氣郁控（推）。","呵":"h「豁活」取「豁」：張口呵出（推）。","㱒":"h「豁活」取「豁」：聲止而豁（推）。","𠳊":"h「豁活」取「豁」：開口豁然（推）。","㰤":"h「豁活」取「豁」：笑氣豁出（推）。","㗿":"h「豁活」取「豁」：怒責豁出（推）。",
"鴚":"g「隔估」取「隔」：雁鳴如隔（推）。","𪀉":"g「隔估」取「隔」：雁鳴如隔（推）。","柯":"k「口控」取「控」：枝幹長而受控（推）。","苛":"k「口控」取「控」：小而密受控（推）。","屙":"零聲母寫法","砢":"l「拢离」取「拢」：眾石聚合（推）。","坷":"k「口控」取「控」：土不平受控（推）。","蚵":"h「豁活」取「豁」：穴處豁然（推）。","𥰮":"g「隔估」取「隔」：筍節相間（推）。","牁":"k「口控」取「控」：系舟受控（推）。","鈳":"零聲母寫法","抲":"h「豁活」取「豁」：揮斥豁出（推）。","軻":"k「口控」取「控」：車軸受控（推）。"}
rows=[]
for k,ch,py,cl in rowsall:
    sm=SM[ch]
    if sm=="零聲母寫法": sm="「零聲母」不系：零聲母，緒論七組未列（照實）。"; sm=py.split("、")[0][-1]+sm
    rows.append((ch,py,cl,ps[k],sm))
head={"char":"可","head":"可","pinyin":"kě","level":2,"parent":"丂","bus":[{"num":34,"name":"丂"}],
 "sections":[{"key":"benyi","label":"本义","text":"\n".join(ps[129:132]),"cites":[]},
  {"key":"zhuanyi","label":"转义","text":"\n".join(ps[132:134]),"cites":[]},
  {"key":"shengmu","label":"声母拟态","text":"k「口控」取「口」：張口而歌、點頭而許（推）。","cites":[]},
  {"key":"zizu","label":"字族衍义","text":"","groups":[
    {"title":"①指雁叫，表示歌唱、呵斥、贊許、大笑","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[:10]]},
    {"title":"②指雁身，表示上細長而下肥大","note":"","rows":[[r[0],r[1],r[2],r[3]] for r in rows[10:]]}]},
  {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
head["photos"]=["01."+("png" if os.path.exists(os.path.join(P,"可","01.png")) else "jpg")]; head["captions"]=["斧柯"]
json.dump(head,io.open(os.path.join(C,"可.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for r in rows:
    f=os.path.join(C,r[0]+".json")
    d={"char":r[0],"head":r[0],"pinyin":r[1],"level":3,"parent":"可","bus":[{"num":34,"name":"丂"}],
       "sections":[{"key":"shiyi","label":"释义","text":r[3],"cites":[]},
        {"key":"shengmu","label":"声母拟态","text":r[4],"cites":[]},
        {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
    json.dump(d,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("rows",len(rows))