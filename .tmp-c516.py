import json,subprocess,os,glob
FY="【427 聿部·肅·飛】肅有撑船浮行一面，故鷫（神鸟）、驌（良马）、䎘（鸟羽声）取其浮飞疾行。"
FZ="【427 聿部·肁】肁＝从戶从聿，聿指拿开顶门的竹杠，象开门，故为「始开」；转义开端、初始。《说文》「始开也」。辨证：肁之初文本当为「启」（从户从口）；「肈」甲骨文从戈从户，象破门攻打，故又引申开始、谋划。音源：本聿声，因有开始义而义音同「兆」。"
N="字形：古文字字形库未收。"
D=[("䎘","sù",FY,"《正韵》「䎘䎘，鸟羽声」；《广雅》「飞也」——鸟振羽而飞。","s「失收」取「收」：羽收而振。"),
("驌","sù",FY,"《玉篇》「骕骦，古之良马」——骏马名。","s取收：马收蹄而疾。"),
("肁","zhào",FZ,"从户从聿，以竹杠开门——始开；引申开端、初始。","zh「凿总」取「凿」：凿门而开。"),
("肈","zhào",FZ,"甲骨文从戈从户，执戈破门——攻城；引申开始、谋划。","zh取凿：戈凿门。"),
("肇","zhào",FZ,"《说文》「击也，从攴肈省声」——敲打；又始也、敏也。","zh取凿：击而始。")]
for ch,p,F,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「竹竿／持械触物」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"yb7-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第427部「聿部」（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡427g2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡427g.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡427g.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
from docx import Document
d=Document(r"D:\字谱智能体\卷七十一  聿部.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(150,min(len(ps),200)):
    if ps[j] and len(ps[j])>8: print(j, ps[j][:95])