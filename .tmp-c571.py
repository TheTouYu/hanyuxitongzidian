import json,subprocess,os,glob
F="【455 兀部】兀＝高而上平（《说文》「高而上平也，从一在儿上」），象人首秃而高；引申突兀、动摇不安。"
N="字形：古文字字形库未收。"
D=[("兀","wù",F,"《说文》「高而上平也，从一在儿上」——高而平秃；引申突兀、兀自。","w「勿问」取「问」：高秃而问。"),
("杌","wù",F,"《说文》「木也」；《集韵》「樹無枝也」——无枝之木；杌陧，不安。","w取问：木秃而问。"),
("軏","yuè",F,"《说文》「車轅耑持衡者」——辕端与衡相接的销钉。","y「柔锐」取「锐」：辕端而锐。"),
("阢","wù",F,"《集韵》「阢隉，不安也」——危而不安。","w取问：危而不问。"),
("卼","wù",F,"《集韵》「卼臲，危也」——危动不安。","w取问：危动而问。"),
("扤","wù",F,"《说文》「動也，从手兀聲」——摇动。","w取问：手摇而问。"),
("矹","wù",F,"《集韵》「矹硉，石崖皃」——石崖高耸。","w取问：石高而问。"),
("鼿","wù",F,"《集韵》「鼻也」——鼻，兀然高起。","w取问：鼻高而问。"),
("泉","quán",F,"《说文》「水原也，象水流出成川形」——泉水源头。","q「亲缺」取「缺」：水出而缺。"),
("線","xiàn",F,"《说文》「縷也，从糸泉聲」——线，取泉流细长不断。","x「续消」取「续」：线续而消。"),
("腺","xiàn",F,"《玉篇》「腺，肉也」——腺体，取泉流分泌。","x取续：液续而消。"),
("湶","quán",F,"《集韵》「泉水也」——同泉。","q取缺：泉涌而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取兀部「高而上平／动摇」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbe-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第455－456部（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡455a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡455a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡455a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))