# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
rows=json.load(io.open(r"D:\系统汉字\.tmp-changrows.json",encoding="utf-8"))
def sec(k,l,t,**kw):
    d={"key":k,"label":l,"text":t}; d.update(kw); return d
head={
 "char":"厂","head":"厂（厈）","pinyin":"hǎn","level":1,"bus":["35"],
 "sections":[
  sec("benyi","本义",rows["213"].split("本義：",1)[1] if "本義：" in rows.get("213","") else
      "甲骨文本與“石”同源，象懸崖形。上面突出呈棚狀。西周金文添加聲符“干”，義即下面象干一樣陡直，上面則橫而斜出。hǎn，《說文》：“山石之厓巗，人可居，象形。凡厂之屬皆从厂。，籀文从干。呼旱切。”"),
  sec("zhuanyi","转义","由懸崖的上部突出之狀，引申指翻轉、覆蓋。此義分化如“反（fǎn）”，《說文》：“覆也。”"),
  sec("bianzheng","辩证","由于“厂”本指石，多被作為形旁使用，表示石類事物。直接作為聲旁使用，幾乎是沒有，多另加“干、圭”等作為聲符。\n\n因為大雁是水鳥，多棲息于草澤。跟指懸崖的“厂”沒有什麼關聯。"),
  sec("yinyuan","音源","指“石”，則為借音字。義音同“干”。指雁陣，則為音源字，源自大雁叫聲。"),
  sec("shengmu","声母拟态","h「豁活」取「豁」：懸崖上突下陡，遮覆如棚，其下豁然可居（推）。"),
  sec("zizu","字族衍义","",groups=[
    {"t":"①指“石”，表示懸崖或懸崖狀","rows":[
      ["厓","yá","厂","山邊；圭為疊加聲符，狀如圭"],
      ["崖","yá","山","高邊；山高如圭，上部邊沿突出"],
      ["涯","yá","水","水邊懸崖；上伸下凹，引申邊際"],
      ["睚","yá","目","上部眼眶；怒視"],
      ["屵","è","山","岸高；仰也"],
      ["娾","ǎi","女","額頭前突如崖之狀"],
      ["厊","yǎ","厂","上牙齙出"],
      ["广","yǎn","广","因崖為屋，一邊下"],
      ["𠆲","yǎn","","高峻皃"],
      ["𢇘","yǎn","广","卑皃；齊"],
      ["㚧","yǎn","女","婦人齊整皃"],
      ["𢇞","hàn","","吮吸乳汁之狀"]]},
    {"t":"②同“丂”，表示大雁","rows":[
      ["㷳","yàn","火","火色如褐雁"],
      ["贗","yàn","貝","偽物；鵝似雁而味不如"],
      ["鴈","yàn","鳥","大雁；厂或為丂（人字陣）之誤"]]}]),
 ],
}
# fix benyi from paragraph 213 raw (rows has 213)
head["sections"][0]["text"]=rows["213"].replace("本義：","",1)
json.dump(head,io.open(os.path.join(C,"厂.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# family cards
ZERO="y「零聲母」不系：零聲母，緒論七組未列（照實）。"
fam=[("228","厓"),("229","崖"),("230","涯"),("231","睚"),("232","屵"),("233","娾"),("234","厊"),("235","广"),("236","𠆲"),("237","𢇘"),("238","㚧"),("239","𢇞"),("241","㷳"),("242","贗"),("243","鴈（雁）")]
n=0
for k,ch in fam:
    txt=rows[k]
    d={"char":ch,"head":ch,"pinyin":"","level":3,"parent":"厂","bus":["35"],
       "sections":[sec("shiyi","释义",txt),sec("shengmu","声母拟态",ZERO)]}
    json.dump(d,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("head+",n)