# -*- coding: utf-8 -*-
import json,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
MIME={"zh":"凿总","z":"凿总","ch":"刺持","c":"刺持","sh":"失收","s":"失收","h":"豁活","g":"隔估","k":"口控","j":"聚决","q":"亲缺","x":"续消","b":"闭剥","p":"拼辟","f":"附分","m":"蒙末","d":"囤动","t":"涂突","n":"纳弄","l":"拢离","r":"柔锐"}
def mk(ch,py_,lev,par,bus,sec,trad=None,simp="",ali=None):
    d={"char":ch,"trad":trad or ch,"simp":simp,"pinyin":py_,"level":lev,"parent":par,"bus":[{"num":bus[0],"name":bus[1]}],"sections":sec}
    if ali: d["aliases"]=ali
    json.dump(d,open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
def fam(ch,py_,lei,gl,par,bus):
    ini="".join(c for c in py_ if c.isalpha())[:2]; key=ini if ini in MIME else ini[:1]
    s=[{"key":"shiyi","label":"释义","text":f"从{lei}㠯聲：{gl}。","cites":[]},
       {"key":"shengmu","label":"声母拟态","text":(f"{key}「{MIME[key]}」取一面：{gl[:14]}（推）。" if key in MIME else "零聲母，不系。"),"cites":[]}]
    mk(ch,py_,3,par,bus,s)
G1=[("佀","sì","人","《說文》「象也」相貌相似（同父所生）"),("娰","sì","女","同嫁一夫的年長女子（姒）")]
G2=[("苢","yǐ","艸","芣苡／薏苡，食之宜子"),("䬮","yí","食","飴，米糵煎成之穀芽糖"),("笖","yǐ","竹","生筍，竹胎"),("泤","sì","水","汜，水分出又流回主流之岔流")]
G3=[("㭒","sì","木","《說文》「臿也」鍬臿一類農具，俗作耜"),("鈻","sì","金","箭頭裝入箭杆的部分，取㭒之意")]
mk("㠯","yǐ",1,"",(8,"㠯"),[
 {"key":"benyi","label":"本义","text":"㠯（以），yǐ：象雄性生殖器形——圓頭部分象陰囊，細線部分象陰莖；指雄性、父系。本義分化為「厶、氏」。《玉篇》「厶，今爲私」；漢伶玄《飛燕外傳》「早有私病，不近婦人」，「私」指男性生殖器。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"繁殖後代所必需，故引申指「用」（《說文》「用也。从反巳……羊止切」）；引申依照、憑藉（物以類聚、以小見大）、因為（以此、以人廢言）、做、完結。","cites":[]},
 {"key":"bianzheng","label":"辩证","text":"對㠯的溯源眾說紛紜（薏苡、胎、耜、矣、始諸說），均不確，唯揭示「㠯、以、氏、氐」四字同源一事為確。","cites":[]},
 {"key":"yinyuan","label":"音源","text":"音源字。其音 yǐ 應源於性高潮時的叫聲；或作 sì，表穿刺、進入行為義。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"零聲母一系，緒論七組未列，不系（照實）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"","groups":[
  {"title":"①指共㠯，表示同父或同夫","note":"","rows":[[c,p,l,t] for c,p,l,t in G1]},
  {"title":"②指㠯之用，表示致孕、懷胎","note":"","rows":[[c,p,l,t] for c,p,l,t in G2]},
  {"title":"③指㠯之狀，表示可以插、刺之物","note":"","rows":[[c,p,l,t] for c,p,l,t in G3]}]}],simp="/",ali=["以"])
for g in (G1,G2,G3):
    for ch,py_,lei,gl in g: fam(ch,py_,lei,gl,"㠯",(8,"㠯"))
SUB=[("台","yí","从口㠯聲：口可指女陰或男陰之口，㠯聲象性交時狀態；引申怡悅、頤養（今高臺之台係「臺」之簡化，字源無關）"),
     ("厶","sī","與㠯同源，象男性生殖器形（《正字通》引鄭樵「音鳥，男子之勢」）；引申個人、自己的、奸邪"),
     ("矣","yǐ","从厶从矢，厶指男性生殖器、矢比況交媾（岩畫交媾旁繪弓箭），象意射精（本應歸冓部）"),
     ("氏","shì","㠯之變體，加一筆分化，指雄性、父系；後借為氏族之氏"),
     ("氐","dī","从氏下加一，與氏所指本同（雄性、根本）；引申根本、低平"),
     ("巳","sì","㠯之倒寫，象胎兒之形，與㠯同源；借為地支第六位"),
     ("了","liǎo","从子無臂，象嬰兒初生；借為結束、明白")]
for ch,py_,txt in SUB:
    mk(ch,py_,2,"㠯",(8,"㠯"),[
     {"key":"benyi","label":"本义","text":f"{ch}（{py_}，㠯部內二級字根）：{txt}。","cites":[]},
     {"key":"shengmu","label":"声母拟态","text":"見其本部（㠯）說；本字另詳其卡。","cites":[]},
     {"key":"buzhu","label":"说明","text":"本部內二級字根，字族詳見原稿本部各節；後續逐字補齊。","cites":[]}])
print("㠯部卡与8族字、7个二级存目")
