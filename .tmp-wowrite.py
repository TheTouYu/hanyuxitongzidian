# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"
D=json.load(io.open(r"D:\系统汉字\.tmp-wo.json",encoding="utf-8"))
SM="w「零聲母」不系：疑母字今讀零聲母，緒論七組未列（照實）。"
head={
 "char":"我","head":"我（𠨂𢦐𢦖𢦠𨈟𩇶𢦓）","pinyin":"wǒ","level":1,"bus":[{"num":36,"name":"我"}],
 "aliases":["𠨂","𢦐","𢦖","𢦠","𨈟","𩇶","𢦓"],
 "sections":[
  {"key":"benyi","label":"本义","text":"象戈類兵器形。這種兵器與一般的戈不同，有突出的三角刺，一般為三個，呈鋸齒狀排列，大約是砍斫類武器；或者是作為儀仗用的。wǒ，《說文》：“古殺字。”"},
  {"key":"zhuanyi","label":"转义","text":"由我之狀，引申指傾側。《說文》：“頃頓也。”《段注》：“謂順側也。頃，頭不正也。頓，下首也。故引申爲頃側之意。”傾側如點頭示意，故又引申指第一人稱代詞。《廣韻》：“己稱。”"},
  {"key":"bianzheng","label":"辩证","text":"由于小篆“我”的表刃部分演變成了“𠄒”，故《說文》：“施身自謂也。或說我，頃頓也。从戈从𠄒。𠄒，或說古垂字。一曰古殺字。凡我之屬皆从我。，古文我。五可切。（注）徐鍇曰：从戈者，取戈自持也。”析形不確。\n由于“我”作為武器或儀仗，很早就退出了歷史舞台，本義不再使用。加上其借音于鵝，故為“鵝”的音義所替代。《說文》：“䳘，鴖鵝也。从鳥我聲。五何切。”“鵝”又反過來以“我”為聲。說明它們之間的音義互通關係。鵝的優美身姿，以及遷徙的習性，可能一度被作為崇拜的圖騰。如楚國的巫師峨冠博帶，其狀便正如鵝一般。因此，“我”的被作為第一人稱，很可能是源于巫師的自稱。"},
  {"key":"yinyuan","label":"音源","text":"借音字。因我狀如鵝而借音于鵝。“鵝”即从“我”聲。"},
  {"key":"shengmu","label":"声母拟态","text":SM},
  {"key":"zizu","label":"字族衍义","groups":D["rows"]},
  {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷五雁","label":"卷五 雁"}]}
 ]}
json.dump(head,io.open(os.path.join(C,"我.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
n=0
for ch,py,cat,txt in D["cards"]:
    c={"char":ch,"head":ch,"pinyin":py,"level":3,"parent":"我","bus":[{"num":36,"name":"我"}],
       "sections":[
        {"key":"shiyi","label":"释义","text":txt},
        {"key":"shengmu","label":"声母拟态","text":SM},
        {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
    json.dump(c,io.open(os.path.join(C,ch+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("cards",n)
# glyph index
ip=os.path.join(G,"index.json"); ix=json.load(io.open(ip,encoding="utf-8")); chs=ix["chars"]
chs["我"]["files"]=D["wo"]; chs["娥"]["files"]=D["e"]
json.dump({"chars":chs},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
# photos
P=os.path.join(G,"photos")
for name,val in (("index.json",{"photos":{"我":["01.jpg"]}}),("captions.json",{"captions":{"我":["西周我"]}})):
    p=os.path.join(P,name); d=json.load(io.open(p,encoding="utf-8")); m=d.get(list(d.keys())[0]) or {}
    for k,v in val[list(val.keys())[0]].items(): m[k]=v
    json.dump({list(val.keys())[0]:m},io.open(p,"w",encoding="utf-8"),ensure_ascii=False)
print("ok")