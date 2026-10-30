import json,subprocess,os,glob
F="【434 釆部】釆（biàn）＝从乇（动物张开的指爪）从小（细颗粒），象意动物张爪翻找细物，或兽爪踩出的足印；引申反复筛选、辨别。"
N="字形：古文字字形库未收。"
D=[("釆","biàn",F,"部头字：从乇从小，翻找细物／兽爪足印，引申辨别（《说文》「辨别也，象兽指爪分别」）。","b「闭剥」取「剥」：爪扒而分。"),
("悉","xī",F,"《说文》「详尽也，从心从釆」——心里清楚、详尽。","x「续消」取「消」：尽而知之。"),
("宷","shěn",F,"《说文》「悉也，知宷谛也」——宀覆而釆别之，详审、熟究（即審）。","sh「失收」取「收」：覆而收别。"),
("蟋","xī",F,"蟋蟀——叫声小而嘈杂，如簸扬时的细响。","x取消：声细而消。"),
("僁","xiè",F,"《说文》「声也，读若㞕」——动草声、鸷鸟声、呻吟声。","x取消：声细而散。"),
("𦸝","xī",F,"牛膝，药草——苗高二三尺，叶如匙，有节似牛膝。","x取消：茎节而柔。"),
("㴽","xiè",F,"《玉篇》「瀎㴽，水流也」——水流之貌。","x取消：水疾而消。"),
("𣍸","pò",F,"《说文》「月始生，霸然也」——月始生微光，即霸（胐）之初形。","p「拼辟」取「辟」：月出而分。"),
("䊝","xiè",F,"《说文》「𥻦也，从米悉声」——米散；䊝𥻦双声，皆散意。","x取消：米散而消。"),
("窸","xī",F,"《集韵》「从穴出也」；窸窣，声不安。","x取消：细声不安。"),
("竊","qiè",F,"《说文》「盗自中出曰窃，从穴从米」——穿穴入而取米，引申私、浅、著。","q「亲缺」取「缺」：穴缺而入。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取釆部「翻扒／辨别」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lb7-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第434部「釆部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡434a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡434a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡434a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))