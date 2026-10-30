import json,subprocess,os,glob
F="【453 丸部】丸＝圆转之形（《说文》「圜也，傾側而轉者，从反仄」），象小圆物、球丸。"
N="字形：古文字字形库未收。"
D=[("丸","wán",F,"《说文》「圜也，傾側而轉者，从反仄」——小而圆、可转之物。","w「勿问」取「问」：圆转而问。"),
("紈","wán",F,"《说文》「素也，从糸丸聲」——细白绢，取圆润洁白。","w取问：绢润而问。"),
("芄","wán",F,"《说文》「芄蘭，莞也」——《诗》「芄蘭之支」：蔓生草。","w取问：草蔓而问。"),
("汍","wán",F,"《集韵》「汍瀾，泣也」——泪流圆转。","w取问：泪转而问。"),
("肒","huán",F,"《集韵》「疹也」——皮肤肿起如水泡圆。","h「豁活」取「活」：泡起而活。"),
("忨","wàn",F,"《说文》「貪也，从心元聲」——贪求。","w取问：心贪而问。"),
("玩","wán",F,"《说文》「弄也，从玉元聲」——把弄玉器，引申玩赏、戏弄。","w取问：玉弄而问。"),
("翫","wán",F,"「玩」的异体，从羽——习玩、轻慢。","w取问：羽玩而问。"),
("刓","wán",F,"《说文》「剓也」——刻削使圆。","w取问：刀削而问。"),
("岏","wán",F,"《集韵》「巑岏，山高銳皃」——山锐而圆。","w取问：山锐而问。"),
("园","yuán",F,"「園」的简化字：种蔬果树木、四周有篱的地方。","y「柔锐」取「锐」：园围而锐。"),
("元","yuán",F,"《说文》「始也，从一从兀」——人首为元，引申始、善、大。","y取锐：首出而锐。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取丸部「圆转」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbg-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第453－454部（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡453a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡453a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡453a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))