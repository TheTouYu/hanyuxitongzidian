import json,subprocess,os,glob
F="【444 雈部】萈支雈聲字：取鹭之宽阔、曲颈、水草诸面。"
N="字形：古文字字形库未收。"
D=[("寬","kuān",F,"《说文》「屋寬大也，从宀萈聲」——房屋宽大；引申宽宏、舒缓、宽恕。","k「口控」取「控」：屋宽而控。"),
("髖","kuān",F,"《说文》「髀上也，从骨寬聲」——胯骨、髋部。","k取控：骨宽而控。"),
("鑧","kuān",F,"《集韻》「器名」——器名，疑即宽口器。","k取控：器宽而控。"),
("𦏊","quán",F,"《集韻》「羊名」——羊名。","q「亲缺」取「缺」：羊角而缺。"),
("𦆼","wǎn",F,"《集韻》「綰，或从萈」——系结、盘绕。","w「勿问」取「问」：丝结而问。"),
("𪈻","quán",F,"《玉篇》「𪈻鵒，亦鴝鵒也」——八哥鸟。","q取缺：鸟鸣而缺。"),
("𦒨","qí",F,"《集韻》「羽盛皃」——羽毛丰盛。","q取缺：羽张而缺。"),
("𡅻","huàn",F,"《集韻》「叫呼也」——呼叫。","h「豁活」取「活」：呼而活。"),
("𡚊","huān",F,"《集韻》「奢也」——奢侈。","h取活：奢而活。"),
("萈","huán",F,"《说文》「山羊細角者，从兔足，萈聲」——細角山羊（原稿字形析为萈声）。","h取活：羊角而活。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取雈部「宽阔／曲颈」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbz-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第444部「雈部」（卷七十四 雈）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡444c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡444c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡444c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))