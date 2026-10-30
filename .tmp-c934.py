import sys,glob,re,json,os,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
ROOT=r"D:\系统汉字"
want={12,21,23,61,70,78}
found={}
for f in glob.glob(r"D:\字谱智能体\*.docx"):
    try: ps=[p.text.strip() for p in Document(f).paragraphs]
    except: continue
    for i,t in enumerate(ps):
        m=re.match(r"^(\d{1,3})[.．]\s*(\S{1,2})部$",t)
        if m and int(m.group(1)) in want: found.setdefault(int(m.group(1)),(m.group(2),ps,i))
print("found",sorted(found))
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
n=0
for num,(nm,ps,i) in sorted(found.items()):
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
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 补最后6部首卡(𦣞𠂔ㄗ𦥑𠌶𦐇)"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:100])