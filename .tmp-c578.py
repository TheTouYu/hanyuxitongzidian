import json,subprocess,os,glob
F="【463 又部·余支】又有持肉、园囿、走摆诸面：囿以垣养禽兽而引申局限；賄为财货；姷、酭皆酬报相助；䞥、迶皆行走摆手之状。"
N="字形：古文字字形库未收。"
D=[("囿","yòu",F,"从囗有声——苑有垣、放养禽兽；引申区域、局限（囿于成见）。","y「柔锐」取「柔」：围而柔。"),
("蛕","huí",F,"从虫有声——《说文》「腹中長蟲也」，蛔虫。","h「豁活」取「活」：虫动而活。"),
("銪","yǒu",F,"金属元素铕（Eu）的译名用字，取「有」之音。","y取柔：借声记物。"),
("賄","huì",F,"从贝有声——《说文》「財也」，财物；引申贿赂。","h取活：财流而活。"),
("洧","wěi",F,"从水有声——古水名，今双洎河，颍水支流。","w「蒙末」取「末」：水末而流。"),
("絠","gǎi",F,"从糸有声——弓两端系弦处（弓弭），又训解绳。","g「隔估」取「隔」：弦隔而系。"),
("姷","yòu",F,"从女有声——《说文》「耦也」，相助；或从人作侑。","y取柔：相助而柔。"),
("酭","yòu",F,"从酉有声——《玉篇》「報也」，酬酒、回报，通「侑」。","y取柔：酬而柔。"),
("䞥","yòu",F,"从走有声——《说文》「走也」，走路时手的摆动。","y取柔：走摆而柔。"),
("迶","yòu",F,"从辵有声——《玉篇》「行」，行走。","y取柔：行而柔。"),
("戫","yù",F,"从戈有声——《玉篇》「有文章也」，同「彧」；又训疾貌。","y取柔：文而柔。"),
("䆜","yòu",F,"从穴有声——《玉篇》「空也」，空。","y取柔：空而柔。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取又部「持、围、走」诸面，形符各定落点：贝与酉主财与酬，走与辵主动，穴主空。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbx-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第463部又部（卷七十六 又）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡463c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡463c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡463c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))