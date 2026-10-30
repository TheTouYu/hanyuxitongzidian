import json,subprocess,os,glob
F="【438 半部】半＝从牛八声，宰牲剖分（判之初文）；字族取「大块、拌和、两半、边界」诸面。"
N="字形：古文字字形库未收。"
D=[("絆","bàn",F,"《说文》「马絷也，从糸半声」——绊马足的绳索；《释名》「半也，拘使半行不得自纵」。","b「闭剥」取「剥」：绳分而拘。"),
("拌","pān",F,"《玉篇》「弃也」——舍弃不顾；又分剖、搅拌（bàn）。","p「拼辟」取「辟」：弃而分。"),
("秚","bàn",F,"《集韵》「物之相和，通作伴」——物相和合。","b取剥：和而分。"),
("靽","bàn",F,"《集韵》「驾牛具，在后曰靽」——套在牲口后部的皮带。","b取剥：套而分。"),
("跘","pán",F,"《集韵》「蹒跚，跛行貌」；又交足坐、跌倒。","p取辟：步分而跛。"),
("䉽","bǎn",F,"《集韵》「屑米饼也」——米粉饼（粄）。","b取剥：米碎而分。"),
("胖","pàn",F,"《说文》「半体肉也，一曰广肉，从半从肉」——从脊柱分开的全牲；又夹脊肉。","p取辟：肉分而半。"),
("坢","pǎn",F,"《集韵》「平坦也」；又尘埃、堤防；粪肥。","p取辟：土分而平。"),
("衅","xìn",F,"《玉篇》「牲血涂器祭也，亦作釁」——血祭；又缝隙、松动、罪兆。","x「续消」取「消」：血涂而消。"),
("袢","fàn",F,"《说文》「无色也，从衣半声」——白色细葛夏衣；袢延，衣热。","f「附分」取「分」：衣薄而分。"),
("姅","bàn",F,"《说文》「妇人污也」——月经、分娩、流产见血。","b取剥：血分而下。"),
("判","pàn",F,"《说文》「分也，从刀半声」——分开、剖分；又断、分辨。","p取辟：刀分而判。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取半部「剖分／两半」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbk-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第438部「半部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡438b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡438b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡438b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))