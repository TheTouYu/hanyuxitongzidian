# -*- coding: utf-8 -*-
import json,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
MIME={"zh":"凿总","z":"凿总","ch":"刺持","c":"刺持","sh":"失收","s":"失收","h":"豁活","g":"隔估","k":"口控","j":"聚决","q":"亲缺","x":"续消","b":"闭剥","p":"拼辟","f":"附分","m":"蒙末","d":"囤动","t":"涂突","n":"纳弄","l":"拢离","r":"柔锐"}
def mk(ch,py_,lev,par,bus,sec):
    json.dump({"char":ch,"trad":ch,"simp":"","pinyin":py_,"level":lev,"parent":par,"bus":[{"num":bus[0],"name":bus[1]}],"sections":sec},open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
def fam(ch,py_,lei,gl,par,bus):
    ini="".join(c for c in py_ if c.isalpha())[:2]; key=ini if ini in MIME else ini[:1]
    s=[{"key":"shiyi","label":"释义","text":f"从{lei}桀聲：{gl}。","cites":[]},
       {"key":"shengmu","label":"声母拟态","text":(f"{key}「{MIME[key]}」取一面：{gl[:14]}（推）。" if key in MIME else "零聲母，不系。"),"cites":[]}]
    mk(ch,py_,3,par,bus,s)
G1=[("𧎩","jié","虫","《集韻》土𧎩，似蝗而小，善跳"),("榤","jié","木","《玉篇》「杙也」木樁，雞棲于杙"),("傑","jié","人","《說文》「傲也」，《廣韻》英傑特立"),("滐","jié","水","《集韻》水激回旋"),("嵥","jié","山","《集韻》嵥𡴎，高貌"),("𡩣","jié","宀","《集韻》「覆也」"),("𥠹","jié","禾","《說文》「禾舉出苗也」")]
G2=[("磔","zhé","石","《說文》「辜也」車裂、裂牲；祭風曰磔"),("搩","zhé","手","《集韻》張手度物；《廣韻》強暴"),("謋","huò","言","《正字通》破聲、疾速"),("𧤠","zhé","角","同「鞨」，治皮")]
G3=[("䮪","chéng","馬","犗馬；「騬」之訛"),("𦵴","jié","艸","草名；《正字通》以為譌字"),("㻧","duò","玉","玉名；《正字通》𤧮㻧並譌")]
mk("桀","jié",1,"",(7,"桀"),[
 {"key":"benyi","label":"本义","text":"桀，jié：从舛在木上（舛＝分张两足，木＝树）。象意有二——①立于树上，表示高出（分化作「傑」）；②陈尸于树上，表示分剖并挂起风干（《說文》「磔也……渠列切」，分化作「磔」）。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"由高出引申为特立、俊杰；由分剖引申为裂开、磔裂、张布；又借为夏桀之「桀」（凶暴）。","cites":[]},
 {"key":"yinyuan","label":"音源","text":"借音字；因有立高处义，义音同「匃」（《墨子·備梯》「直桀」孫詒讓引作「置楬」；《詩·衛風》「庶士有朅」《釋文》「朅，《韓詩》作桀」）。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"j「聚决」取「决」：分张而决裂（推）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"","groups":[
  {"title":"①指站在樹上，表示特立、高出","note":"","rows":[[c,p,l,t] for c,p,l,t in G1]},
  {"title":"②指分張于樹，表示裂開、分剖","note":"","rows":[[c,p,l,t] for c,p,l,t in G2]},
  {"title":"③形近字「乘、栗、朵」之訛","note":"","rows":[[c,p,l,t] for c,p,l,t in G3]}]}])
for g in (G1,G2,G3):
    for ch,py_,lei,gl in g: fam(ch,py_,lei,gl,"桀",(7,"桀"))
mk("𠓲","chéng",2,"桀",(7,"桀"),[
 {"key":"benyi","label":"本义","text":"𠓲（乘），chéng：甲骨文从大（人）在木上，象人登树／乘车之形。原稿注「167《乘部》」，独立为部。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"引申为乘坐、登、凭借、四马一车（千乘）。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"ch「刺持」取「持」：登木而持（推）。","cites":[]},
 {"key":"buzhu","label":"部属说明","text":"本部字根在 167 乘部独立立部，此处存目。","cites":[]}])
print("桀部+",len(G1+G2+G3))