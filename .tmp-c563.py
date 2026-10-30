import json,subprocess,os,glob
F="【451 回部】亘支余字取「宽大、光明、萦绕」诸面；旬支取「十日一周、回环周遍」诸面。"
N="字形：古文字字形库未收。"
D=[("喛","huàn",F,"《集韵》「哀也」——哀声回绕；同「唤」。","h「豁活」取「活」：哀呼而活。"),
("䚙","xuān",F,"《集韵》「角皃，一曰牛角」——牛角回曲。","x「续消」取「消」：角曲而消。"),
("𧻚","yuán",F,"《集韵》「走也」——行走回绕。","y「柔锐」取「锐」：行绕而锐。"),
("𡘍","gèn",F,"《集韵》「大也」——广大绵亘。","g「隔估」取「隔」：大而隔。"),
("蝖","xuān",F,"《集韵》「蟲名」——虫名，善盘旋。","x取续：虫旋而消。"),
("煊","xuān",F,"《集韵》「光明也」——火光盛大、光明温暖。","x取续：火盛而消。"),
("萱","xuān",F,"《说文》「藼，令人忘憂艸也」，或作萱——萱草（忘忧草）。","x取续：忘忧而消。"),
("揎","xuān",F,"《集韵》「手發衣也」——捋袖露手，取舒展之状。","x取续：袖展而消。"),
("旬","xún",F,"《说文》「徧也，十日為旬，从勹，日」——十日一周，周遍回环。","x取续：日周而消。"),
("詢","xún",F,"《说文》「謀也，从言旬聲」——咨询、问谋。","x取续：言周而消。"),
("荀","xún",F,"《说文》「艸也，从艸旬聲」；亦国名、姓。","x取续：草生而消。"),
("洵","xún",F,"《说文》「渦中水也，从水旬聲」——《诗》「洵美且都」：水旋；引申信实。","x取续：水旋而消。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取亘／旬支「回环周遍」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbm-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第451部「回部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡451e2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡451e.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡451e.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))