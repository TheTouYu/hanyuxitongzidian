import json,subprocess,os,glob
F="【458 玄部】玄＝幽深黑赤；玄支取「幽暗、旋转、悬垂」诸面；459 員部＝从口从貝，象鼎圆口（圆之初文）。"
N="字形：古文字字形库未收。"
D=[("炫","xuàn",F,"《说文》「燿也」——火光炫耀；引申炫示。","x「续消」取「续」：光耀而续。"),
("眩","xuàn",F,"《说文》「目無常主也」——眼花缭乱、眩惑。","x取续：目乱而续。"),
("鉉","xuàn",F,"《说文》「舉鼎也」——《易》「鼎黃耳金鉉」：举鼎的横杠。","x取续：鼎举而续。"),
("昡","xuàn",F,"《集韵》「日光也」——日光炫耀。","x取续：日光而续。"),
("玅","miào",F,"「妙」之异体——微妙、美妙，取幽玄难测。","m「蒙末」取「末」：玄妙而末。"),
("袨","xuàn",F,"《说文》「盛服也」——黑色盛服。","x取续：衣玄而续。"),
("盷","xuán",F,"《集韵》「目大也」——目大而转。","x取续：目转而续。"),
("員","yuán",F,"《说文》「物數也，从貝口聲」——本象鼎圆口（圆之初文），引申员数。","y「柔锐」取「锐」：圆而锐。"),
("圓","yuán",F,"《说文》「圜全也」——圆形、圆满。","y取锐：圆全而锐。"),
("隕","yǔn",F,"《说文》「從高下也」——从高处坠落。","y取锐：坠而锐。"),
("損","sǔn",F,"《说文》「減也」——减少、损失。","s「失收」取「收」：减而收。"),
("殞","yǔn",F,"《集韵》「歿也」——死亡、陨落。","y取锐：命殒而锐。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取玄／員支「幽深、圆转」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第458－459部（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡458a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡458a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡458a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))