import json,subprocess,os,glob
F="【436 𠬜部·开闢支】棥＋𠬜＝双手打开门；《说文》「闢，开也，从门辟声」；讹变从幵，故与幵声字混。"
N="字形：古文字字形库未收。"
D=[("開","kāi",F,"从门从𠬜，象双手打开门；引申舒张、开放、通达、裂开、释张、开列。","k「口控」取「开」：门开而通。"),
("闢","pì",F,"《说文》「开也，从门辟声」——开辟、开列、条陈。","p「拼辟」取「辟」：推开而分。"),
("𥳐","qiǎn",F,"《玉篇》「𥳐䉳，户籍也」——户板。","q「亲缺」取「缺」：板分而列。"),
("鐦","kuí",F,"同「魁」——汤勺；又译元素 Cf（锎）。","k取开：勺分而取。"),
("𤡲","kāi",F,"《玉篇》「兽也」，疑为𤜵之讹。","k取开：兽分而奔。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取𠬜部「开列／分拨」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbe-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第436部「𠬜部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡436c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡436c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡436c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
from docx import Document
d=Document(r"D:\字谱智能体\卷七十三  釆.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(175,min(len(ps),235)):
    if ps[j] and len(ps[j])>6: print(j, ps[j][:78])