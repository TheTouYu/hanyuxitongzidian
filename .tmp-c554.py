import json,subprocess,os,glob
from docx import Document
F="【445 串部】串部余字：取「贯穿、逃匿、环绕」诸面。"
N="字形：古文字字形库未收。"
D=[("竄","cuàn",F,"《说文》「匿也，从鼠在穴中」——鼠窜入穴，引申逃匿、放逐、改易文字。","c「次刺」取「刺」：鼠窜而刺。"),
("窜","cuàn",F,"「竄」的简化字，义同：逃匿、奔逃、删改。","c取刺：窜而刺。"),
("𠌼","huàn",F,"《集韻》「患，或作𠌼」——忧患之异体。","h「豁活」取「活」：忧而活。"),
("𡠛","huàn",F,"《集韻》「女字」——女子名用字。","h取活：借声记名。"),
("𤶱","huàn",F,"《集韻》「病也」——病名。","h取活：病而活。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取串部「贯穿／逃匿」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbv-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第445部「串部」（卷七十四 雈）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡445b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡445b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡445b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
import shutil
fs=[f for f in os.listdir(r"D:\字谱智能体") if "七十五" in f]
print("vol75:", fs)
if fs:
    d=Document(os.path.join(r"D:\字谱智能体",fs[0]))
    ps=[p.text.strip() for p in d.paragraphs]
    for i,t in enumerate(ps):
        if t and (t[0].isdigit() and ("部" in t) or "卷首" in t or "龠" in t[:4]):
            print("p",i,t[:80])