import json,subprocess,os,glob
from docx import Document
F="【451 回部】回＝象回旋之形（《说文》「轉也，从囗，中象回轉形」），本义回旋、环绕；转义返回、回报、邪曲。"
N="字形：古文字字形库未收。"
D=[("回","huí",F,"《说文》「轉也，从囗，中象回轉形」——回旋、环绕；引申返回、回报、邪曲。","h「豁活」取「活」：转环而活。"),
("迴","huí",F,"「回」的后起分别字，专表回旋、绕行、回避。","h取活：旋绕而活。"),
("徊","huái",F,"《集韵》「徘徊，不进皃」——来回踱步、迟疑不进。","h取活：往复而活。"),
("洄","huí",F,"《说文》「溯洄也，从水从回」——《诗》「溯洄从之」：逆流而上。","h取活：水回而活。"),
("蛔","huí",F,"《说文》「腹中長蟲也，从虫回聲」——蛔虫，盘曲如回。","h取活：虫盘而活。"),
("痐","huí",F,"《集韵》「腹中長蟲」——同蛔，腹疾。","h取活：疾回而活。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取回部「回旋、环绕」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbq-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第451部「回部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡451a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡451a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡451a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
d=Document(r"D:\字谱智能体\卷七十五  叀.docx")
ps=[p.text.strip() for p in d.paragraphs]
for j in range(119,200):
    t=ps[j]
    if t and len(t)<95: print("p",j,t[:200])