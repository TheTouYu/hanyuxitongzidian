# -*- coding: utf-8 -*-
import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
MIME={"zh":"凿总","z":"凿总","ch":"刺持","c":"刺持","sh":"失收","s":"失收","h":"豁活","g":"隔估","k":"口控","j":"聚决","q":"亲缺","x":"续消","b":"闭剥","p":"拼辟","f":"附分","m":"蒙末","d":"囤动","t":"涂突","n":"纳弄","l":"拢离","r":"柔锐"}
def mk(ch,py_,lev,par,bus,sec):
    json.dump({"char":ch,"trad":ch,"simp":"","pinyin":py_,"level":lev,"parent":par,"bus":[{"num":bus[0],"name":bus[1]}],"sections":sec},open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
def fam(ch,py_,lei,gl,par,bus):
    ini="".join(c for c in py_ if c.isalpha())[:2]; key=ini if ini in MIME else ini[:1]
    s=[{"key":"shiyi","label":"释义","text":f"从{lei}{par}聲：{gl}。","cites":[]},
       {"key":"shengmu","label":"声母拟态","text":(f"{key}「{MIME[key]}」取一面：{gl[:14]}（推）。" if key in MIME else "零聲母，不系。"),"cites":[]}]
    mk(ch,py_,3,par,bus,s)
G1=[("極","jí","木","《說文》「棟也」屋之中棟；引申至極、窮盡"),("𤺷","jí","疒","《字彙補》「病也」"),("殛","jí","歺","《說文》「殊也」誅殺、流放"),("𡹪","jí","山","《集韻》山名"),("𢉗","jí","广","同「極」，指棟樑"),("𥈂","jí","目","《集韻》「張目也」"),("𦎢","jì","羊","羊行峭壁"),("𧛘","jí","衣","同「襋」，衣領")]
G2=[("㥛","jí","心","《說文》「疾也」心急"),("䩯","jí","革","《說文》「急也」皮堅急"),("𤷉","jí","疒","《字彙》「疾也，气急也」"),("𧩦","jí","言","《集韻》「訥言也」急不能言")]
G3=[("𠔠","yuè","食","《字彙補》「湯中汋」汆燙")]
G4=[("𢔔","hán","彳","《字彙》「水入船也」，形近「函」之訛")]
mk("亟","jí",2,"乞",(6,"乞"),[
 {"key":"benyi","label":"本义","text":"亟，jí：甲骨文从人处上下之间形，象意有三——人上窜下跳（急切、敏捷、频繁）；顶天立地（极端、边远，「極」之初文）；敬上怜下（相爱，《方言》「亟、憐、憮、㤿，愛也」）。","cites":[]},
 {"key":"bianzheng","label":"辩证","text":"西周后繁化：加口、加攴或省为卜、又，《說文》「敏疾也。从人从口，从又从二」析形已非初形。","cites":[]},
 {"key":"yinyuan","label":"音源","text":"本「乞」聲，因有急義，音義同「戒」（《爾雅·釋言》「悈，急也」，《釋文》「悈，又作亟」）。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"j「聚决」取「决」：急迫而决（推）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"","groups":[
  {"title":"①指頂天立地，表示頂端、偏遠","note":"","rows":[[c,p,l,t] for c,p,l,t in G1]},
  {"title":"②指上竄下跳，表示急切、迅速","note":"","rows":[[c,p,l,t] for c,p,l,t in G2]},
  {"title":"③象意字，含急義","note":"","rows":[[c,p,l,t] for c,p,l,t in G3]},
  {"title":"④形近字「函」之訛","note":"","rows":[[c,p,l,t] for c,p,l,t in G4]}]}])
for g in (G1,G2,G3,G4):
    for ch,py_,lei,gl in g: fam(ch,py_,lei,gl,"亟",(6,"乞"))
mk("亙","gèn",2,"乞",(6,"乞"),[
 {"key":"benyi","label":"本义","text":"亙，gèn：甲骨文从二（上下）中有一点，与「亟」同源，表上下之间横贯不断；後立为第504部「亙部」字根（原稿第412段「亙（𠄭𠄨𠄣）：504《亙部》」）。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"引申为延续不断、横贯（亘古、绵亘）。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"g「隔估」取「隔」：上下相隔而贯（推）。","cites":[]},
 {"key":"buzhu","label":"部属说明","text":"本部字根在 504 亙部独立立部，此处仅作乞部二级字根存目。","cites":[]}])
W=[("旣","jì","皀","《說文》「小食也」食畢"),("暨","jì","日","《說文》「日頗見也」及、與"),("炁","qì","火","同「氣」，云气"),("概","gài","木","《說文》「杚斗斛」平斗斛之木"),("溉","gài","水","《說文》「一曰灌注也」灌溉"),("摡","gài","手","《說文》「滌也」拭滌"),("慨","kǎi","心","慷慨、慨嘆"),("嘅","kǎi","口","《說文》「嘆也」"),("䀈","qì","目","視也"),("黖","xì","黑","黑貌"),("蔇","jì","艸","《說文》「艸多皃」"),("穊","jì","禾","《說文》「稠也」稠密")]
mk("旡","jì",2,"乞",(6,"乞"),[
 {"key":"benyi","label":"本义","text":"旡，jì：象人饮食毕而口气上逆之形（打嗝），「既」之初文；《說文》「飲食气屰不得息曰旡」。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"引申为已经、完毕（分化作「既」）。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"j「聚决」取「聚」：氣聚而上逆（推）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"","groups":[{"title":"①食畢氣逆、已然而貫","note":"","rows":[[c,p,l,t] for c,p,l,t in W]}]}])
for ch,py_,lei,gl in W: fam(ch,py_,lei,gl,"旡",(6,"乞"))
print("亟族",len(G1+G2+G3+G4),"旡族",len(W))