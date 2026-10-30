import json,subprocess,os,glob
F="【451 回部】旬支余字取「周遍、信实、山玉」诸面；訇支取「大声轰响、周遍震动」之面。"
N="字形：古文字字形库未收。"
D=[("恂","xún",F,"《说文》「信心也，从心旬聲」——《论语》「恂恂如也」：信实恭顺；亦恐惧。","x「续消」取「续」：心信而续。"),
("㰬","xún",F,"《集韵》「气也」——气息周流。","x取续：气周而续。"),
("峋","xún",F,"《集韵》「嶙峋，山厓重深皃」——山石层叠深峻。","x取续：山层而续。"),
("郇","xún",F,"《说文》「周武王子所封國，在晉地」——古国名（今山西临猗）。","x取续：地名借声。"),
("珣","xún",F,"《说文》「醫無閭珣玗琪，《周書》所謂夷玉」——美玉名。","x取续：玉润而续。"),
("筍","sǔn",F,"《说文》「竹胎也，从竹旬聲」——竹笋，旬日而长。","s「失收」取「收」：笋生而收。"),
("殉","xùn",F,"《说文》「用人從葬也」——以人从葬；引申为道义献身。","x取续：从死而续。"),
("徇","xùn",F,"《说文》「行示也」——巡行示众；引申曲从、营求。","x取续：行示而续。"),
("訇","hōng",F,"《说文》「騃言聲」；《广韵》「匉訇，大聲」——大声轰响，周遍震动。","h「豁活」取「活」：声响而活。"),
("渹","hōng",F,"《集韵》「水石聲」——水激石之声。","h取活：水响而活。"),
("輷","hōng",F,"《集韵》「車聲」——车行轰响。","h取活：车响而活。"),
("鍧","hōng",F,"《集韵》「鏗鍧，鐘鼓聲相雜」——钟鼓相杂之声。","h取活：钟响而活。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取旬／訇支「周遍、轰响」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbl-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第451部「回部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡451f2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡451f.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡451f.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))