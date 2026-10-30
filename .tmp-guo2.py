# -*- coding: utf-8 -*-
import json,io,os,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
p=os.path.join(C,"虍.json"); d=json.load(io.open(p,encoding="utf-8"))
d["sections"]=[s for s in d["sections"] if s["key"]!="erji"]
json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
fam=[("𢸗","guó","手","《漢典》：“揭開，刮掉。”","g「隔估」取「隔」：以手隔物而揭刮（推）。"),
     ("㶁","guó","水","《說文》：“水裂去也。从水。虢聲。古伯切。”水受阻而分道流去。《揚子·方言》：“激水也。”huò，《集韻》：“湱，水聲。或从虢。”","g「隔估」取「隔」：水受隔而裂去（推）。"),
     ("𧭣","guó","言","《集韻》：“郭獲切，音虢。𧭣𧭣，多言。”","g「隔估」取「隔」：言語相隔而多（推）。")]
for z,py_,lei,luo,sm in fam:
    cd={"id":z,"char":z,"head":z+"（湱）" if z=="㶁" else z,"pinyin":py_,"level":3,"parent":"虢","bus":{"num":48,"name":"虍"},
        "sections":[{"key":"shiyi","label":"釋義","text":luo},
                    {"key":"shengmu","label":"聲母擬態","text":sm},
                    {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷八虎","label":"卷八 虎"}]}],"lei":lei}
    json.dump(cd,io.open(os.path.join(C,z+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("family 3")