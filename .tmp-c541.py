import json,subprocess,os,glob
F="【439 㡀部】敝＝破布；诸字取「憋住、破败」一面。"
F2="【440 必部】必＝甲骨文同「弋」（系丝可回收之箭），金文加八声；如墨绳取直之器，引申标准、肯定、专一、谜藏（祕）。"
N="字形：古文字字形库未收。"
D=[("憋","biē",F,"《方言》「恶也」；《广韵》「急性貌、怒也」——性急而勉强忍住。","b「闭剥」取「剥」：气憋而分。"),
("彆","biè",F,"《集韵》「弓戾谓之㢼，或作彆」——弓两端外弯处；今彆扭、强忍。","b取剥：弓张而分。"),
("𩋇","bì",F,"《集韵》「刀削饰，或作珌」——刀鞘末端装饰。","b取剥：饰分而缀。"),
("𡘴","biē",F,"《玉篇》「大也」；《集韵》「巨力也」——大力。","b取剥：力分而巨。"),
("𡐞","biē",F,"《仓颉篇》「大阜，在左冯翊池阳县北」；泥𡐞。","b取剥：土阜而分。"),
("必","bì",F2,"甲骨文同弋，金文加八声；如丝浸墨取直之器，引申标准、必定、专一、隐祕。","b「闭剥」取「剥」：绳分而直。"),
("泌","bì",F2,"《说文》「侠流也，从水必声」——从狭处急流；又液体由细孔排出。","b取剥：水泌而分。"),
("䏟","bié",F2,"《说文》「肥肉也，从肉必声」——肥得沁油。","b取剥：脂泌而分。"),
("苾","bì",F2,"《说文》「馨香也，从艸必声」——芳香；苾刍，西域草名。","b取剥：香泌而散。"),
("飶","bì",F2,"《说文》「食之香也，从食必声」——食物香气。","b取剥：香泌而溢。"),
("邲","bì",F2,"《说文》「晋邑也」——晋楚战于邲，今河南荥阳北。","b取剥：地名借声。"),
("䩛","bì",F2,"《说文》「车束也，从革必声」——车上皮革捆扎处；又通辔。","b取剥：束而分。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取本部「憋破／墨绳取直」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbo-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第439－440部（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡440a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡440a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡440a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))