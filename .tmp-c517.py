import json,subprocess,os,glob
F="【428 曰部】曰＝从口上有一，象张口说话；《说文》「词也」。转义：为、叫作；又作语助。音源：借音字，因有言辞义而义音同「聿」（《诗》「曰为改岁」《汉书》作「聿为」）。字族一支取「张口说话→裂开、连续」。"
N="字形：古文字字形库未收。"
D=[("曰","yuē","从口上一，象张口说话；引申为、叫作，又作语端之词。","y「柔锐」取「锐」：口出言而锐。"),
("汩","gǔ","《说文》「治水也」——治水；又乱也、汩没（淹没）、疾行。","g「隔估」取「隔」：水隔而治。"),
("欥","yú","《说文》「诠词也」——表示诠释的虚词；又辞、喜。","y取锐：词锋微锐。"),
("𡿯","yù","《说文》「水流也」——水行貌。","y取锐：水流锐进。"),
("𢪏","hú","《广韵》「牵物动转也」；《集韵》「裂也」，或同掘、滑。","h「豁活」取「豁」：牵而豁开。"),
("𩒳","huì","《说文》「昧前也」——实为「湏」之讹字。","h取豁：借形记讹。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取曰部「张口出言／裂开连续」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"yb8-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第428部「曰部」（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡428a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡428a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡428a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
from docx import Document
d=Document(r"D:\字谱智能体\卷七十一  聿部.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(165,min(len(ps),215)):
    if ps[j] and len(ps[j])>8: print(j, ps[j][:95])