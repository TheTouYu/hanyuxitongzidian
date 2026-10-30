import json,subprocess,os,glob
F="【454 元部】元＝人首（《说文》「始也，从一从兀」），引申首、始、大；诸字取「首、始、圆全」诸面。"
N="古文字字形库未收。"
D=[("沅","yuán",F,"《说文》「水，出牂牁故且蘭，東北入江」——沅江。","y「柔锐」取「锐」：水长而锐。"),
("芫","yán",F,"《说文》「魚毒也」——芫花（毒鱼）、芫荽（香菜）。","y取锐：草毒而锐。"),
("冠","guān",F,"《说文》「絭也，所以絭髮，弁冕之總名」——帽子；guàn 加冠、居首。","g「隔估」取「隔」：首戴而隔。"),
("鼋","yuán",F,"《说文》「大鼈也」——大鳖，元有大义。","y取锐：鳖大而锐。"),
("頑","wán",F,"《说文》「㨡頭也」——头钝难劈，引申愚钝、顽固。","w「勿问」取「问」：头钝而问。"),
("完","wán",F,"《说文》「全也，从宀元聲」——屋宇完好，引申完整、完毕。","w取问：全而问。"),
("阮","ruǎn",F,"《说文》「代郡五阮關也」——关名；后为姓、乐器名（阮咸）。","r「柔锐」取「柔」：关隘而柔。"),
("杬","wán",F,"《说文》「木也」——木名，皮可煎汁藏果。","w取问：木大而问。"),
("邧","yuán",F,"《说文》「地名」——邑名。","y取锐：地名借声。"),
("坃","yuán",F,"《集韵》「地名」——地名用字。","y取锐：地名借声。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取元部「首、始、圆全」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbf-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第454部「元部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡454a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡454a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡454a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))