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
F1="【第607部「褭部」】褭＝从馬从衣：以組帶馬也（《說文》），絲帶系馬；一曰馬之飄逸（騕褭，良馬）；引申柔長（裊）。"
F2="【第608部「雔部」】雔＝从二隹相對：雙鳥也（《說文》），兩鳥相鬥或相和鳴；實即「讎」之初文，可視為隹之二疊表群鳥；引申伴侶、應驗、售賣、仇怨、報復、償付。"
D=[("褭","niǎo",F1,"从馬从衣：以組帶馬也（《說文》「以組帶馬也」），絲帶系馬；騕褭，良馬。","n「纳弄」取「纳」：帶系而纳。"),
("㒟","niǎo",F1,"从人褭聲：偠㒟，舞者㒟身若環（《玉篇》），細腰。","n取纳弄：身曲而纳。"),
("䃵","niáo",F1,"从石褭聲：山曲曰䃵（《集韻》），山曲處。","n取纳弄：石曲而纳。"),
("𢴶","niǎo",F1,"从手褭聲：摘也、搦也（《廣韻》《字彙》）。","n取纳弄：手摘而纳。"),
("𨽖","niǎo",F1,"从阜褭聲：偃低皃（《集韻》）。","n取纳弄：阜低而纳。"),
("㠡","niǎo",F1,"从山褭聲：岰㠡，山皃（《集韻》）。","n取纳弄：山曲而纳。"),
("𣟊","niǎo",F1,"从木褭聲：木長弱皃（《集韻》），柔長之木。","n取纳弄：木長而纳。"),
("𨳀","niǎo",F1,"从門褭聲：柔長也（《集韻》）。","n取纳弄：門長而纳。"),
("雔","chóu",F2,"从二隹相對：雙鳥也（《說文》「雙鳥也」），兩鳥相鬥或相和鳴，讎之初文。","ch「刺持」取「持」：雙鳥持而對。"),
("讎","chóu",F2,"从言雔聲：對答也（《說文》「猶𧭭也」），匹偶、仇怨、校讎、償付。","ch取刺持：言對而持。"),
("犨","chōu",F2,"从牛雔聲：牛息聲（《說文》「牛息聲」），牛喘息、牛名。","ch取刺持：牛息而持。"),
("㘜","chóu",F2,"雔之俗字：雙鳥也（《五音集韻》），《正字通》以為讎字之訛。","ch取刺持：鳥口而持。")]
rows=[]
for ch,p,F0,xp,sm in D:
    num=607 if F0==F1 else 608
    nm="褭" if num==607 else "雔"
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"褭部取「以組帶馬、柔長」：褭系馬、㒟細腰、䃵山曲、𢴶摘、𨽖偃低、㠡山、𣟊木長、𨳀柔長；雔部取「雙鳥相對」：雔雙鳥、讎對答、犨牛息、㘜俗字。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":nm}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lfinal-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":f"源自《系統漢語》第{num}部「{nm}部」（卷一百 壽）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 607褭部+608雔部12字 全书部目成卡")[-50:])
p2=ROOT+r"\intake\20261024-字卡608a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡608a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("err",v.get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡608a.json"); print(git("commit","-m","knowledge: 607/608收尾12条 全书部目成卡")[-50:])
print("cards",len(glob.glob(ROOT+r"\web\public\cards\*.json")))