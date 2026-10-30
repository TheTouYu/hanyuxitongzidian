import sys,glob,os,re,json,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"
PYR=re.compile(r"[a-zA-Züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]{2,8}")
heads={}
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for i,t in enumerate(ps):
        m=re.match(r"^(\d{1,3})[.．]\s*(\S{1,2})部$",t)
        if m: heads.setdefault(m.group(2),(int(m.group(1)),ps,i))
n=p=0
for fp in glob.glob(ROOT+r"\web\public\cards\*.json"):
    d=json.load(open(fp,encoding="utf-8"))
    if d.get("pinyin"): continue
    ch=d["char"]; n+=1
    if ch in heads:
        num,ps,i=heads[ch]
        txt=" ".join(ps[i:i+6])
        cands=[x for x in PYR.findall(txt) if x.islower() or any(c in x for c in "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ")]
        if cands: d["pinyin"]=cands[0]; p+=1
    for s in d["sections"]:
        if s["key"]=="xingpang" and "字根" in s["text"]:
            s["text"]="形旁聲旁：本字即部內字根，形義合一；其字族見本部下列各條。"
        if s["key"]=="hengxiang" and "只標本根義" in s["text"]:
            s["text"]="橫向對照：本字為部根，同族比況見本部各字卡；此處只標本根義。"
    json.dump(d,open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("骨卡",n,"补拼音",p)
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 骨卡补拼音与六书栏"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:90])