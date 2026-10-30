import json,subprocess,os,glob
F="【437 八部·分支】分＝从刀八声，剖开；字族取分散、众多、乱起诸面。"
N="字形：古文字字形库未收。"
D=[("紛","fēn",F,"《说文》「马尾韬也，从糸分声」——包藏马尾的套子（取纷聚义）；引申纷纭、众多、杂乱。","f「附分」取「分」：丝乱而分。"),
("頒","fén",F,"《说文》「大头也，从页分声」——大头；又鬓。bān，布也、赐也（颁赐）。","b「闭剥」取「剥」：分而布之。"),
("忿","fèn",F,"《说文》「悁也，从心分声」——气不平、恨怒。","f取分：气分而怒。"),
("棼","fēn",F,"《说文》「复屋栋也，从林分声」——重屋的栋；林木棼错、乱也。","f取分：木分而乱。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取分部「分散／剖开」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbh-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第437部「八部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡437c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡437c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡437c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
from docx import Document
d=Document(r"D:\字谱智能体\卷七十三  釆.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(235,min(len(ps),300)):
    if ps[j] and len(ps[j])>6: print(j, ps[j][:78])