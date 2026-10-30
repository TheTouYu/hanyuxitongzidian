import sys,glob,os,re,json,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"
cards={os.path.basename(p)[:-5] for p in glob.glob(ROOT+r"\web\public\cards\*.json")}
head={}
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for i,t in enumerate(ps):
        m=re.match(r"^(\d{1,3})[.．]\s*([\u3400-\u9fff]{1,2})部$",t)
        if not m: continue
        n=int(m.group(1))
        if n<100: head.setdefault(n,(m.group(2),ps,i))
print("1-99 部头(带部字)",len(head))
miss=[n for n in sorted(head) if head[n][0] not in cards]
print("缺卡",len(miss))
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
n=0
for num in miss:
    nm,ps,i=head[num]
    body=""
    for j in range(i,min(i+8,len(ps))):
        if ps[j].startswith(("本義","本义")): body=re.sub(r"^本[義义][：:]\s*","",ps[j]); break
    g=len(glob.glob(rf"{ROOT}\web\public\glyphs\{nm}\*.png"))
    sec=[{"key":"bengen","label":"字根本义","text":f"【第{num}部部首字·一級字根】"+body[:170],"cites":[]},
         {"key":"zigen","label":"字形","text":(f"字形：字形库存 {g} 形。" if g else "字形：字形库未收。"),"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":"本字为字根，字族另见本部下列条目。","cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"本部字族与他部交叉者见各字卡；此处只标本根义。","cites":[]},
         {"key":"shengmu","label":"声母义","text":"声母义：待按绪论补。","cites":[]}]
    json.dump({"char":nm,"pinyin":"","bus":[{"num":num,"name":nm}],"sections":sec},open(rf"{ROOT}\web\public\cards\{nm}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    n+=1
print("added",n)
subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 补部1-99部首卡(带部字标题)"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:100]); print("total",len(glob.glob(ROOT+r"\web\public\cards\*.json")))