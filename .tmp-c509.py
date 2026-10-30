import json,subprocess,os,glob
F="【426 皆部】皆＝二虎直立相抗而齐；本部余字多取「齐一／威猛」两面——众口齐声、众病齐发、众草齐长、骨节相齐。"
N="字形：古文字字形库未收。"
D=[("𢝷","xié","人名用字。","借声记名。"),
("𢔡","kāi","《广韵》「徘𢔡，行恶」——行步邪僻。","j取聚：行步偏聚。"),
("勓","kài","《集韵》「劾，勤力也，一曰勉也」——勉力、勤力。","j取聚：力聚而勤。"),
("㾬","jiē","《正字通》同痎——老疟发作无时名㾬疟；痎为二日一发之疟。","j取聚：寒热齐发。"),
("蝔","jiē","《广韵》「虫名」；《淮南子》「蝔知雨至」，虫大如笔管、长三寸，俗名猥狗，天雨则藏草木下。","j取聚：虫聚而藏。"),
("𥏪","kǎi","《集韵》「桂林谓人短为矲雉，或作𥏪」——身材短小。","j取聚：身短而聚。"),
("𦎥","qiān","《集韵》「羟，羊名」——羊名。","j取聚：借声记物。"),
("𧳧","xiē","《集韵》「兽名」。","j取聚：借声记物。"),
("𦂄","kāi","《说文》「大丝也」——粗大之丝。","j取聚：丝聚而粗。"),
("𦝨","jiē","《说文》「臞也」——瘦而肋骨外露，如阶之级级；一说当为肥。","j取聚：骨节相聚而露。"),
("𩩰","jiē","《篇海类编》「同𦝨，瘦也」；hái 同骸，胫骨。","j取聚：骨聚而瘦。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取皆部「齐一相聚」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"jb3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第426部「皆部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡426c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡426c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡426c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))