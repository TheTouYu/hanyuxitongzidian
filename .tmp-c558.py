import json,subprocess,os,glob
F="【450 叀部】毄支取「纺车转动相击、缠结、坚硬」诸面。"
N="字形：古文字字形库未收。"
D=[("毄","jī",F,"《说文》「相擊中也，从車从攴」——车辖相碰；本义纺叀缠线时相击之声。","j「聚决」取「聚」：击而聚。"),
("轚","jí",F,"《说文》「車轄相擊也，从車毄聲」——《周礼》「舟輿擊互者」，路窄车船相碰。","j取聚：车碰而聚。"),
("擊","jī",F,"《说文》「攴也，从手毄聲」——攻打、碰撞。","j取聚：手击而聚。"),
("礊","kè",F,"《说文》「堅也，从石毄聲」——坚硬；huò 鞭声。","k「口控」取「控」：石坚而控。"),
("蟿","qì",F,"《集韵》「蟲名，似𧌻蝑細長」——蝗类，善弹腿跳跃，故有击打义。","q「亲缺」取「缺」：虫跳而缺。"),
("罊","qì",F,"《说文》「器中盡也，从缶毄聲」——器中空尽。","q取缺：器空而缺。"),
("墼","jī",F,"《说文》「瓴適也，一曰未燒也」——砖坯、土砖。","j取聚：土聚而击。"),
("𤪢","lì",F,"《说文》「玉也，从玉毄聲，讀若鬲」——玉名；疑「瑴」之讹。","l「拢离」取「离」：玉碎而离。"),
("𣤢","xì",F,"《说文》「且唾聲，一曰小笑」——唾声、轻笑；疑「嗀」之异体。","x「续消」取「消」：气出而消。"),
("檕","jì",F,"《说文》「繘耑木也，从木毄聲」——汲水绳端的木辘轳。","j取聚：木转而聚。"),
("蘻","jì",F,"《说文》「狗毒也，从艸毄聲」——狗毒草（有毒之草）。","j取聚：草毒而聚。"),
("𣫦","xì",F,"《玉篇》「子孫相繋也」——同「系」，联属不绝。","x取续：系续而消。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取叀部「轮转相击、缠结坚硬」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbr-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第450部「叀部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡450d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡450d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡450d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))