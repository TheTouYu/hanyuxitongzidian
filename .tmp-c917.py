import sys,json,subprocess,os,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
def git(*a):
    r=subprocess.run([ROOT+r"\tools\git.cmd"]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
N="字形：古文字字形库未收。"
F1="【第597部「用部」】用＝象蟲蛹形，中空可燃；蛹化過程引申包藏、安寧、泥濘之狀。"
F2="【第598部「亢部」】亢＝象人頸（喉管）之形，《說文》「人頸也」；頸直而高，引申高亢、抗禦、亢旱。"
D=[("甯","nìng",F1,"从用寧聲：所願也（《說文》「所願也」），寧願、安寧；通「寧」。","n「纳弄」取「纳」：願纳而弄。"),
("澝","nìng",F1,"从水寧聲：同「濘」，淤積的泥水氹（《字海》）。","n取纳弄：泥纳而弄。"),
("橣","nìng",F1,"从木寧聲：木名（《集韻》），檸檬，味澀。","n取纳弄：木涩而弄。"),
("𧑗","nìng",F1,"从虫寧聲：蟲名，似蟬（《集韻》），觸之腹脹。","n取纳弄：蟲脹而弄。"),
("𩕋","nǐng",F1,"从頁寧聲：頂顚也（《集韻》），頭頂。","n取纳弄：頂高而弄。"),
("𤢆","nìng",F1,"从犬寧聲：同「獰」，猙獰，犬毛；一曰惡也（《集韻》）。","n取纳弄：犬惡而弄。"),
("𡛾","nǎi",F1,"从女寧聲：乳也（《龍龕》），通「妳/嬭」，乳房、奶。","n取纳弄：乳纳而弄。"),
("𦕘","tīng",F1,"从耳寧聲：正作「聽」（《龍龕》），聆也。","t「涂突」取「涂」：聲入而突。"),
("亢","kàng",F2,"象人頸之形：人頸也（《說文》「人頸也」），頸喉；引申高、抗、亢旱。","k「口控」取「控」：頸直而控。"),
("抗","kàng",F2,"从手亢聲：扞也（《說文》「扞也」），抵抗、高抗。","k取口控：手扞而控。"),
("伉","kàng",F2,"从人亢聲：匹也（《說文》「匹也」），伉儷；伉直。","k取口控：人匹而控。"),
("吭","háng",F2,"从口亢聲：喉嚨（《廣韻》「鳥喉」），引吭高歌。","h「豁活」取「豁」：喉開而豁。")]
rows=[]
for it in D:
    ch,p,F0,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    num=597 if F0==F1 else 598
    nm="用" if num==597 else "亢"
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"用部取「包藏、安寧」：甯願、澝泥、橣木、𧑗蟲、𩕋頂、𤢆獰、𡛾乳、𦕘聽；亢部取「頸直而高」：亢頸、抗扞、伉匹、吭喉。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":nm}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lyong4-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":f"源自《系統漢語》第{num}部「{nm}部」（卷九十八 銿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 597尾+598亢部首12字")[-60:])
p2=ROOT+r"\intake\20261024-字卡598a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡598a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡598a.json"); print(git("commit","-m","knowledge: 597尾+598亢部首12条")[-60:])