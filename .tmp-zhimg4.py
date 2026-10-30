import sys,os,json,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷一  雞.docx"); ps=d.paragraphs
idx=[k for k,p in enumerate(ps) if p.text.strip().startswith("▲赤麂")][0]
src=None
for k in (idx-1,idx-2,idx+1,idx+2):
    if 0<=k<len(ps):
        for bl in ps[k]._p.iter():
            for a in bl.attrib:
                if a.endswith('}embed'): src=bl.attrib[a]
        if src: break
def save(ch,rid):
    part=d.part.related_parts[rid]; blob=part.blob[:8]
    ext=".png" if blob.startswith(b"\x89PNG") else ".jpg"
    out=rf"D:\系统汉字\web\public\glyphs\photos\{ch}"; os.makedirs(out,exist_ok=True)
    for f in glob.glob(out+r"\*"): os.remove(f)
    fn="01"+ext
    open(os.path.join(out,fn),"wb").write(d.part.related_parts[rid].blob)
    return [fn]
names=save("旨",src); save("麂",src)
p=r"D:\系统汉字\web\public\glyphs\photos\index.json"
dd=json.load(open(p,encoding="utf-8")); ph=dd.get("photos") or dd
ph["旨"]=names; ph["麂"]=names
json.dump({"photos":ph},open(p,"w",encoding="utf-8"),ensure_ascii=False)
# 耆 二级字根卡
C=r"D:\系统汉字\web\public\cards"
q={"char":"耆","trad":"耆","simp":"","pinyin":"qí","level":2,"parent":"旨","bus":[{"num":3,"name":"旨"}],"sections":[
 {"key":"benyi","label":"本义","text":"耆，qí：从老旨聲，本为年老之称（《说文》「老也」）；旨取脂膏久积义，故年久者曰耆。","cites":[]},
 {"key":"zhuanyi","label":"转义","text":"引申为强横（耆定、耆功）、指师长（耆旧）。","cites":[]},
 {"key":"yinyuan","label":"音源","text":"旨聲，脂膏久积而厚，故音义与「旨」相承。","cites":[]},
 {"key":"shengmu","label":"声母拟态","text":"q「亲缺」取「亲」：积久相近（推）。","cites":[]},
 {"key":"zizu","label":"字族衍义","text":"耆系（二级字根），按义类分组：","groups":[
  {"title":"①耆之声：指脂膏所聚之长、老","note":"","rows":[
   ["鬐","qí","髟","马鬃；取长者义，故从髟"],
   ["鰭","qí","魚","鱼鳍；取耆（支柱）义，故从鱼"],
   ["蓍","shī","艸","蓍草，多年生；取耆老义"],
   ["嗜","shì","口","嗜好；取耆（欲）义"],
   ["愭","qí","心","恭顺；耆声记音"],
   ["榰","zhī","木","柱下石；取耆（支柱）义"],
   ["搘","zhī","手","支撑；取支柱义"],
   ["螧","qí","虫","虫名；记音"],
   ["䅲","qí","禾","禾名；耆省声"]]}]}]}
json.dump(q,open(rf"{C}\耆.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 耆系成员 parent 改耆
memb="鬐 鰭 蓍 嗜 愭 榰 搘 螧 䅲 鰭".split()
n=0
for ch in memb:
    f=rf"{C}\{ch}.json"
    if not os.path.exists(f): continue
    c=json.load(open(f,encoding="utf-8")); c["parent"]="耆"; c["level"]=3
    json.dump(c,open(f,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("photo->旨/麂",names,"| 耆卡 ok | reparent",n)