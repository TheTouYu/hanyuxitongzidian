import json,subprocess,os,glob
F="【438 半部】半＝从牛八声，剖牲；字族取两半、边界、分离诸面。"
N="字形：古文字字形库未收。"
D=[("㪵","bàn",F,"《说文》「量物分半也，从斗从半」——用斗量物、分其半；升五十谓之㪵。","b「闭剥」取「剥」：量而分。"),
("畔","pàn",F,"《说文》「田界也，从田半声」——田地的界限；又借为背叛、离开。","p「拼辟」取「辟」：田分而界。"),
("泮","pàn",F,"《说文》「诸侯乡射之宫，西南为水，东北为墙」——泮宫，一半有水；又冰释（泮涣）。","p取辟：水分而半。"),
("怑","bàn",F,"《集韵》「怑愌，不顺也」——不随心。","b取剥：心分而不顺。"),
("柈","pán",F,"《集韵》「槃，承槃也，或作柈」——盛物的盘；又木名。","p取辟：盘分而承。"),
("鉡","bàn",F,"《集韵》「锹也」——铁锹；又同槃。","b取剥：锹分而掘。"),
("𩢔","bàn",F,"《集韵》「𩢔䮗，马行貌」——马行之状。","b取剥：马分而驰。"),
("溿","pàn",F,"《正字通》「沜、溿，并俗字，泮，涯也」——水岸。","p取辟：水涯而分。"),
("詊","pàn",F,"《集韵》「巧言」——巧言。","p取辟：言巧而分。"),
("牉","pàn",F,"《玉篇》「半也，分也」；《广韵》「牉合，夫妇也」——半、分；合婚为牉合。","p取辟：体半而合。"),
("𧺾","pǎn",F,"《集韵》「走貌」——行走之状。","p取辟：行而分。"),
("𨒃","pàn",F,"《集韵》「去也」——离去。","p取辟：去而分。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取半部「分半／边界」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbl-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第438部「半部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡438c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡438c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡438c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
from docx import Document
d=Document(r"D:\字谱智能体\卷七十三  釆.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(299,min(len(ps),360)):
    if ps[j] and len(ps[j])>6: print(j, ps[j][:78])