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
F="【第604部「刀部」】刀＝象砍刀形，《說文》「兵也。象形」；字族多取「切割、斷絕、裁製」一面。"
D=[("刀","dāo",F,"象砍刀形：兵也（《說文》「兵也。象形」），切削之器。","d「囤动」取「囤」：刃聚而動。"),
("初","chū",F,"从刀从衣：裁衣之始也（《說文》「始也。从刀从衣。裁衣之始也」），開始；未形成字族，附於刀部。","ch「刺持」取「刺」：刀刺而持。"),
("絕","jué",F,"从糸从刀从卩：斷絲也（《說文》「絕，斷絲也」），象不連體、絕二絲。","j「聚决」取「决」：絲決而斷。"),
("剛","gāng",F,"从刀岡聲：彊斷也（《說文》「彊斷也」），剛強。","g「隔估」取「隔」：刀隔而斷。"),
("剄","jǐng",F,"从刀巠聲：刑也（《說文》「刑也」），割頸。","j取聚决：頸斷而决。"),
("刎","wěn",F,"从刀勿聲：剄也（《說文》「剄也」），刎頸。","w? 零聲母；此處借聲。"),
("判","pàn",F,"从刀半聲：分也（《說文》「分也」），判分、判斷。","p「拼辟」取「拼」：分拼而斷。"),
("刺","cì",F,"从刀朿聲：直傷也（《說文》「直傷也」），刺擊。","c「刺持」取「刺」：刀刺而持。"),
("副","fù",F,"从刀畐聲：判也（《說文》「判也」），副貳、剖開。","f「附分」取「分」：附分而斷。"),
("剖","pōu",F,"从刀咅聲：判也（《說文》「判也」），剖開。","p取拼辟：剖拼而斷。"),
("剡","yǎn",F,"从刀炎聲：銳利也（《說文》「銳利也」），剡木為矢。","y? 零聲母；此處借聲。"),
("券","quàn",F,"从刀𢍏聲：契也（《說文》「契也」），契券、券書。","q「亲缺」取「亲」：契亲而斷。")]
rows=[]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"刀部同取「切割、斷絕、裁製」一面：刀兵、初裁衣、絕斷絲、剛彊斷、剄割頸、刎剄、判分、刺直傷、副判、剖判、剡銳、券契。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":604,"name":"刀"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"ldao-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第604部「刀部」（卷一百 壽）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 604刀部12字")[-40:])
p2=ROOT+r"\intake\20261024-字卡604a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡604a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡604a.json"); print(git("commit","-m","knowledge: 604刀部12条")[-40:])