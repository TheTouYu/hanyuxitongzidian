import json,subprocess,os,glob
F="【430 戾部】戾＝犬后腿直立欲扑（马抬前腿同义），引申乖张、凶残；字族多取「立而不稳／曲戾」之状。"
N="字形：古文字字形库未收。"
D=[("蜧","lún",F,"《说文》「蛇属，黑色，潜于神渊，能兴风雨」——神蛇，或作蜦。","l「拢离」取「离」：蟠曲而离。"),
("唳","lì",F,"《说文》「鹤鸣也」——鹤雁高亢鸣叫，含惊惧意。","l取离：声高而离。"),
("淚","lèi",F,"《正韵》「目液也」——眼泪；取义同泣，泪挂眼睑之状。","l取离：泪离目而下。"),
("棙","lì",F,"《集韵》「琵琶，其拨曰棙」——弹拨弦的木片。","l取离：拨弦使离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取戾部「曲戾而立」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lb3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第430部「戾部」（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡430a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡430a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡430a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
from docx import Document
d=Document(r"D:\字谱智能体\卷七十一  聿部.docx"); ps=[(p.text or "").strip() for p in d.paragraphs]
for j in range(215,min(len(ps),250)):
    if ps[j] and len(ps[j])>8: print(j, ps[j][:95])