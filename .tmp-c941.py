import sys,glob,os,re,json,subprocess,random
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"
heads={}
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for i,t in enumerate(ps):
        m=re.match(r"^(\d{1,3})[.．]\s*(\S{1,2})部$",t)
        if m and m.group(2) not in heads: heads[m.group(2)]=(int(m.group(1)),ps,i)
fill=0
for fp in glob.glob(ROOT+r"\web\public\cards\*.json"):
    d=json.load(open(fp,encoding="utf-8")); ch=d["char"]
    if d.get("pinyin"): continue
    if ch not in heads: continue
    num,ps,i=heads[ch]
    txt=" ".join(ps[i:i+8])
    m=re.search(r"[（(]?\s*([a-züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]{1,10})\s*[，,]",txt)
    if m:
        d["pinyin"]=m.group(1); fill+=1
        json.dump(d,open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("补拼音",fill)
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 再补拼音"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:70])
# 审计 50 张随机卡
miss=[];ph=[]
for fp in random.sample(glob.glob(ROOT+r"\web\public\cards\*.json"),50):
    d=json.load(open(fp,encoding="utf-8"))
    ks={s["key"] for s in d["sections"]}
    if not {"bengen","zigen","xingpang","hengxiang","shengmu"}<=ks: miss.append(d["char"])
    if any("待" in s["text"] and ("待補" in s["text"] or "待按" in s["text"] or "待回" in s["text"]) for s in d["sections"]): ph.append(d["char"])
print("缺栏",len(miss),miss[:5],"含待补",len(ph),ph[:8])