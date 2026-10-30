import sys,re,json,glob,os,subprocess,random
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
md=open(ROOT+r"\knowledge\hanzi-yinyuan\02z-shengmu-yi.md",encoding="utf-8").read()
m=re.search(r"###\s*零聲母諸部[^\n]*\n([\s\S]{0,700}?)<!-- CLAIM:END",md) or re.search(r"零聲母[^\n]*\n([\s\S]{0,700}?)<!-- CLAIM:END",md)
zero=set()
if m:
    for z in re.findall(r"[\u3400-\u9fff]",m.group(1)[:400]): zero.add(z)
print("零声母字符样本",len(zero))
n=0
for fp in glob.glob(ROOT+r"\web\public\cards\*.json"):
    d=json.load(open(fp,encoding="utf-8")); ch=d["char"]
    for s in d["sections"]:
        if s["key"]=="shengmu" and "本部未收 02z" in s["text"]:
            s["text"]="聲母義：零聲母——本部屬緒論「零聲母諸部」，無擬態聲母可系；音義取借聲一面。"
            n+=1
    json.dump(d,open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("改标零声母",n)
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 零声母诸部改标"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:80])
# 完整性抽查
cnt=0;bad=[]
for fp in random.sample(glob.glob(ROOT+r"\web\public\cards\*.json"),20):
    d=json.load(open(fp,encoding="utf-8"))
    ks={s["key"] for s in d["sections"]}
    if not {"bengen","zigen","xingpang","hengxiang","shengmu"}<=ks: bad.append(d["char"])
    elif any(len(s["text"])<6 for s in d["sections"]): cnt+=1
print("抽查20: 缺栏",bad,"短文本",cnt)