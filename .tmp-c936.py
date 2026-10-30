import sys,glob,os,re,json,subprocess
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
sm={}
md=open(ROOT+r"\knowledge\hanzi-yinyuan\02z-shengmu-yi.md",encoding="utf-8").read()
for m in re.finditer(r"###\s*(\S{1,3})部：([^\n]{0,40})",md): sm[m.group(1)]=m.group(2).strip()
n=0
for fp in glob.glob(ROOT+r"\web\public\cards\*.json"):
    d=json.load(open(fp,encoding="utf-8"))
    ch=d["char"]
    if ch not in heads: continue
    num,ps,i=heads[ch]
    seg=[]
    for j in range(i+1,min(i+30,len(ps))):
        t=ps[j]
        if re.match(r"^\d{1,3}[.．]",t): break
        seg.append(t)
    def grab(keys):
        for t in seg:
            if t.startswith(keys): return re.sub(r"^[^：:]*[：:]\s*","",t)
        return ""
    ben=grab("本義") or grab("本义"); zhuan=grab("轉義"); yin=grab("音源"); bian=grab("辯證")
    fam=[t for t in seg if re.match(r"^[\u3400-\u9fff\U00020000-\U0002ffff]{1,3}[，,]?\s*[a-zA-Zü]",t) and "《" in t]
    g=len(glob.glob(rf"{ROOT}\web\public\glyphs\{ch}\*.png"))
    smt=sm.get(ch)
    sec=d["sections"]
    get=lambda k:[s for s in sec if s["key"]==k][0]
    get("bengen")["text"]=f"【第{num}部部首字·一級字根】{ben[:420] or get('bengen')['text']}"
    get("zigen")["text"]=(f"字形：字形库存 {g} 形（見字根字形圖）。" if g else "字形：字形庫未收。")
    get("xingpang")["text"]="形旁聲旁：本字為部內字根（象形／象意），形義合一；其字族在本部下。"+(f" 轉義：{zhuan[:120]}" if zhuan else "")
    get("hengxiang")["text"]=("同部字族："+"、".join(re.split(r"[，,]",fam[0])[0] for _ in [0]) if False else ("同部字族見本部各條："+"；".join(x[:40] for x in fam[:5]) if fam else "同部字族見本部各條；本字單用。"))
    get("shengmu")["text"]=(f"聲母義（{ch}部）：{smt}" if smt else "聲母義：本部未收 02z 條，按緒論取聲母擬態義一面，待補。")
    if bian: get("shengmu")["text"]+=f" 辨證：{bian[:120]}"
    json.dump(d,open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    n+=1
print("upgraded",n)
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 部首卡按五步补音源辨證声母义"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:90])