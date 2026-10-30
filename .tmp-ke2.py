# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"; G=r"D:\系统汉字\web\public\glyphs"; P=os.path.join(G,"photos")
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); ps=[p.text.strip() for p in doc.paragraphs]; parts=doc.part.related_parts
PY=r"a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü"
groups=[("①指雁叫，表示歌唱、呵斥、贊許、大笑",(137,147)),("②指雁身，表示上細長而下肥大",(148,161)),
        ("③指雁的浮水",(162,165)),("④指雁的姿態，表示宛曲",(166,179)),("⑤指雁（鵝）羽，表示白色",(180,183))]
def parse(t):
    m=re.match(r"^(.+?)(["+PY+r"]{1,8})(?=《|$|[（(])",t)
    if not m: return None
    return [m.group(1).strip(), m.group(2), "", t[m.end():].strip()]
gs=[]
for title,(a,b) in groups:
    rows=[r for k in range(a,b+1) if ps[k] and (r:=parse(ps[k]))]
    gs.append({"title":title,"note":"","rows":rows})
    print(title[:8],len(rows))
benyi="".join(ps[k] for k in (129,130,131)).replace("本義：","",1)
zhuanyi="".join(ps[k] for k in (132,133)).replace("轉義：","",1)
secs=[
 {"key":"benyi","label":"本义","text":benyi,"cites":[]},
 {"key":"zhuanyi","label":"转义","text":zhuanyi,"cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"k「口控」取「口」：口在下，朝下者為歌唱、答應、啄食（推）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"","groups":gs,"cites":[]},
 {"key":"suoshujuan","label":"所属卷","text":"","links":[{"ch":"卷五雁","label":"卷五 雁"}],"cites":[]}]
d={"char":"可","head":"可（𠰕）","pinyin":"kě","level":2,"parent":"丂","bus":[{"num":34,"name":"丂"}],"aliases":["𠰕"],"sections":secs}
json.dump(d,io.open(os.path.join(C,"可.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# photo 斧柯 p135
for el in doc.paragraphs[135]._p.iter():
    if el.tag.split("}")[-1]=="blip":
        rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")][0]
        b=parts[rid].blob; dd=os.path.join(P,"可"); os.makedirs(dd,exist_ok=True)
        for f in os.listdir(dd): os.remove(os.path.join(dd,f))
        ext="png" if b[:4]==b"\x89PNG" else "jpg"
        open(os.path.join(dd,"01."+ext),"wb").write(b)
        idx=json.load(io.open(os.path.join(P,"index.json"),encoding="utf-8")); m=idx.get("photos") or idx
        m["可"]=["01."+ext]
        json.dump({"photos":m},io.open(os.path.join(P,"index.json"),"w",encoding="utf-8"),ensure_ascii=False)
        cap=json.load(io.open(os.path.join(P,"captions.json"),encoding="utf-8")); cm=cap.get("captions") or cap
        cm["可"]=["斧柯"]
        json.dump({"captions":cm},io.open(os.path.join(P,"captions.json"),"w",encoding="utf-8"),ensure_ascii=False)
        print("photo",ext,len(b)); break
print("glyphs",len(os.listdir(os.path.join(G,"可"))) if os.path.isdir(os.path.join(G,"可")) else 0)