import json,subprocess,os,glob
F="【451 回部】軍支余字取「回旋、包围、晕转」诸面；云支取「云气回转、魂气周流」之面。"
N="字形：古文字字形库未收。"
D=[("皸","jūn",F,"《说文》「足坼也，从皮軍聲」——皮肤冻裂如军围之纹。","j「聚决」取「聚」：皮裂而聚。"),
("鼲","hún",F,"《说文》「鼠，出胡地，皮可作裘」——灰鼠，毛可制裘。","h「豁活」取「活」：鼠走而活。"),
("鶤","kūn",F,"《说文》「鳥，从鳥軍聲」——大鸡（鶤鸡），一说凤属。","k「口控」取「控」：鸟鸣而控。"),
("緷","gǔn",F,"《说文》「緯也」；《集韵》「束也」——纬线、捆束。","g「隔估」取「隔」：线束而隔。"),
("翬","huī",F,"《说文》「大飛也」——《诗》「如翬斯飛」：振翅疾飞，取回旋之势。","h取活：飞旋而活。"),
("諢","hùn",F,"《集韵》「弄言」——诙谐取笑之言。","h取活：言谐而活。"),
("暈","yùn",F,"《广韵》「日月傍氣」——日月周围光气回环；引申昏晕。","y「柔锐」取「锐」：气环而锐。"),
("餫","yùn",F,"《说文》「野饋曰餫」——运送军粮。","y取锐：粮运而锐。"),
("云","yún",F,"《说文》「山川氣也，从二，象回轉形」——云气回旋；借为「曰」。","y取锐：气转而锐。"),
("沄","yún",F,"《说文》「轉流也，从水云聲」——水流回转。","y取锐：水转而锐。"),
("魂","hún",F,"《说文》「陽气也，从鬼云聲」——阳气周流，离形而游。","h取活：气游而活。"),
("壇","tán",F,"《说文》「祭場也，从土亶聲」——筑土为台，环而祭之。","t「涂突」取「突」：土筑而突。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取軍／云支「回旋、周流」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbj-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第451部「回部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡451h2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡451h.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡451h.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))