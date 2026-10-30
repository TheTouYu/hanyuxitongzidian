import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第512部「囧部」】囧＝甲骨文象心臟截面形（內曲線為心室瓣膜），金文象剖開的兩塊心臟，本義剖開的心臟；音源為心跳聲，與「心」同源異體；轉義坦白、表明（《玉篇》「大明也、彰也」）。"
N="字形：古文字字形库未收。"
D=[("囧","jiǒng",F,"本部字根：象剖開的心臟，引申坦白、彰明；《說文》析為窗牖不確。","j「聚决」取「聚」：心聚而剖露。"),
("莔","méng",F,"从艸朙省聲：貝母（《說文》「貝母也」），鱗莖狀如心形，亦如貝如女陰。","m「蒙末」取「蒙」：蒙覆而生。"),
("𥭮","méng",F,"《集韻》「竹名，或作䈍」——竹之一種。","m取蒙末：蒙密之竹。"),
("㴄","yǐng",F,"《集韻》「水洄皃，或从景」——取心臟泵血之狀為意，水迴旋。","y「柔锐」取「柔」：水柔而洄。"),
("𢚊","xī",F,"《說文》「古文悉」——明瞭於心。","x「续消」取「续」：心續而明。"),
("朙","míng",F,"从囧从月：心明白如月照（《廣韻》「通也」）；或从日从月取明亮，从田从月取月光透窗。","m取蒙末：月照破蒙。"),
("萌","méng",F,"从艸明聲：艸芽初露（《說文》「艸芽也」），引申始生。","m取蒙末：芽破蒙而出。"),
("橗","méng",F,"《集韻》「木名」；《玉篇》「木心」——木之心。","m取蒙末：木心含蒙。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諸字：莔取貝母心形、㴄取水洄、萌取芽初露、橗取木心，皆承「心形／剖露而生」一面；只列本部谐声字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":512,"name":"囧"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lji-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第512部「囧部」（卷八十四 心）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡512a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡512a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡512a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))