# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷八  虎.docx"); parts=doc.part.related_parts
d=os.path.join(G,"虢"); os.makedirs(d,exist_ok=True)
for f in os.listdir(d): os.remove(os.path.join(d,f))
fs=[];n=0
for el in doc.paragraphs[108]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
        if rid:
            b=parts[rid[0]].blob
            if len(b)>=1200:
                n+=1; fn="%02d.png"%n; open(os.path.join(d,fn),"wb").write(b); fs.append("虢/"+fn)
idx=json.load(io.open(os.path.join(G,"index.json"),encoding="utf-8"))
idx.setdefault("chars",{})["虢"]={"doc":"卷八 虎","files":fs}
json.dump(idx,io.open(os.path.join(G,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
BEN=("根據西周早期金文，本从手从𢮎。“𢮎”，象意虎的掌擊，《玉篇》：“批𢮎也。”老虎前肢的力量是貓科動物中最爲强大的。"
 "因此，在搏擊時，老虎的殺手鐧就是用前掌猛力批擊對方。据科學測定，其力度能達到一噸左右。从“手”，指如老虎一樣掌摑。"
 "實即“摑”的初文，guó，《廣韻》：“掌耳。”《集韻》：“批也。”")
ZY="由於掌心一般呈窩狀，故音義同“郭”。guō，《集韻》：“國名。《春秋傳》：‘攻郭則虞救之。’通作虢。”“郭，開也、虗也。”《廣韻》：“城郭也。《釋名》曰：‘郭，廓也，廓落在城外也’。”"
BZ=("由於“𢮎”所从“手”或作“攴”，遂與“手”演變成“寽”作“虢”。故《說文》：“虢，虎所攫畫明文也。从虎寽聲。古伯切。”所析不確。"
 "《段注》也認為：“寽在十五部。虢在五部。非聲也。”本當為“𢮎”聲，而“𢮎”本“虎”聲。")
rows1=[["虢","guó","虍","《廣韻》：“國名，周封虢仲於西虢，秦屬三川郡，義寧元年爲鳳林郡，武德初爲鼎州。又爲虢州。亦姓，《左傳》晉大夫虢射也。古伯切。”"]]
rows2=[["𢸗","guó","手","《漢典》：“揭開，刮掉。”"],
       ["㶁（湱）","guó","水","《說文》：“水裂去也。从水。虢聲。古伯切。”水受阻而分道流去。《揚子·方言》：“激水也。”huò，《集韻》：“湱，水聲。或从虢。”"],
       ["𧭣","guó","言","《集韻》：“郭獲切，音虢。𧭣𧭣，多言。”"]]
card={"id":"虢","char":"虢","head":"虢","pinyin":"guó","level":2,"parent":"虍","bus":{"num":48,"name":"虍"},
 "sections":[
  {"key":"benyi","label":"本義","text":BEN},
  {"key":"zhuanyi","label":"轉義","text":ZY},
  {"key":"bianzheng","label":"辯證","text":BZ},
  {"key":"shengmu","label":"聲母擬態","text":"g「隔估」取「隔」：虎掌橫隔而批擊（推）。"},
  {"key":"zizu","label":"字族衍義","groups":[
     {"no":"①","title":"指外廓","rows":rows1},
     {"no":"②","title":"指批擊","rows":rows2}]},
  {"key":"zixing","label":"字形","text":"取自《系統漢語》原稿卷八「虎」p108，共 %d 形。"%len(fs)},
  {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷八虎","label":"卷八 虎"}]}]}
json.dump(card,io.open(os.path.join(C,"虢.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("虢 ok",len(fs))