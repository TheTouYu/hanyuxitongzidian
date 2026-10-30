import json,subprocess,os,glob
F="【461 川部→462 鮮部】川支取「贯穿、顺流」诸面；462 鮮部＝从魚从羴省，鲜鱼之味，引申新鲜、鲜明、少。"
N="字形：古文字字形库未收。"
D=[("圳","zhèn",F,"《集韵》「溝也」——田间水沟；粤语「圳」即水沟。","zh「凿总」取「总」：沟聚而总。"),
("釧","chuàn",F,"《集韵》「釧，臂環也」——手镯，取贯穿腕上。","ch「刺持」取「持」：环贯而持。"),
("訓","xùn",F,"《说文》「說教也，从言川聲」——以言疏导，如川之贯穿。","x「续消」取「续」：教续而消。"),
("馴","xùn",F,"《说文》「馬順也，从馬川聲」——马顺从人意。","x取续：马顺而续。"),
("紃","xún",F,"《说文》「圜采也」——圆形绦带、饰绳。","x取续：绳圆而续。"),
("汌","chuàn",F,"《集韵》「水名」——水名。","ch取持：水贯而持。"),
("鮮","xiān",F,"《说文》「魚名，出貉國」——鲜鱼；引申新鲜、鲜明、鲜少。","x取续：鱼鲜而续。"),
("鱻","xiān",F,"三鱼为鱻——新鲜之极，同「鮮」。","x取续：鱼多而续。"),
("尟","xiǎn",F,"《说文》「是少也」——少，同「鮮少」之鲜。","x取续：少而续。"),
("癬","xuǎn",F,"《集韵》「乾瘍也」——癣，皮肤干痒如鱼鳞。","x取续：皮癣而续。"),
("蘚","xiǎn",F,"《集韵》「苔蘚也」——苔藓，贴石而生如鱼鳞。","x取续：苔贴而续。"),
("燹","xiǎn",F,"《玉篇》「野火也」——野火焚烧。","x取续：火延而续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取川／鮮支「贯穿、鲜少」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lba-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第461－462部（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡461a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡461a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡461a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))