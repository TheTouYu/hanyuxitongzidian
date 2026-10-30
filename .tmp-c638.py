import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FC="【第522部「刅部」】刅＝西周金文象枝葉對生之形（一般樹木枝葉交互，荊卻對生），為「荊」之初文；枝條柔韌有香，可編籃、作鞭→引申懲罰、創傷；音源義音同「良」（氣味如狼）。"
FJ="【第523部「㓝部」】㓝＝从井从刅，「井」象交叉紋路：或象用荊條編結器物（→創造），或象抽打之傷痕（→刑罰）；辯證「荊、刱、㓝、刑」本同源，《說文》析形不確。"
N="字形：古文字字形库未收。"
D=[("刅","chuāng",FC,"本部字根：荊枝對生，引申創傷。","ch「刺持」取「刺」：枝刺而傷。"),
("荊","jīng",FC,"从艸刑聲：楚木（《說文》），枝條柔韌可編、可作鞭，故古稱兩湖為荊。","j「聚决」取「聚」：枝聚而對生。"),
("創","chuàng",FC,"从刀倉聲：刅傷之分化，引申創造、開始。","ch取刺持：刀刺而創。"),
("梁","liáng",FC,"从木从水、刅聲：水橋（《說文》），以荊木連接架成；引申屋梁。","l「拢离」取「拢」：木攏為梁。"),
("粱","liáng",FC,"从米梁省聲：米名（《說文》），似粟而大（白粱、青粱）。","l取拢离：米粒攏聚。"),
("㓝","xíng",FJ,"本部字根：荊條編結或抽打，引申法度、刑罰。","x「续消」取「续」：編續成器。"),
("刑","xíng",FJ,"从刀幵聲：罰罪（《說文》），實為㓝之分化。","x取续消：罰而續。"),
("形","xíng",FJ,"从彡幵聲：象形、體貌（《說文》），取荊條編結之器形。","x取续消：器形而續。"),
("型","xíng",FJ,"从土刑聲：鑄器之法（《說文》），先用荊條編成器模。","x取续消：模續而成。"),
("硎","xíng",FJ,"从石刑聲：砥石、磨刀石（《集韻》）。","x取续消：石磨而續。"),
("銒","xíng",FJ,"从金幵聲：似鐘而頸長之盛羹器（《說文》），狀如荊條編簍。","x取续消：器長而續。"),
("郉","xíng",FJ,"从邑幵聲：周公所封，今河北邢臺（《說文》）。","x取续消：邑續而聚。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同卷兩部同源：刅支取「荊木成器／創傷」（刅／荊／創／梁／粱）、㓝支取「編結成器→創造」「抽打傷痕→刑罰」（㓝／刑／形／型／硎／銒／郉）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":522 if F0 is FC else 523,"name":"刅" if F0 is FC else "㓝"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lchuang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第522－523部（卷八十六 良）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡522a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡522a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡522a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))