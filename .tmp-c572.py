import json,subprocess,os,glob
F="【457 旋部】旋＝从㫃从疋，象人举旗回旋而行（《说文》「周旋，旌旗之指麾也」）；引申回旋、旋即。"
N="字形：古文字字形库未收。"
D=[("旋","xuán",F,"《说文》「周旋，旌旗之指麾也」——举旗回旋；引申旋转、旋即。","x「续消」取「续」：旋续而消。"),
("漩","xuán",F,"《集韵》「漩澴，水回皃」——漩涡，水回旋成涡。","x取续：水旋而续。"),
("璇","xuán",F,"《说文》「美玉也」——璇玑玉衡，北斗星名。","x取续：玉润而续。"),
("還","huán",F,"《说文》「復也，从辵睘聲」——返回、归还；hái 犹、更。","h「豁活」取「活」：回转而活。"),
("澴","huán",F,"《集韵》「水回旋也」——水势回环。","h取活：水回而活。"),
("鏇","xuàn",F,"《说文》「圜鑪也」——旋转的车床；《集韵》「温器」。","x取续：旋削而续。"),
("嫙","xuán",F,"《集韵》「好也」——美好，取回旋柔美之状。","x取续：美转而续。"),
("縼","xuàn",F,"《集韵》「繩也」——绳索，取缠绕回旋。","x取续：绳绕而续。"),
("玄","xuán",F,"《说文》「幽遠也，黑而有赤色者為玄」——幽深黑赤；引申玄妙。","x取续：幽深而续。"),
("弦","xián",F,"《说文》「弓弦也，从弓，象絲軫之形」——弓上之丝，取紧绷回弹。","x取续：弦张而续。"),
("舷","xián",F,"《集韵》「船邊也」——船的两侧，如弓之弦。","x取续：船边而续。"),
("泫","xuàn",F,"《说文》「湝流也」——《礼记》「其泣矣，其涕泫然」：泪流回旋。","x取续：泪流而续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取旋／玄支「回旋、幽深」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbd-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第457－458部（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡457a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡457a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡457a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))