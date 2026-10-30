import sys,json,glob,os,re,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"
cards={os.path.basename(p)[:-5] for p in glob.glob(ROOT+r"\web\public\cards\*.json")}
head={}
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for i,t in enumerate(ps):
        m=re.match(r"^(\d{3})[.．]\s*(.{1,4}?)部$",t)
        if m: head.setdefault(int(m.group(1)),(m.group(2),f,i,ps))
miss=[n for n in sorted(head) if head[n][0] not in cards]
print("missing",len(miss))
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
n=0
for num in miss[:40]:
    nm,f,i,ps=head[num]
    txt=""
    for j in range(i,min(i+6,len(ps))):
        if ps[j].startswith("本義"): txt=ps[j]; break
    if not txt:
        for j in range(i,min(i+6,len(ps))):
            if ps[j] and not ps[j].startswith(("▲","字族","轉義")): txt="本義："+ps[j]; break
    body=re.sub(r"^本義[：:]\s*","",txt)[:160]
    if body.startswith("本義"): body=body[3:]
    fp=rf"{ROOT}\web\public\cards\{nm}.json"
    if os.path.exists(fp): continue
    sec=[{"key":"bengen","label":"字根本义","text":f"【第{num}部部首字·一級字根】"+body,"cites":[]},
         {"key":"zigen","label":"字形","text":"字形：见字根字形图。","cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":"本字为字根，字族另见本部下列条目。","cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"本部字族与他部交叉者见各字卡；此处只标本根义。","cites":[]},
         {"key":"shengmu","label":"声母义","text":"" ,"cites":[]}]
    json.dump({"char":nm,"pinyin":"","bus":[{"num":num,"name":nm}],"sections":sec},open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    n+=1
print("added",n)
r=subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 补部首卡40张(据原稿部头本義)"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:200])