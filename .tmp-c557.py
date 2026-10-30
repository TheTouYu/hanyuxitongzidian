import json,subprocess,os,glob
F="【450 叀部】惠支取「纺叀之短尖、细密、用心专一」诸面；軎支取「纺轮转动、缠线、相击」诸面。"
N="字形：古文字字形库未收。"
D=[("潓","huì",F,"《说文》「水，出廬江，入淮」——水名。","h「豁活」取「活」：水流而活。"),
("韢","suì",F,"《说文》「櫜紐也」——扎口袋的皮绳；一说盛敌人首级的口袋。","s「失收」取「收」：绳扎而收。"),
("繐","suì",F,"《说文》「細疏布也」——细而疏的麻布，古作丧服；亦指穗状饰物。","s取收：布疏而收。"),
("鏸","huì",F,"《广韵》「銳也，又三隅矛」；suì 大鼎；ruì 侍臣所执兵。","h取活：兵锐而活。"),
("憓","huì",F,"《玉篇》「愛也、羡也」；《集韵》「怒也」——爱羡，亦怒。","h取活：心爱而活。"),
("譓","huì",F,"《集韵》「辨察也」；《广韵》「多謀智曰譓，又順也」——明察多谋。","h取活：言察而活。"),
("𦒎","huì",F,"《集韵》「翮末」——《玉篇》「六翮之末」：鸟翅羽茎的末端。","h取活：羽末而活。"),
("嘒","huì",F,"《说文》「小聲也」——《诗》「嘒彼小星」：细小之声、微明。","h取活：声小而活。"),
("蕙","huì",F,"《玉篇》「香草，生下濕地」——一干数花而香不足者蕙，古以避疫。","h取活：草香而活。"),
("軎","wèi",F,"从口从叀：象纺轮之形，亦象拈纱时纺轮转动的细索之声。","w「勿问」取「问」：轮转而问。"),
("轡","pèi",F,"《说文》「馬轡也，从絲从軎」——《诗》「六轡如絲」：驾驭牲口的缰绳。","p「拼辟」取「拼」：绳并而拼。"),
("繫","xì",F,"《玉篇》「子孫相繋也，与系同」——联属、拴缚。","x「续消」取「续」：绳续而续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取叀部「短尖／细密／轮转」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbs-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第450部「叀部」（卷七十五 叀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡450c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡450c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡450c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))