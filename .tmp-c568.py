import json,subprocess,os,glob
F="【452 全部】全＝纯玉完具（从入从工），引申完备、纯色；诸字取「纯全、衡量、完聚」诸面。"
N="字形：古文字字形库未收。"
D=[("牷","quán",F,"《说文》「牛純色」——祭祀用的纯色全牛。","q「亲缺」取「缺」：纯而补缺。"),
("荃","quán",F,"《说文》「芥𦷵也」；《庄子》「得魚忘荃」——香草，亦通「筌」。","q取缺：草全而缺。"),
("詮","quán",F,"《说文》「具也，从言全聲」——详尽解释、具列其义。","q取缺：言全而缺。"),
("銓","quán",F,"《说文》「衡也，从金全聲」——衡量轻重、铨选人才。","q取缺：衡全而缺。"),
("跧","quán",F,"《集韵》「跧伏，蜷曲也」——蜷伏在地。","q取缺：足蜷而缺。"),
("佺","quán",F,"《说文》「偓佺，仙人也」——仙人名。","q取缺：仙全而缺。"),
("栓","shuān",F,"《集韵》「木釘也」——木钉、门栓，取全木一段。","sh「失收」取「收」：木栓而收。"),
("拴","shuān",F,"《集韵》「揀也」；俗「繫也」——用绳系住。","sh取收：绳系而收。"),
("洤","quán",F,"《集韵》「水名」——水名。","q取缺：水全而缺。"),
("烇","quán",F,"《集韵》「火也」——火貌。","q取缺：火全而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取全部「纯全、完聚」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbh-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第452部「全部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡452b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡452b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡452b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))