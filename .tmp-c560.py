import json,subprocess,os,glob
F="【451 回部】回部余字取「盘旋回绕、昏乱、圆好」诸面。"
N="字形：古文字字形库未收。"
D=[("茴","huí",F,"《玉篇》「茴香，草名」——大茴香（八角）、小茴香，皆取香浓；《集韵》「藥艸，防風葉也」。","h「豁活」取「活」：草香而活。"),
("恛","huí",F,"《集韵》「昏亂皃」——神志昏乱，如回旋不安。","h取活：心昏而活。"),
("佪","huí",F,"《玉篇》「佪佪，惛也」；huái「俳佪」即徘徊——来回走动。","h取活：人回而活。"),
("廻","huí",F,"《正字通》「同回」——回旋、环绕。","h取活：旋绕而活。"),
("絗","hú",F,"《集韵》「縷縈也」——丝缕萦绕。","h取活：丝萦而活。"),
("㻁","guī",F,"《说文》「玫瑰，一曰圜好」，俗从回——圆润美好之玉。","g「隔估」取「隔」：玉圆而隔。"),
("䛛","huì",F,"《集韵》「膽气滿聲，一曰胡市也，一曰決後悔也」——高声、转手倒卖、决而后悔。","h取活：言满而活。"),
("䤧","huì",F,"《玉篇》「金䤧」——金名。","h取活：金结而活。"),
("䨓","léi",F,"「雷」之古文：籀文靁间有回，回象雷声回旋。","l「拢离」取「离」：雷震而离。"),
("𠲛","huí",F,"象声字：念咒语声。","h取活：声咒而活。"),
("𡏁","huì",F,"《集韵》「地形回屈」——地势回环屈曲。","h取活：地回而活。"),
("𡹯","huì",F,"《集韵》「山無草木也」——秃山，取回环之状。","h取活：山秃而活。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取回部「盘旋、环绕」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbp-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第451部「回部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡451b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡451b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡451b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))