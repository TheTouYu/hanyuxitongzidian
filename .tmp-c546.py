import json,subprocess,os,glob
F="【440 玨部】玨（jué）＝从玉二叠，象意玉串（二叠表多，可合可分），本义「二玉相合为一玨」。轉義：分瑞玉为信→班（分列、班次、分给）；玉色驳杂→斑（驳文、色杂、白发）。音源：借音，义音同「分」。"
N="字形：古文字字形库未收（原稿引玉虎符图）。"
D=[("玨","jué",F,"《说文》「二玉相合為一玨」——双玉为信；亦作瑴。","j「聚决」取「决」：双玉分合。"),
("班","bān",F,"《说文》「分瑞玉，从玨从刀」——以刀分瑞玉，各持为凭；引申分列、班次、分给、回返。","b「闭剥」取「剥」：玉分而别。"),
("𨌥","fú",F,"《说文》「車笭間皮篋，古者使奉玉以藏之」——车栏皮匣，装玉亦装弓矢。","f「附分」取「附」：匣附车而分。"),
("𢴬","bàn",F,"《集韵》「絆也，引擊也」——牵绊、击打。","b取剥：牵分而击。"),
("斑","bān",F,"《集韵》「辬，駁文也，或作斑」；《韻會》「雜色曰斑」——色驳杂。","b取剥：色驳而分。"),
("癍","bān",F,"《汉典》「皮膚上生的斑點」——皮肤斑点。","b取剥：点散而分。"),
("𤡰","bān",F,"《集韵》「逋還切，音班，獸名」——兽名。","b取剥：兽分而走。"),
("𩔮","bān",F,"《搜眞玉鏡》「音班」，疑同「頒」——头半白；颁，大头。","b取剥：发白而分。"),
("𪄕","bān",F,"《汉典》「斑鳩」——羽色斑驳之鸟。","b取剥：羽斑而分。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取玨部「玉之分合／色驳」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbt-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第440部「玨部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡440c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡440c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡440c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))