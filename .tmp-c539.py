import json,subprocess,os,glob
F="【439 㡀部】㡀（bì）＝从巾从八，一幅布狭小而破败，为「敝」之初文；引申小、破旧、屏障、昏暗。"
N="字形：古文字字形库未收。"
D=[("敝","bì",F,"《说文》「帗也，一曰败衣」——一幅巾、破衣；引申坏、败、尽、仆倒。","b「闭剥」取「剥」：布裂而剥。"),
("鷩","biē",F,"《说文》「赤雉也」——锦鸡，长尾如破巾；性急憋，不可生服。","b取剥：羽散而剥。"),
("嫳","piè",F,"《说文》「易使怒也，从女敝声」——易发脾气；轻薄之貌。","p「拼辟」取「辟」：性急而分。"),
("獙","bì",F,"《山海经》「状如狐而有翼，音如鸿雁」——獙獙，有翅怪兽。","b取剥：翼分而飞。"),
("徶","bié",F,"《集韵》「徶㣯，衣服婆娑貌」——衣袂飘动。","b取剥：衣散而分。"),
("䭱","bié",F,"《集韵》「香也」；《玉篇》「小香」——香气。","b取剥：香细而分。"),
("𩓝","bié",F,"《玉篇》「𩓝䫔，短貌」——身材矮小。","b取剥：形短而分。"),
("䘷","biē",F,"《玉篇》「袂也、敝衣也」——衣袖；破衣。","b取剥：衣破而分。"),
("䌘","biè",F,"《玉篇》「编绳也，剑带也」——棕绳、剑带。","b取剥：绳编而分。"),
("虌","biē",F,"《广韵》「蕨菜」——蕨。","b取剥：蕨拳而分。"),
("䳤","biē",F,"《玉篇》「䳤𩿧，鸟」；《广韵》「鸺鹠」——小鸟名。","b取剥：羽分而飞。"),
("暼","piē",F,"《集韵》「暼暼，日落势也」——日落之状。","p取辟：光散而分。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取㡀部「破布／狭小」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbm-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第439部「㡀部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡439a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡439a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡439a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))