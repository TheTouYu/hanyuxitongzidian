# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
RAD={"醵":"酉","噱":"口","㘌":"口","𥴧":"竹","壉":"土","澽":"水","䆽":"穴","臄":"肉","據":"手","鐻":"金","籧":"竹","璩":"玉","𦼫":"艸","𪍸":"麥","躆":"足","𨎶":"車","𨞙":"邑","㯫":"木","䟊":"足","𤢓":"犬","𧲋":"豕","𧴘":"豸","𧝲":"衣","𨼫":"阜","𩁋":"鳥","𨼽":"阜","蘧":"艸","遽":"辵","劇":"刀","勮":"力","懅":"心","𧇿":"且","㷾":"火","𥜅":"示"}
rows={}; cur=None
for k in range(308,348):
    t=ps[k]
    if not t: continue
    if t.startswith("▲") or t.startswith("字族衍義"): continue
    m=re.match(r"^([①②③④])(.+)$",t)
    if m: cur=m.group(2); rows[cur]=[]; continue
    m=re.match(r"^(\S+?)\s*([a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+(?:、[a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+)?)\s*(.*)$",t)
    if m and cur: rows[cur].append((m.group(1),m.group(2),m.group(3)))
gs=[]
for no,(t,rs) in zip("①②③④",rows.items()):
    gs.append({"no":no,"title":t,"rows":[[a,b,RAD.get(re.split(r"[（(]",a)[0],""),c] for a,b,c in rs]})
SS=[{"ch":"卷八虎","label":"卷八 虎"}]
SM={"醵":"j「聚决」取「聚」：湊錢聚合而飲（推）。","噱":"j「聚决」取「聚」：大笑張口，氣聚於喉（推）。","㘌":"j「聚决」取「聚」：笑不止，氣聚不散（推）。","𥴧":"j「聚决」取「聚」：圓筐聚物（推）。","壉":"j「聚决」取「聚」：地名，照實記音（推）。","澽":"j「聚决」取「聚」：曝晒而乾硬開裂（推）。","䆽":"q「亲缺」取「缺」：穴空而缺（推）。","臄":"j「聚决」取「聚」：口內上齶聚肉（推）。","據":"j「聚决」取「聚」：以爪聚按而持之（推）。","鐻":"j「聚决」取「聚」：鐘鼓之柎，聚獸形（推）。","籧":"q「亲缺」取「缺」：粗席疏缺（推）。","璩":"q「亲缺」取「缺」：耳環穿孔而缺（推）。","𦼫":"q「亲缺」取「缺」：苦蕒葉缺（推）。","𪍸":"q「亲缺」取「缺」：小麥粒小如缺（推）。","躆":"j「聚决」取「聚」：以足據地聚力（推）。","𨎶":"q「亲缺」取「缺」：車輞外周環缺（推）。","𨞙":"q「亲缺」取「缺」：聚落，照實記音（推）。","㯫":"q「亲缺」取「缺」：籬落間隔成缺（推）。","䟊":"q「亲缺」取「缺」：小跳疾走（推）。","𤢓":"j「聚决」取「聚」：獸迅頭，聚而奮（推）。","𧲋":"j「聚决」取「聚」：豕名，照實記音（推）。","𧴘":"h「豁活」取「豁」：貉似狐，善睡而性活（推）。","𧝲":"j「聚决」取「聚」：衣名，照實記音（推）。","𨼫":"q「亲缺」取「缺」：臺階層層有缺（推）。","𩁋":"q「亲缺」取「缺」：鶺鴒尾長而缺（推）。","𨼽":"q「亲缺」取「缺」：將帥，照實記音（推）。","蘧":"q「亲缺」取「缺」：瞿麥莖節膨大而缺（推）。","遽":"j「聚决」取「决」：驛傳急疾，決然而速（推）。","劇":"j「聚决」取「决」：尤甚猛烈（推）。","勮":"j「聚决」取「决」：盡力而决（推）。","懅":"j「聚决」取「聚」：心急氣聚（推）。","𧇿":"z「凿总」取「总」：姑且匆匆而往（推）。","㷾":"j「聚决」取「聚」：火聚而熾（推）。","𥜅":"l「拢离」取「拢」：福祿攏聚（推）。"}
def card(ch,head,pinyin,level,parent,sections,aliases=None,grade=None,rootLevel=None):
    dd={"char":ch,"head":head,"pinyin":pinyin,"level":level,"parent":parent,"bus":{"num":48,"name":"虎"},"suoshujuan":"卷八 虎（第48部 虍）","links":SS,"sections":sections}
    if aliases: dd["aliases"]=aliases
    if grade: dd["grade"]=grade
    if rootLevel: dd["rootLevel"]=rootLevel
    json.dump(dd,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
card("豦","豦","jù",2,"虍",[
 {"key":"benyi","label":"本义","text":ps[303].replace("本義：","",1)},
 {"key":"zhuanyi","label":"转义","text":ps[304].replace("轉義：","",1)},
 {"key":"bianzheng","label":"辩证","text":ps[305].replace("辯證：","",1)+"\n"+ps[306]},
 {"key":"shengmu","label":"声母拟态","text":"j「聚决」取「聚」：猛獸聚爪按拏而立（推）。"},
 {"key":"zizu","label":"字族衍义","groups":gs},
 {"key":"zixing","label":"字形","text":"取自《系统汉语》原稿卷八 虎（第48部 虍）。"},
 {"key":"suoshujuan","label":"所属卷","text":"","links":SS}])
m=0
for g in gs:
    for name,p,ls,st in g["rows"]:
        base=re.split(r"[（(]",name)[0]
        card(base,name,p,3,"豦",[
         {"key":"shiyi","label":"释义","text":st},
         {"key":"shengmu","label":"声母拟态","text":SM.get(base,"（按今读音取拟态义一面，推。）")},
         {"key":"suoshujuan","label":"所属卷","text":"卷八 虎（第48部 虍）","links":SS}])
        m+=1
# ▲瞿麥 → 蘧
dd=os.path.join(P,"蘧"); os.makedirs(dd,exist_ok=True)
for f in os.listdir(dd): os.remove(os.path.join(dd,f))
for el in doc.paragraphs[337]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob; ext="png" if b[:4]==b"\x89PNG" else "jpg"
            open(os.path.join(dd,"01."+ext),"wb").write(b); break
cap="瞿麥"
for name,key in (("index.json","photos"),("captions.json","captions")):
    p=os.path.join(P,name); x=json.load(io.open(p,encoding="utf-8")); mm=x.get(key) or x
    mm["蘧"]=["01.jpg"] if key=="photos" else [cap]
    json.dump({key:mm},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
gi=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
gi.setdefault("photos",{})["蘧"]=[{"file":"photos/蘧/01.jpg","caption":cap}]
json.dump(gi,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
print("groups",[(g["title"],len(g["rows"])) for g in gs],"cards",m)