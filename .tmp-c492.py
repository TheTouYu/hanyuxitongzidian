import json,subprocess,os,glob
B="【419 犮部】犮与亥同源，金文象直立的旱獭正面形、足加一丿表示抬起前肢；转义：直立→挺拔抽引、往前扑、毛皮宜作蔽膝、掘根致沙化→旱灾、毛发、腿肉。音源：源自旱獭叫声。"
N="字形：古文字字形库未收。"
D=[("炦","bá","《说文》「火气也」——柴薪已尽、火将熄，以手拨治，惟稍存火气。","b「闭剥」取「剥」：拨火而存气。"),
("馛","bó","《玉篇》「大香」——香气浓烈。","b「闭剥」取「剥」：香剥而烈。"),
("䣮","pò","《广韵》「酒气」——酒的气味。","p「拼辟」取「辟」：气辟而散。"),
("𢘀","pèi","《广雅》「怒也」——愤怒。","p「拼辟」取「辟」：气辟而怒。"),
("𣧧","bó","《集韵》「腐气」。","b「闭剥」取「剥」：腐败之气。"),
("颰","bá","《集韵》「小风谓之颰，一曰疾风」——疑指龙卷风。","b「闭剥」取「剥」：风剥地而起。"),
("𤝜","fèi","《说文》「犬鸣也」——犬吠；或作犻、𤝜。","f「附分」取「分」：声分而吠。"),
("𦍱","gāo","《五音篇海》「音羔」——羊羔。","g「隔估」取「隔」：羔隔母而鸣。"),
("𧲯","bō","《玉篇》「豸」——长脊兽。","b「闭剥」取「剥」：豸剥而走。"),
("𩂔","fú","《集韵》「雨貌」。","f「附分」取「分」：雨分而落。"),
("𩠷","fú","《玉篇》「妇人首饰也」。","f「附分」取「分」：饰分而戴。"),
("𩃶","bó","《广韵》「云气」；《集韵》「云貌」。","b「闭剥」取「剥」：云剥而布。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":B,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取犮部「旱獭气息／皮毛」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）","statement":f"{ch}（{p}）：{xp}",
"boundary":"源自《系統漢語》第419部「犮部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡419d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡419d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡419d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))