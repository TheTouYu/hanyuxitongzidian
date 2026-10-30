# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
bus=[{"num":35,"name":"厂"}]; JUAN={"ch":"卷五雁","label":"卷五 雁"}
head={"char":"炭","head":"炭（𡵼）","pinyin":"tàn","level":2,"parent":"厂","bus":bus,
 "aliases":["𡵼"],"gdir":"炭",
 "sections":[
  {"key":"benyi","label":"本义","text":"戰國古文从火从彥省。象意物質燃燒後形成的顏色如雁一般灰褐，指火炭。實即餘燼，故戰國古文或从“厂”从“少火”，或徑作“幺火”，指其火勢微弱。tàn，《廣韻》：“火炭。”《正字通》：“燒木未灰也。”《玉篇》：“灺也。”燭燼。"},
  {"key":"bianzheng","label":"辩证","text":"漢簡字形變化較大，或从火从岩，應是指可以燃燒的石頭，即煤炭。與小篆的从“屵”一脈相承。故《說文》：“燒木餘也。从火，岸省聲。他案切。”所釋當指石炭才是。可視為古文“炭”的轉義。"},
  {"key":"shengmu","label":"声母拟态","text":"t「涂突」取「涂」：火餘如塗抹之灰，色如雁褐（推）。"},
  {"key":"zizu","label":"字族衍义","groups":[
    {"no":"①","title":"指炭状，表示屈曲、灰暗","rows":[
      ["湠","tàn","水","《玉篇》：“大水也。”《廣韻》：“湠漫，水廣皃，出《字林》。”"],
      ["㨏","tān","手","《玉篇》：“撃也。”《集韻》：“槃㨏，宛轉也。”"],
      ["𣁗（𢾋𢾡）","tàn","文","《玉篇》：“𣁗𣁜，無采色也。”《廣韻》：“𢾋𣁜，無文章皃。”"],
      ["㛶","tàn","女","《集韻》：“㛶𡞲，無儀適皃。”儀容不加修飾。"]]},
    {"no":"②","title":"音译字","rows":[
      ["碳","tàn","石","一種非金屬元素。符號C，原子序數6。為無臭無味的固體。無定形碳有焦炭、木炭等，晶體碳有金剛石和石墨。拉丁文carbonium的音譯。不過，其中的“炭”仍具有一定的含義，因為物質燃燒後，剩下的主要是碳。"],
      ["羰","tàng","羊","《漢典》：“[羰基]碳氧兩種原子構成的原子團。”英文carbonyl(羰基)的音譯。"]]},
    {"no":"③","title":"形近字“岸”之訛","rows":[
      ["𩤧（䮗）","àn","馬","《正字通》：“䮗字之譌。”䮗，《說文》：“馬頭有髮赤色者。”《廣韻》：“𩢔䮗，馬行。又馬白頟至脣。”西周金文“厂”本可以加“干”為聲，故不能算是訛字。其狀也正如白頭雁。"]]}]},
  {"key":"suoshujuan","label":"所属卷","links":[JUAN]}]}
json.dump(head,io.open(os.path.join(C,"炭.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
fam=[("湠","tàn","《玉篇》：“大水也。”《廣韻》：“湠漫，水廣皃，出《字林》。”","t「涂突」取「涂」：水漫如灰塗（推）。"),
("㨏","tān","《玉篇》：“撃也。”《集韻》：“槃㨏，宛轉也。”","t「涂突」取「突」：擊而突下（推）。"),
("𣁗","tàn","《玉篇》：“𣁗𣁜，無采色也。”《廣韻》：“𢾋𣁜，無文章皃。”","t「涂突」取「涂」：色如灰塗（推）。"),
("㛶","tàn","《集韻》：“㛶𡞲，無儀適皃。”儀容不加修飾。","t「涂突」取「涂」：容不加飾如塗（推）。"),
("碳","tàn","一種非金屬元素。符號C，原子序數6。為無臭無味的固體。無定形碳有焦炭、木炭等，晶體碳有金剛石和石墨。拉丁文carbonium的音譯。不過，其中的“炭”仍具有一定的含義，因為物質燃燒後，剩下的主要是碳。","t「涂突」取「涂」：音譯，炭義仍存（推）。"),
("羰","tàng","《漢典》：“[羰基]碳氧兩種原子構成的原子團。”英文carbonyl(羰基)的音譯。","t「涂突」取「涂」：音譯，取炭音（推）。"),
("𩤧","àn","《正字通》：“䮗字之譌。”䮗，《說文》：“馬頭有髮赤色者。”《廣韻》：“𩢔䮗，馬行。又馬白頟至脣。”西周金文“厂”本可以加“干”為聲，故不能算是訛字。其狀也正如白頭雁。","零聲母不系（原字从厂，今读 àn 前无辅音）（推）。")]
for ch,py,shi,sm in fam:
    d={"char":ch,"head":ch,"pinyin":py,"level":3,"parent":"炭","bus":bus,
       "sections":[{"key":"shiyi","label":"释义","text":shi},{"key":"shengmu","label":"声母拟态","text":sm},{"key":"suoshujuan","label":"所属卷","links":[JUAN]}]}
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# glyph index
ip=os.path.join(G,"index.json"); ix=json.load(io.open(ip,encoding="utf-8")); ch=ix["chars"]
files=sorted(os.listdir(os.path.join(G,"炭")))
ch["炭"]={"doc":"卷五  雁.docx","variants":["𡵼"],"files":["炭/"+f for f in files]}
json.dump({"chars":ch},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
# photos
pi=os.path.join(G,"photos","index.json"); px=json.load(io.open(pi,encoding="utf-8")); pm=px.get("photos") or px
pm["炭"]=[sorted(os.listdir(os.path.join(G,"photos","炭")))[0]]
json.dump({"photos":pm},io.open(pi,"w",encoding="utf-8"),ensure_ascii=False)
pc=os.path.join(G,"photos","captions.json"); cx=json.load(io.open(pc,encoding="utf-8")); cmx=cx.get("captions") or cx
cmx["炭"]=["火炭"]
json.dump({"captions":cmx},io.open(pc,"w",encoding="utf-8"),ensure_ascii=False)
print("done")