# -*- coding: utf-8 -*-
import json,io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
d=json.load(io.open(rf"{C}\厶.json",encoding="utf-8"))
d["level"]=1; d["parent"]=""
for s in d["sections"]:
    if s.get("key")=="benyi":
        s["text"]=("厶，niǎo／sī／mǒu：象雄性器之形，與「㠯」（以）同源，為其異體寫法（《正字通》引鄭樵：「厶非自營義；音鳥，男子之勢」）。"
                   "《說文》「奸衺也，自營為厶」以閉環立說，析形不確。"
                   "既與㠯同字，故亦列為一級字根，其諧聲字（私、𦮺）另見字族表。")
    if s.get("key")=="bianzheng":
        s["text"]="厶與㠯、以、氏、巳為一字之異寫，非別字；故厶不附於㠯之下，自為一級字根。"
json.dump(d,io.open(rf"{C}\厶.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
y=json.load(io.open(rf"{C}\㠯.json",encoding="utf-8"))
for s in y["sections"]:
    if s.get("key")=="zizu":
        for g in s["groups"]:
            if g.get("title","").startswith("本部二級字根"):
                g["rows"]=[r for r in g["rows"] if str(r[0])!="厶"]
                g["title"]="本部二級字根（各見其卡；厶為㠯之異體，已升作一級字根，另見其卡）"
json.dump(y,io.open(rf"{C}\㠯.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("done")