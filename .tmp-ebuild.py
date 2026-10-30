# -*- coding: utf-8 -*-
import json,io,os,re,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
G=r"D:\系统汉字\web\public\glyphs"; C=r"D:\系统汉字\web\public\cards"
doc=Document(r"D:\字谱智能体\卷五  雁.docx"); parts=doc.part.related_parts
ps=[p.text.strip() for p in doc.paragraphs]
PY=r"[a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü]+"
def split(t):
    m=re.match(r"^(\S{1,10}?)("+PY+r")",t)
    return (m.group(1),m.group(2),t[m.end():].lstrip()) if m else (t[:1],"",t[1:].lstrip())
r1=[split(ps[k]) for k in range(518,527) if ps[k]]
r2=[split(ps[k]) for k in range(530,540) if ps[k] and not ps[k].startswith("▲")]
SM="e「零聲母」不系：影母字今讀零聲母，緒論七組未列（照實）。"
head={"char":"戹","head":"戹（厄𠨳𠂬𢀴𢨩𠂘𠨬𢨤）","pinyin":"è","level":1,"bus":[{"num":38,"name":"厄"}],
 "aliases":["厄","𠨳","𠂬","𢀴","𢨩","𠂘","𠨬","𢨤"],
 "sections":[
  {"key":"benyi","label":"本义","text":ps[507].split("：",1)[1]},
  {"key":"zhuanyi","label":"转义","text":ps[508].split("：",1)[1]+"\n"+ps[509].split("：",1)[1] if "：" in ps[509] else ps[508].split("：",1)[1]+"\n"+ps[509]},
  {"key":"bianzheng","label":"辩证","text":ps[512].split("：",1)[1]+"\n"+ps[513]+"\n"+ps[514]},
  {"key":"yinyuan","label":"音源","text":ps[515].split("：",1)[1]},
  {"key":"shengmu","label":"声母拟态","text":SM},
  {"key":"zizu","label":"字族衍义","groups":[{"no":"①","title":"指軛頸，表示阻塞、卡住、握住","rows":[[a,b,"",c] for a,b,c in r1]},
    {"no":"②","title":"指軛狀，表示彎曲、婀娜","rows":[[a,b,"",c] for a,b,c in r2]}]},
  {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
json.dump(head,io.open(os.path.join(C,"戹.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
def fam(rows):
    for ch,py,rest in rows:
        name=ch.split("（")[0]
        d={"char":name,"head":ch,"pinyin":py,"level":3,"parent":"戹","bus":[{"num":38,"name":"厄"}],
           "sections":[{"key":"shiyi","label":"释义","text":rest},{"key":"shengmu","label":"声母拟态","text":SM},
             {"key":"suoshujuan","label":"所属卷","links":[{"ch":"卷五雁","label":"卷五 雁"}]}]}
        json.dump(d,io.open(os.path.join(C,name+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
fam(r1); fam(r2)
def blobs(k):
    o=[]; seen=set()
    for el in doc.paragraphs[k]._p.iter():
        if el.tag.split("}")[-1]=="blip":
            rid=[v for a,v in el.attrib.items() if a.endswith("}embed") or a.endswith("}id")]
            if rid and rid[0] not in seen: seen.add(rid[0]); o.append(parts[rid[0]].blob)
    return o
def dump(ch,bs):
    d=os.path.join(G,ch); os.makedirs(d,exist_ok=True)
    for f in os.listdir(d):
        if f.lower().endswith((".png",".jpg")): os.remove(os.path.join(d,f))
    o=[]
    for i,x in enumerate(bs):
        ext="png" if x[:4]==b"\x89PNG" else "jpg"; fn="%02d.%s"%(i+1,ext)
        open(os.path.join(d,fn),"wb").write(x); o.append(ch+"/"+fn)
    return o
gb=blobs(506); e=dump("戹",gb[:12]); k=dump("𠂬",gb[12:13]); w=dump("㧖",gb[13:14])
ixp=os.path.join(G,"index.json"); ix=json.load(io.open(ixp,encoding="utf-8")); chs=ix["chars"]
chs.setdefault("戹",{"doc":"","variants":"","files":[]})["files"]=e
chs.setdefault("𠂬",{"doc":"","variants":"","files":[]})["files"]=k
chs.setdefault("㧖",{"doc":"","variants":"","files":[]})["files"]=w
ph=ix.get("photos") or {}
for ch,k2,cap in (("戹",510,"負軛的銅車牛（南北朝）"),("軶",527,"青銅軛（商）")):
    bb=blobs(k2)
    if bb:
        d=os.path.join(G,"photos",ch); os.makedirs(d,exist_ok=True)
        for f in os.listdir(d): os.remove(os.path.join(d,f))
        ext="png" if bb[0][:4]==b"\x89PNG" else "jpg"; open(os.path.join(d,"01."+ext),"wb").write(bb[0])
        ph[ch]=[{"file":ch+"/01."+ext,"caption":cap}]
ix["photos"]=ph
json.dump(ix,io.open(ixp,"w",encoding="utf-8"),ensure_ascii=False)
print("rows",len(r1),len(r2),"glyphs",len(e),len(k),len(w))