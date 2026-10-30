# -*- coding: utf-8 -*-
import json,io,os,sys,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; P=r"D:\系统汉字\web\public\glyphs\photos"
doc=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=[p.text.strip() for p in doc.paragraphs]
def sect(k,l,t,links=None):
    s={"key":k,"label":l,"text":t,"cites":[]}
    if links: s["links"]=links
    return s
g1=[["嫡","dí","女","嫡dí《說文》：“孎也。从女啻聲。都曆切。”謹慎。《增韻》：“正室曰嫡，正室所生之子曰嫡子。一曰嫡，敵也，言無與敵也。”"],
["鏑","dí","金","鏑dí《說文》：“矢鏠也。从金啻聲。都曆切。”箭頭。甲骨文本从矢从帝。《釋名》：“鏑，敵也。可以禦敵也。”"],
["敵（敌）","dí","攴","敵（敌）dí《說文》：“仇也。从攴啻聲。徒曆切。”仇敵。《爾雅·釋詁》：“當也。”《玉篇》：“對也。”《廣韻》：“匹也。輩也。主也。”《廣雅》：“正也。”"],
["𪄱","dí","鳥","𪄱dí《說文》：“雉屬，戇鳥也。从鳥，適省聲。都曆切。”大約是指鶡，因其好鬥。"],
["樀（㭙）","dì、zhí、zhé","木","樀（㭙）dì《說文》：“戶樀也。从木啻聲。《爾雅》曰：‘簷謂之樀。’讀若滴。都曆切。”《篇海類編》：“機上卷絲器。”zhí，《集韻》：“磨床。”木磨盤。zhé，《集韻》：“㭙，《說文》：‘槌也。’或作樀。”"],
["蹢","zhí、dí","足","蹢zhí《說文》：“住足也。从足，適省聲。或曰蹢躅。賈侍中說：足垢也。直只切。”踟躕不前。dí，《廣雅》：“足也。”足蹄。"],
["䎮（𦔝）","tì","耒","䎮（𦔝）tì《廣韻》：“他計切，音替。不耕而種。”《集韻》：“種也。或从啻。”指所插的孔剛好夠放進種子。"],
["𪐏","zhé、zhí","黍","𪐏zhé《玉篇》：“黏飯也。”《廣韻》：“黏皃。”《廣雅》：“搏也，黏也。”zhí，《廣韻》：“黏黐。”"],
["甋","dì","瓦","甋dí《玉篇》：“瓴甋。”《爾雅·釋宮》：“瓴甋謂之甓。”長方磚。"],
["䵂","zhí","麥","䵂zhí《說文》：“麥核㞕也。十斤為三斗。从麥啻聲。直只切。”磨碎後與麩尚未篩分的麥屑。"],
["𥕐（𥐝𥖾）","dí","石","𥕐（𥐝𥖾）dí《廣雅》：“伐也。”《集韻》：“《博雅》：‘磓也。’或从適。从勺。一曰水𥕐番車。”墜落。碓。"],
["𡣪","shì","女","𡣪shì《廣韻》：“嫁也。施只切。”"],
["𣂉","dí","斗","𣂉dí《博雅》：“量也。”《集韻》：“量器。”"],
["適（适）","shì","辵","適（适）shì《說文》：“之也。从辵啻聲。適，宋魯語。施只切。”適、往。《篇海類編》：“至也。”《玉篇》：“女子出嫁。”《廣雅》：“善也。”《方言》：“牾也。”《廣韻》：“樂也。”"],
["𥧮","zhé","穴","𥧮zhé《廣雅》：“窟也。”《玉篇》：“兔窟也。”指洞窟狹窄，剛好能容身。"]]
g2=[["摘","zhāi、tì","手","摘zhāi《說文》：“拓果樹實也。从手啻聲。一曰指近之也。他曆切。又竹戇切。”採摘果實。《廣雅》：“取也。”《廣韻》：“發也。”揭發。tì，《廣韻》：“動也。”撥動、挑剔、擾亂。"],
["擿","zhì、tī、zhāi","手","擿zhì《說文》：“搔也。从手適聲。一曰投也。直只切。”《段注》：“以象骨搔首，因以為飾，即後人玉導、玉搔頭之類也。”即髮簪之類。同“揥”。tī，《集韻》：“挑也。”“磓也。”zhāi，《集韻》：“摘，取也。或从適。”"],
["𧬍（謫）","zhé、zé","言","𧬍（謫）zhé《說文》：“罰也。从言啻聲。陟革切。”罰罪。《玉篇》：“咎也、罪也、過也、怒也。”《廣雅》：“責也。”zé，《方言》：“怒也。”"]]
shang={"char":"啇","head":"啇（啻）","pinyin":"chì、dì、shì","level":2,"parent":"帝","bus":[{"num":11,"name":"帝"}],
 "sections":[sect("benyi","本义",ps[599]),sect("zhuanyi","转义",ps[600]+ps[601]+ps[602]),
  sect("bianzheng","辩证",ps[605]),sect("shengmu","声母拟态","d「囤动」取「囤」：啇為蒂印、木根，承果實而囤聚養分於本，故取囤（推）。"),
  {"key":"zizu","label":"字族衍义","text":"原文字族衍義兩組：","cites":[],
   "groups":[{"title":"①指蒂，表示相當、相對、相配","note":"","rows":g1},{"title":"②指取蒂，表示採摘、歸咎","note":"","rows":g2}]},
  {"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷二㠯","label":"卷二㠯"}]}]}
json.dump(shang,io.open(rf"{C}\啇.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
# reparent children
n=0
for ch,_,_,txt in [r for g in (g1,g2) for r in g]:
    base=re.sub(r"（.*?）","",ch)
    p=os.path.join(C,base+".json")
    if not os.path.exists(p): continue
    d=json.load(io.open(p,encoding="utf-8"))
    d["parent"]="啇"; d["level"]=3; d["bus"]=[{"num":11,"name":"帝"}]
    sm=next((s for s in d["sections"] if s["key"]=="shengmu"),None) or sect("shengmu","声母拟态","")
    juan={"key":"suoshujuan","label":"所属卷","text":"","cites":[],"links":[{"ch":"卷二㠯","label":"卷二㠯"}]}
    d["sections"]=[sect("shiyi","释义",txt),sm,juan]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
# 帝 加二级字根说明
dp=r"D:\系统汉字\web\public\cards\帝.json"; dz=json.load(io.open(dp,encoding="utf-8"))
if not any(s["key"]=="erji" for s in dz["sections"]):
    dz["sections"].insert(len(dz["sections"])-1,{"key":"erji","label":"本部二级字根","text":"啇（啻）：从口在帝中，象脫落的蒂，詳見「啇」卡。","cites":[]})
json.dump(dz,io.open(dp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("啇卡建立；改挂",n)