import json,subprocess,os,glob
F="【451 回部】匀支＝均分周遍；軍支＝战车回环绕营；诸字取「均、转、围」诸面。"
N="字形：古文字字形库未收。"
D=[("匀","yún",F,"《说文》「少也，从勹二」——本指均分、调匀，周而复始。","y「柔锐」取「锐」：分均而锐。"),
("韵","yùn",F,"《说文》新附「和也，从音勻聲」——声音和谐、气韵。","y取锐：音和而锐。"),
("筠","yún",F,"《说文》「竹皮也，从竹均聲」——竹青皮；亦竹子。","y取锐：竹皮而锐。"),
("畇","yún",F,"《说文》「田，川也」——《诗》「畇畇原隰」：田地均整。","y取锐：田均而锐。"),
("均","jūn",F,"《说文》「平，徧也，从土从勻，勻亦聲」——土地均平、周遍。","j「聚决」取「聚」：土聚而均。"),
("鈞","jūn",F,"《说文》「三十斤也，从金勻聲」——均分重量之准；引申权衡、均等。","j取聚：金均而聚。"),
("軍","jūn",F,"《说文》「圜圍也，四千人為軍，从車从包省」——战车回环绕营，故包围、驻军。","j取聚：车围而聚。"),
("葷","hūn",F,"《说文》「臭菜也，从艸軍聲」——气味辛臭之菜（葱蒜韭），引申荤腥。","h「豁活」取「活」：气臭而活。"),
("渾","hún",F,"《说文》「混流聲也」——水势回旋浑厚；引申浑浊、浑全。","h取活：水浑而活。"),
("運","yùn",F,"《说文》「迻徙也，从辵軍聲」——军旅回环行进，引申运行、转运、命运。","y取锐：行转而行。"),
("輝","huī",F,"《说文》「光也，从火軍聲」——火光周遍照耀。","h取活：光周而活。"),
("揮","huī",F,"《说文》「奮也，从手軍聲」——振臂挥动，取回旋之势。","h取活：手挥而活。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取匀／軍支「均分、回环绕围」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbk-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第451部「回部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡451g2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡451g.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡451g.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))