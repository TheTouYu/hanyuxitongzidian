# -*- coding: utf-8 -*-
import io,json,os,re,sys,glob
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
C=r"D:\系统汉字\web\public\cards"
Z=json.load(io.open(r"D:\系统汉字\web\public\zigen.json",encoding="utf-8"))
CN="零一二三四五六七八九十"
def cn(n):
    if n<=10: return CN[n]
    if n<20: return "十"+CN[n%10]
    if n<100: return CN[n//10]+"十"+(CN[n%10] if n%10 else "")
    return "一百"
files=glob.glob(r"D:\字谱智能体\*.docx")
idx={}
for f in files:
    m=re.search(r"卷([零一二三四五六七八九十百]+)",os.path.basename(f))
    if m: idx.setdefault(m.group(1),f)
miss=[]; ok=0; empty=0
H=re.compile(r"^\d{1,3}[.．]\s*\S{1,2}部$")
for j in Z["juan"]:
    key=cn(j["no"]); f=idx.get(key)
    nm="卷%s%s"%(key,j["name"])
    p=os.path.join(C,nm+".json"); d=json.load(io.open(p,encoding="utf-8"))
    secs=[s for s in d["sections"] if s.get("key")!="zizu"]
    text=""
    if f:
        ps=[x.text.strip() for x in Document(f).paragraphs]
        buf=[]
        for t in ps:
            if not t: continue
            if H.match(t): break
            buf.append(t)
        text="\n\n".join(buf[:40])
    if text:
        secs=[{"key":"juanshou","label":"卷首","text":text,"cites":[]}]+[s for s in secs if s.get("key")!="juanshou"]
        ok+=1
    else:
        secs=[{"key":"juanshou","label":"卷首","text":"原稿本卷无卷首导言，直接列部目。","cites":[]}]+[s for s in secs if s.get("key")!="juanshou"]
        empty+=1
    d["sections"]=secs+[s for s in d["sections"] if s.get("key")=="zizu"]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("docx",len(files),"mapped",len(idx),"卷首成文",ok,"无导言",empty,"缺docx",len([j for j in Z["juan"] if cn(j["no"]) not in idx]))