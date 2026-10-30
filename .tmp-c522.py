import json,subprocess,os,glob
F="【432 隶部】隶（dài）＝从又抓动物尾巴，象抓住尾巴从后追及，为「逮」之初文；转义附属、剩余（意为割剩的尾巴）、勉强追及、抓不牢而逃脱（放纵安逸）。"
N="字形：古文字字形库未收。"
D=[("逮","dài",F,"《说文》「唐逮，及也，从辵隶声」——到、及；捉拿。","d「囤动」取「动」：追而及之。"),
("𨽿","dài",F,"《说文》「及也，从隶枲声」——赶上；枲为麻无实者，夏麻宜衣，或取其音。","d取动：追及。"),
("㥆","tuì",F,"《说文》「肆也，从心隶声」——放纵；《广雅》「忘也」。","t「涂突」取「突」：放而突。"),
("齂","xiè",F,"《说文》「卧息也，从鼻隶声，读若虺」——鼾声。","x「续消」取「消」：气续而息。"),
("隸","lì",F,"《说文》「附箸也，从隶柰声」——附着、奴仆（后世隶仆义）。","l「拢离」取「拢」：附而不离。"),
("𣟌","lì",F,"《说文》「木也」；络丝车的摇把——手抓握并转动之处。","l取拢：握而转。"),
("𥶾","lì",F,"《广韵》「笘也」——古代小孩写字用的简牍。","l取离：片片相离。"),
("䇐","lì",F,"《说文》「临也，从立从隶」——看视；与莅、涖同。","l取拢：临而近。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取隶部「追及／附著」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lb5-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第432部「隶部」（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡432a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡432a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡432a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
from docx import Document
d=Document(r"D:\字谱智能体\卷七十一  聿部.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(250,min(len(ps),300)):
    if ps[j] and len(ps[j])>8: print(j, ps[j][:90])