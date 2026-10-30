# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
d=os.path.join(G,"處"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
fs=[];n=0
for el in doc.paragraphs[360]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            n+=1; b=parts[rid[0]].blob; ext="png" if b[:4]==b"\x89PNG" else "jpg"
            fn="%02d.%s"%(n,ext); open(os.path.join(d,fn),"wb").write(b); fs.append("處/"+fn)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi["chars"]["處"]={"doc":"卷八 虎","files":fs}; json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
SS=[{"ch":"卷八虎","label":"卷八 虎"}]
rows=[["𧇤（處）","chǔ","虍","《字彙補》：『昌據切，同處。』"],
["𧇡","gū","虍","《五音集韻》：『𧇡息。』姑息。"],
["𩴘","jù","鬼","《字彙補》：『音據。』義不詳。疑同『魖』。"],
["𣫦","jì","糸","《說文》：『系或从毄處，作𣫦。』《玉篇》：『子孫相繋也。《說文》曰：與系同。』"],
["𥱿（筥）","jǔ","竹","《龍龕》：『養蠶竹器也。《玉篇》同筥。』《方言》：『箄、簍、籅、䈱，𥱿也……𥱿其通語也。』"],
["𩌲","xù","革","《漢典》：『馬耳的裝飾。』耳蓋。"],
["𡼆（嶇）","qū","山","《漢典》：『同嶇字。』"],
["𦍶（羐羑誘）","yǒu","羊","《康典》：『羐（羑），《玉篇》：導也。今作誘。亦作𦍶。』"],
["拠（㨿㩀據）","jù","手","《宋元以來俗字譜》：『據，《三國志平話》作拠。』『據』，《說文》：『杖持也。』『豦』本站立之意。跟『處』有別，應是訛混。"],
["𠽁（噱）","jué","口","《漢典》：『同噱。』大笑。"],
["𢟶（懅）","jù","心","《正字通》：『俗懅字。』懼怕。羞慚。"],
["𤩁（璩）","jù","玉","《正字通》：『俗璩字。』"],
["𦸵（𦼫）","jù","艸","《龍龕》：『同𦼫。』苦蕒菜。"],
["𤓤","xiǎn","火","《川篇》：『先踐切。』義不詳，疑即『燹』。"],
["𠝪（剜）","wān","刀","《字彙補》：『於歡切，音灣。刻削。』『剜』的訛字。"]]
SM={"𧇤":"ch「刺持」取「持」：止而持守其處（推）。","𧇡":"g「隔估」取「隔」：姑息止隔（推）。","𩴘":"j「聚决」取「聚」：鬼名，照實記音（推）。","𣫦":"j「聚决」取「聚」：子孫相聚相繋（推）。","𥱿":"j「聚决」取「聚」：竹器聚蠶（推）。","𩌲":"x「续消」取「续」：耳飾連綴而續（推）。","𡼆":"q「亲缺」取「缺」：山路崎嶇而缺（推）。","𦍶":"y「零聲母」不系：零聲母，緒論七組未列（照實）。","拠":"j「聚决」取「聚」：以手聚杖而持（推）。","𠽁":"j「聚决」取「聚」：大笑氣聚於口（推）。","𢟶":"j「聚决」取「聚」：懼怕羞慚，氣聚於心（推）。","𤩁":"j「聚决」取「聚」：玉佩聚串（推）。","𦸵":"j「聚决」取「聚」：苦蕒叢聚而生（推）。","𤓤":"x「续消」取「消」：火燹延燒而消（推）。","𠝪":"w「零聲母」不系：零聲母，緒論七組未列（照實）。"}
gs=[{"no":"①","title":"指處所，表示棲息、處置、依仗","rows":rows[0:9]},
    {"no":"②","title":"形近字「豦、宛」之訛","rows":rows[9:]}]
AL=["処","䖏","处"]
json.dump({"char":"處","head":"處（処䖏处）","pinyin":"chǔ","level":2,"parent":"虍","grade":"二级字根","aliases":AL,"bus":{"num":48,"name":"虎"},"suoshujuan":"卷八 虎（第48部 虍）","links":SS,
 "sections":[{"key":"benyi","label":"本义","text":ps[361].replace("本義：","",1)},
 {"key":"zhuanyi","label":"转义","text":"\n".join([ps[362].replace("轉義：","",1),ps[363],ps[364]])},
 {"key":"bianzheng","label":"辩证","text":ps[365].replace("辯證：","",1)+"\n"+ps[366]},
 {"key":"shengmu","label":"声母拟态","text":"ch「刺持」取「持」：駐足而持守其處（推）。"},
 {"key":"zizu","label":"字族衍义","groups":gs},
 {"key":"zixing","label":"字形","text":"取自《系统汉语》原稿卷八 虎（第48部 虍）。"},
 {"key":"suoshujuan","label":"所属卷","text":"","links":SS}]},io.open(os.path.join(C,"處.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for name,p,rad,st in rows:
    c=re.split(r"[（(]",name)[0]
    json.dump({"char":c,"head":name,"pinyin":p,"level":3,"parent":"處","bus":{"num":48,"name":"虎"},"suoshujuan":"卷八 虎（第48部 虍）","links":SS,
     "sections":[{"key":"shiyi","label":"释义","text":st},{"key":"shengmu","label":"声母拟态","text":SM[c]},{"key":"suoshujuan","label":"所属卷","text":"卷八 虎（第48部 虍）","links":SS}]},io.open(os.path.join(C,c+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
v=json.load(io.open(os.path.join(C,"variants.json"),encoding="utf-8")) if os.path.exists(os.path.join(C,"variants.json")) else {}
v["处"]="處"; v["処"]="處"; v["䖏"]="處"
json.dump(v,io.open(os.path.join(C,"variants.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("glyphs",len(fs),"families",len(rows))