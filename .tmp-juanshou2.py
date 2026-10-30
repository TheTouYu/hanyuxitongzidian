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
H=re.compile(r"^(\d{1,3})[.．]\s*(\S{1,2})部$")
paras={}
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[x.text.strip() for x in Document(f).paragraphs]
    except Exception: continue
    paras[f]=ps
assigned={}; used=set()
for j in Z["juan"]:
    for f,ps in paras.items():
        if f in used: continue
        first=None; hi=None
        for i,t in enumerate(ps):
            m=H.match(t)
            if m: first=int(m.group(1)); hi=m.group(2); break
        if first is None: continue
        if j["from"]<=first<=j["to"] and (hi==j["name"] or True):
            # 校验：该文件首个部号应等于本卷首部（或本卷在文件内）
            if first==j["from"] or j["from"]<=first<=j["to"]:
                assigned.setdefault(j["no"],(f,ps)); used.add(f); break
ok=0; empty=0; miss=[]
for j in Z["juan"]:
    key=cn(j["no"]); nm="卷%s%s"%(key,j["name"])
    p=os.path.join(C,nm+".json"); d=json.load(io.open(p,encoding="utf-8"))
    secs=[s for s in d["sections"] if s.get("key") not in ("zizu","juanshou")]
    text=""
    if j["no"] in assigned:
        f,ps=assigned[j["no"]]; buf=[]
        for t in ps:
            if not t: continue
            if H.match(t): break
            buf.append(t)
        text="\n\n".join(buf[:40])
    if text: ok+=1
    elif j["no"] in assigned: empty+=1; text="原稿本卷无卷首导言，直接列部目。"
    else: miss.append(j["no"]); text="（本卷卷首未取到：原稿文件未匹配）"
    d["sections"]=[{"key":"juanshou","label":"卷首","text":text,"cites":[]}]+secs+[s for s in d["sections"] if s.get("key")=="zizu"]
    json.dump(d,io.open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("成文",ok,"无导言",empty,"未匹配",len(miss),miss[:12])