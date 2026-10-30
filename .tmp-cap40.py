# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"; H=["字","读音","类属","取义落点"]
def card(ch,py_,head,ali,benyi,bianzheng,yinyuan,sm,groups):
    secs=[{"key":"benyi","label":"本义","text":benyi,"cites":[]}]
    if bianzheng: secs.append({"key":"bianzheng","label":"辩证","text":bianzheng,"cites":[]})
    if yinyuan: secs.append({"key":"yinyuan","label":"音源","text":yinyuan,"cites":[]})
    secs.append({"key":"shengmu","label":"声母拟态","text":sm,"cites":[]})
    secs.append({"key":"zizu","label":"字族衍义","text":"字族衍义：","groups":[{"title":t,"note":"","rows":rows} for t,rows in groups]})
    d={"char":ch,"trad":ch,"simp":"","pinyin":py_,"level":2,"parent":"示","bus":[{"num":10,"name":"示"}],
       "head":head,"aliases":ali,"sections":secs}
    json.dump(d,io.open(rf"{C}\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
card("柰","nài","柰（奈）",["奈"],
 "柰，nài：从木从示，本义为堆柴于「示」（神主）前燎祭（原稿：「奈本義為堆柴於示前燎祭」）。转义：由堆柴引申为柰树与「忍得住」（奈何）。",
 "《廣雅》以石榴釋柰，非其本義。","音源：「示」为音源字，义音同「氏」。","n「纳弄」取「纳」：柴纳于示前而燎（推）。",
 [("①堆柴爎祭，表短而密集",[["𣛒","nài","木","柴堆短密；柰声"],
  ["隶","lì","隶","及、逮；柰省声记音"],
  ["捺","nà","手","按下；柰声，取短密下压义（推）"],
  ["渿","nài","水","水名；柰声记音"],
  ["㮏","nài","木","木名；柰声"]])])
card("祟","suì","祟",[],
 "祟，suì：字源本即「柰」，指柴祭（原稿：「祟的字源本即『柰』，指柴祭」）。转义：由柴祭引申为神祸、暗中作怪。",
 "","「祟」是音源字，义音同「叕」。","s「失收」取「收」：暗祟而收（推）。",
 [("①塞、幽暗，表暗中作祟",[["𠭥","suì","又","塞也；祟声"],
  ["㝮","cuì","宀","塞也；祟声"],
  ["竄","cuàn","穴","逃窜、藏匿；祟声，取幽塞义（推）"],
  ["贅","zhuì","貝","赘疣；祟声记音"],
  ["蠆","chài","虫","蝎类毒虫；祟声记音"]])])
card("款","kuǎn","款",[],
 "款，kuǎn：从欠柰聲（原稿：「款从柰，本指暗里显露」）。转义：标识、条款、诚恳、缓慢。",
 "","款从「柰」得声，取柰之「短密、暗中」义。","k「口控」取「控」：暗里显露而控（推）。",
 [("①暗中进行，表幽隐",[["䲌","kuǎn","魚","魚名；款声记音"],
  ["窾","kuǎn","穴","空也；款声，取空中暗义（推）"],
  ["䥗","kuǎn","金","金名；款声记音"],
  ["㯘","kuǎn","木","木名；款声记音"],
  ["䕀","kuǎn","艸","艸名；款声记音"]])])
card("祡","chái","祡（柴）",["柴"],
 "祡，chái：从示此聲，本义为烧柴燎祭天神（原稿：「祡本義為燒柴燎祭天神」）。",
 "","音源：借「此」聲。","ch「刺持」取「持」：柴持而燎（推）。",
 [("①柴薪短小，表参差聚集与篱落",[["柴","chái","木","短小薪柴；祡声，取柴薪义"],
  ["偨","cī","人","偨池，参差不齐；柴声"],
  ["㾹","chái","疒","病也；柴声记音"],
  ["䓱","chái","艸","艸名；柴声记音"],
  ["𡍥","zhài","土","篱落；柴声，取柴篱义（推）"]])])
card("市","shì","市",[],
 "市，shì：从丂从巾（原稿：「市的本義是趕赴祭祀場所的廟會」），本义为赶赴祭祀场所的庙会。",
 "市的「示」旁后讹作「丂」「巾」。","","sh「失收」取「收」：聚市而收（推）。",
 [("①市貌热闹，表聚集交易",[["柿","shì","木","果木；市声，取市集果品义（推）"],
  ["遞","dì","辵","传递；市声记音"],
  ["秭","zǐ","禾","禾束；市声记音"],
  ["鬧","nào","鬥","喧闹；市声，取市集喧闹义"]])])
p=rf"{C}\奈.json"
if os.path.exists(p):
    d=json.load(io.open(p,encoding="utf-8")); d["hidden"]=True; d["aliases"]=["柰"]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("ok")