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
F2="【第602部「𠃬部」】𠃬＝从水流過上下兩口，注田疇、注酒敬客、注範鑄器三義；引申求告、叩擊、長久、蒙覆。"
F3="【第603部「周部」】周＝象方格內刻畫有紋飾之形，指雕刻，「彫（雕）」之初文，《說文》「琢文也」；引申周密、周遍、周旋。"
D=[("譸","zhōu",F2,"从言壽聲：詶也（《說文》「詶也」），譸張，誑也。","zh「凿总」取「凿」：言誑而凿。"),
("𠷎","chóu",F2,"从口𢏚聲：咨也、誰也（《廣韻》《說文》），嗟歎聲。","ch「刺持」取「持」：歎持而發。"),
("𤾊","chóu",F2,"从白𢏚聲：詞也（《說文》「詞也」），發語詞。","ch取刺持：言發而持。"),
("䮻","dǎo",F2,"从馬壽聲：禱牲馬祭也（《說文》引《詩》「既禡既禂」），為牲馬祭。","d「囤动」取「囤」：祭聚而動。"),
("𢶈","dǎo",F2,"从手𠷎聲：手推也，一曰築也（《說文》），搗。","d取囤动：手聚而動。"),
("𣪐","chóu",F2,"从殳𠃬聲：懸物𣪐擊（《說文》），懸物搗擊。","ch取刺持：擊持而發。"),
("𢿟","chóu",F2,"从攴𠷎聲：棄也（《說文》「棄也」），《周書》以為討。","ch取刺持：棄持而擊。"),
("䬞","táo",F2,"从風壽聲：風大聲（《玉篇》「風大聲」），大風。","t「涂突」取「涂」：風突而涂。"),
("周","zhōu",F3,"象方格內刻畫紋飾之形：雕刻，「彫」之初文（《說文》「琢文也」）；引申周密、周遍、周旋。","zh取凿总：刻紋而凿。"),
("彫","diāo",F3,"从彡周聲：琢文也（《說文》「琢文也」），雕飾。","d取囤动：雕聚而動。"),
("雕","diāo",F3,"从隹周聲：鷻也（《說文》「鷻也」），大型猛禽；借為雕飾、雕琢。","d取囤动：鳥聚而動。"),
("凋","diāo",F3,"从仌周聲：半傷也（《說文》「半傷也」），凋零、凋敝。","d取囤动：冰聚而動。")]
rows=[]
for ch,p,F0,xp,sm in D:
    num=602 if F0==F2 else 603
    nm="𠃬" if num==602 else "周"
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"𠃬部取「注、告、擊、久」：譸誑、𠷎歎、𤾊詞、䮻馬祭、𢶈手推、𣪐懸擊、𢿟棄、䬞大風；周部取「刻畫周遍」：周刻紋、彫雕飾、雕猛禽、凋零。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":nm}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lzhou4-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":f"源自《系統漢語》第{num}部「{nm}部」（卷一百 壽）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 602余+603周首12字")[-40:])
p2=ROOT+r"\intake\20261024-字卡603a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡603a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡603a.json"); print(git("commit","-m","knowledge: 602余+603周首12条")[-40:])