import json,subprocess,os,glob
F="【437 八部·分部】分＝从刀八声，剖开；字族取分散、香气分布、众多诸面。"
N="字形：古文字字形库未收。"
D=[("汾","fén",F,"《说文》「水，出太原晋阳山，西南入河」——汾河，山西第一大河。","f「附分」取「分」：水分为派。"),
("鳻","fén",F,"《说文》「鸟聚貌，一曰飞貌」——鸟群聚飞。","f取分：鸟散而聚。"),
("梤","fén",F,"《说文》「香木也」——香树。","f取分：香分而散。"),
("衯","fēn",F,"《说文》「长衣貌」——长衣，俗言披风。","f取分：衣长而分。"),
("黺","fěn",F,"《说文》「画粉也」——衮衣上山龙华虫之纹；或指绘画的粉。","f取分：粉分而绘。"),
("扮","fěn",F,"《说文》「握也，读若粉」——握持、鼓动；又打扮。","f取分：握而分。"),
("盆","pén",F,"《说文》「盎也，从皿分声」——盛物洗涤的圆口大底小器。","p「拼辟」取「辟」：器分而容。"),
("邠","bīn",F,"《说文》「周太王国，在右扶风美阳」——同豳，周先祖公刘所居。","b「闭剥」取「剥」：地名借声。"),
("釁","xìn",F,"《说文》「血祭也，象祭灶」——以牲血涂器祭祀；引申缝隙、松动、罪、兆。","x「续消」取「消」：血涂而消。"),
("芬","fēn",F,"《说文》「草初生，其香分布」——花草香气；又和也。","f取分：香分布。"),
("吩","fēn",F,"《集韵》「喷，吒也」；今吩咐，反复叮嘱。","f取分：语分而嘱。"),
("翂","fēn",F,"《集韵》「翂翂，飞也」——鸟飞之貌。","f取分：羽分而飞。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取分部「分散／剖开」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbi-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第437部「八部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡437d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡437d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡437d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))