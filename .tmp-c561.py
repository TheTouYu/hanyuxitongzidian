import json,subprocess,os,glob
F="【451 回部】回部余支与𠬸支：取「回绕、入水取物而没」诸面。"
N="字形：古文字字形库未收。"
D=[("𢙍","xī",F,"《五音集韵》「同悉」——《说文》古文「悉」之讹。","x「续消」取「消」：尽而消。"),
("𩢱","huí",F,"《玉篇》「馬名」；《正字通》疑「駟」之讹。","h「豁活」取「活」：马驰而活。"),
("𣑩","yīn",F,"《植物名实图考》「𣑩樹」——木质坚重，造船者取以为舵。","y「柔锐」取「锐」：木坚而锐。"),
("𥔯","huì",F,"《集韵》「石皃」——石貌，取回屈之状。","h取活：石结而活。"),
("𦂆","huì",F,"《类篇》「衣領緣皃」——衣领缘边之貌。","h取活：缘绕而活。"),
("𪀟","huí",F,"《玉篇》「鳥長一尺，五色文」——五色文鸟。","h取活：鸟彩而活。"),
("𠬸","mò",F,"《说文》「入水有所取也，从又在回下」——手入回水之中取物，即「没」之初文。","m「蒙末」取「末」：入水而末。"),
("沒","mò",F,"《说文》「湛也，从水𠬸聲」——沉没水中；引申终尽、隐没。","m取末：沉水而末。"),
("殁","mò",F,"《玉篇》「死也」——终没、死亡，与「沒」通。","m取末：命终而末。"),
("圽","mò",F,"《集韵》「埋也」——埋没于土。","m取末：土埋而末。"),
("莈","mò",F,"《集韵》「草名」——草名，取没入草丛之状。","m取末：草没而末。"),
("𩑦","mò",F,"《集韵》「頭前也」——头向前俯入水之状。","m取末：头没而末。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取回部「回绕／入水而没」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbo-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第451部「回部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡451c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡451c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡451c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))