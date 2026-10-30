import json,subprocess,os,glob
F="【450 叀部】叀＝纺专拈线；转注诸字取「拈合、旋转、成团、专一」诸面。"
N="字形：古文字字形库未收。"
D=[("傳","chuán",F,"《说文》「遽也，从人專聲」——驿传、传递；zhuàn 传记。纺线相续，故传。","ch「刺持」取「持」：线续而持。"),
("轉","zhuǎn",F,"《玉篇》「迴也、轉運也」——纺轮旋转，引申转运、转变。","zh「凿总」取「总」：轮转而总。"),
("團","tuán",F,"《玉篇》「團圓也」——纱线绕成团，引申团聚、圆形。","t「涂突」取「突」：线团而突。"),
("摶","tuán",F,"《说文》「圜也，从手專聲」——把散物捏聚成团。","t取突：手抟而突。"),
("磚","zhuān",F,"《集韵》「甎，或作磚」——黏土抟成方坯烧硬，如线之拈合成块。","zh取总：土聚而总。"),
("膞","zhuān",F,"《说文》「切肉也」；《集韵》「腓腸也」——切肉成块，形圆。","zh取总：肉聚而总。"),
("鱄","zhuān",F,"《说文》「魚也，从魚專聲」——《吕氏春秋》「魚之美者，洞庭之鱄」。","zh取总：鱼圆而总。"),
("縳","zhuàn",F,"《说文》「白鮮色也，从糸專聲」；《集韵》「束也」——束缚。","zh取总：丝束而总。"),
("剸","tuán",F,"《说文》「切也，从刀專聲」——切断、割。","t取突：刀断而突。"),
("惠","huì",F,"《说文》「仁也，从心从叀」——徐锴「爲惠者，心專也」：用心专一，引申恩惠、柔顺。","h「豁活」取「活」：心专而活。"),
("蟪","huì",F,"《说文》新附「蟪蛄，蟬也」——小青紫蝉，吻长身短，取叀之短尖。","h取活：虫短而活。"),
("橞","huì",F,"《说文》「木也，从木惠聲」；《广韵》「小棺」——木名，亦小棺。","h取活：木小而活。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取叀部「拈合／旋转／成团」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbt-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第450部「叀部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡450b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡450b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡450b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))