# -*- coding: utf-8 -*-
import json,io,re,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷二  㠯.docx"); ps=[p.text.strip() for p in d.paragraphs]
rad={"狋":"犬","祁":"邑","眎":"見","呩":"口","禗":"示","沶":"水","𥥓":"穴","𧵋":"貝","𩚪":"食","𩿷":"鳥","祋":"殳","䒬":"艸","𣆇":"日","𥘖":"頁","𢼗":"攴","𤵫":"疒","𦊎":"网"}
def row(i):
    s=ps[i]; m=re.match(r"^(\S+?)(?:（[^）]*）)?([a-züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]+)",s)
    if not m: return None
    ch=m.group(1); py=m.group(2); body=s[m.end():].lstrip("，,：: ")
    return [ch,py,rad.get(ch,"示"),body]
g1=[r for i in range(430,441) if (r:=row(i))]
g2=[r for i in range(442,445) if (r:=row(i))]
g3=[r for i in range(446,449) if (r:=row(i))]
p=r"D:\系统汉字\web\public\cards\示.json"; c=json.load(io.open(p,encoding="utf-8"))
for s in c["sections"]:
    s["text"]=re.sub(r"^(本義|轉義|辯證|音源)[：:]","",s.get("text",""),count=1)
c["sections"].append({"key":"zizu","label":"字族衍义","text":"","groups":[
 {"title":"①指神靈，表示原因不明，暗地發生的","header":["字","读音","类属","取义落点"],"note":"","rows":g1},
 {"title":"②象意字，含有不明義","header":["字","读音","类属","取义落点"],"note":"","rows":g2},
 {"title":"③形近字“赤、余、不、木”之訛","header":["字","读音","类属","取义落点"],"note":"","rows":g3}]})
json.dump(c,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# photo: caption at 417, image paragraph before
cap=ps[417].lstrip("▲")
rids=[]
for i in (416,415):
    for bl in d.paragraphs[i]._p.iter():
        for a,v in bl.attrib.items():
            if a.endswith('}id') or a.endswith('}embed'):
                try:
                    pt=d.part.related_parts[v]
                    if hasattr(pt,"blob") and pt.content_type.startswith("image") and len(pt.blob)>15000:
                        rids.append((v,len(pt.blob)))
                except KeyError: pass
print("rows",len(g1),len(g2),len(g3),"img",rids[:2],"cap",cap[:30])
if rids:
    rid=rids[0][0]; blob=d.part.related_parts[rid].blob
    ext=".png" if blob[:4]==b"\x89PNG" else ".jpg"
    out=r"D:\系统汉字\web\public\glyphs\photos\示"; os.makedirs(out,exist_ok=True)
    for f in os.listdir(out): os.remove(os.path.join(out,f))
    fn="01"+ext; open(os.path.join(out,fn),"wb").write(blob)
    ip=r"D:\系统汉字\web\public\glyphs\photos\index.json"
    x=json.load(io.open(ip,encoding="utf-8")); ph=x.get("photos") or x
    ph["示"]=[fn]; json.dump({"photos":ph},io.open(ip,"w",encoding="utf-8"),ensure_ascii=False)
    cp=r"D:\系统汉字\web\public\glyphs\photos\captions.json"
    y=json.load(io.open(cp,encoding="utf-8")); yy=y.get("captions") or y
    yy["示"]=[cap]; json.dump({"captions":yy},io.open(cp,"w",encoding="utf-8"),ensure_ascii=False)
    print("photo ok",fn)