# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
d=os.path.join(G,"虐"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
fs=[];n=0
for el in doc.paragraphs[348]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            n+=1; b=parts[rid[0]].blob; ext="png" if b[:4]==b"\x89PNG" else "jpg"
            fn="%02d.%s"%(n,ext); open(os.path.join(d,fn),"wb").write(b); fs.append("虐/"+fn)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi["chars"]["虐"]={"doc":"卷八 虎","files":fs}; json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
SS=[{"ch":"卷八虎","label":"卷八 虎"}]
rows=[["瘧（疟）","nüè","疒","《說文》：『熱寒休作。从疒从虐，虐亦聲。魚約切。』熱寒交作，即瘧疾，打擺子。《釋名》：『酷虐也。凡疾或寒或熱耳，而此疾先寒後熱，兩疾似酷虐者也。』yào，瘧疾的又稱。"],
["謔","xuè","言","《說文》：『戲也。从言虐聲。《詩》曰：善戲謔兮。虛約切。』開玩笑。挑逗。《玉篇》：『喜樂也。』"],
["㖸（噱）","jué","口","《集韻》：『噱，極虐切。《說文》：大笑也。或作㖸。通作𧮫、𠶸、䐘。』niā，方言。語氣詞。表示直陳或命令語氣。"],
["𪘽（𦞐齶）","è","齒","《字彙》：『齶，逆各切，音噩。齒斷也。齒內上下肉也。𪘽，同上。』口腔的上膛。"],
["𨩽（罅）","xià","缶","《漢典》：『同罅。裂縫。』"]]
SM={"瘧":"n「纳弄」取「纳」：寒熱收納而作（推）。","謔":"x「续消」取「续」：戲言相續不休（推）。","㖸":"j「聚决」取「聚」：大笑氣聚於口（推）。","𪘽":"è「零聲母」不系：零聲母，緒論七組未列（照實）。","𨩽":"x「续消」取「消」：裂縫漸開而消散（推）。"}
gs=[{"no":"①","title":"指遇虎，表示發抖皃","rows":[rows[0]]},
    {"no":"②","title":"指扮虎，表示戲謔、咧嘴皃","rows":rows[1:]}]
json.dump({"char":"虐","head":"虐（䖈䖋䨋𣑅𥤫𧆝𧆩𧆧𧆱𩁿𣑾）","pinyin":"nüè","level":2,"parent":"虍","grade":"二级字根","bus":{"num":48,"name":"虎"},"suoshujuan":"卷八 虎（第48部 虍）","links":SS,
 "sections":[{"key":"benyi","label":"本义","text":ps[349].replace("本義：","",1)+"\n"+ps[350]+"\n"+ps[351]},
 {"key":"shengmu","label":"声母拟态","text":"n「纳弄」取「纳」：虎爪反人，威虐納入於身（推）。"},
 {"key":"zizu","label":"字族衍义","groups":gs},
 {"key":"zixing","label":"字形","text":"取自《系统汉语》原稿卷八 虎（第48部 虍）。"},
 {"key":"suoshujuan","label":"所属卷","text":"","links":SS}]},io.open(os.path.join(C,"虐.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
for name,p,rad,st in rows:
    c=re.split(r"[（(]",name)[0]
    json.dump({"char":c,"head":name,"pinyin":p,"level":3,"parent":"虐","bus":{"num":48,"name":"虎"},"suoshujuan":"卷八 虎（第48部 虍）","links":SS,
     "sections":[{"key":"shiyi","label":"释义","text":st},{"key":"shengmu","label":"声母拟态","text":SM[c]},{"key":"suoshujuan","label":"所属卷","text":"卷八 虎（第48部 虍）","links":SS}]},io.open(os.path.join(C,c+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("glyphs",len(fs),"families",len(rows))