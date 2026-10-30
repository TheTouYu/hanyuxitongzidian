# -*- coding: utf-8 -*-
import io,json,glob,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(C+r"\卷一雞.json",encoding="utf-8"))
d["sections"]=[
 {"key":"daoyu","label":"导语","text":"卷一論雞：雞為德禽，兼文武勇仁信五德；又為太陽之鳥，天雞鳴而扶桑日出。","cites":[]},
 {"key":"js_音源","label":"音源","text":"本卷音源字為「雞」：以「奚」為聲，借奚為雞；又以「只」指雞（只為雞距之形）。","cites":[]},
 {"key":"js_说物","label":"说物","text":"雞，知時畜也；頭戴冠者文也，足搏距者武也，敵在前敢鬥者勇也，見食相呼者仁也，守夜不失時者信也（《韓詩外傳》五德）。","cites":[]},
 {"key":"js_文化","label":"文化","text":"天雞扶桑：《玄中記》「東南有桃都山，上有大樹曰扶桑，上有天雞，日初出照此木，天雞即鳴，天下雞皆隨之鳴」。鳳凰與祭祀：鳳凰首戴德、項揭義、背負仁、心抱忠、翼挾信（《山海經》）；雞亦用於祭祀。","cites":[]}]
d["sections"].append([s for s in json.load(io.open(C+r"\卷一雞.json",encoding="utf-8"))["sections"] if s.get("key")=="js_音系"][0])
json.dump(d,io.open(C+r"\卷一雞.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
for f in glob.glob(C+r"\卷*.json"):
    x=json.load(io.open(f,encoding="utf-8")); ch=False
    for s in x["sections"]:
        for g in (s.get("groups") or []):
            if "部目" in (g.get("title") or ""):
                g["title"]=""; ch=True
                for r in g.get("rows",[]):
                    t=str(r[2]) if len(r)>2 else ""
                    t=re.sub(r"^【[^】]*】","",t).strip()
                    if t and t!="—":
                        t=re.split(r"[。；，]",t)[0][:18]
                        if t!=r[2]: r[2]=t
    if ch: json.dump(x,io.open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")