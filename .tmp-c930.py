import sys,json,glob,os,re,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"
cards={os.path.basename(p)[:-5] for p in glob.glob(ROOT+r"\web\public\cards\*.json")}
# 声母义 索引
sm={}
md=open(ROOT+r"\knowledge\hanzi-yinyuan\02z-shengmu-yi.md",encoding="utf-8").read()
for m in re.finditer(r"###\s*(.{1,4}?)部：([^（\n]+)（([^）]*)）\s*\n([\s\S]{0,220}?)<!-- CLAIM:END",md):
    sm[m.group(1)]=(m.group(2),m.group(3),m.group(4).strip().replace("\n"," ")[:150])
head={}
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for i,t in enumerate(ps):
        m=re.match(r"^(\d{3})[.．]\s*(.{1,4}?)部$",t)
        if m: head.setdefault(int(m.group(1)),(m.group(2),f,i,ps))
miss=[n for n in sorted(head) if head[n][0] not in cards]
print("missing",len(miss))
n=0
for num in miss:
    nm,f,i,ps=head[num]
    body=""
    for j in range(i,min(i+7,len(ps))):
        if ps[j].startswith("本義"): body=re.sub(r"^本義[：:]\s*","",ps[j]); break
    if not body:
        for j in range(i,min(i+7,len(ps))):
            if ps[j] and not ps[j].startswith(("▲","字族","轉義")): body=ps[j]; break
    body=body[:170]
    g=len(glob.glob(rf"{ROOT}\web\public\glyphs\{nm}\*.png"))
    s=sm.get(nm)
    smtxt=f"{s[0]}（{s[1]}）：{s[2]}" if s else "声母义：本字为字根，声母拟态义待按绪论补。"
    zt=f"字形：字形库存 {g} 形。" if g else "字形：字形库未收。"
    fp=rf"{ROOT}\web\public\cards\{nm}.json"
    sec=[{"key":"bengen","label":"字根本义","text":f"【第{num}部部首字·一級字根】"+body,"cites":[]},
         {"key":"zigen","label":"字形","text":zt,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":"本字为字根，字族另见本部下列条目。","cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"本部字族与他部交叉者见各字卡；此处只标本根义。","cites":[]},
         {"key":"shengmu","label":"声母义","text":smtxt,"cites":[]}]
    json.dump({"char":nm,"pinyin":"","bus":[{"num":num,"name":nm}],"sections":sec},open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    n+=1
print("added",n)
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 补部首卡247张完(原稿本義+声母义索引)"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:150])
print("total cards",len(glob.glob(ROOT+r"\web\public\cards\*.json")))