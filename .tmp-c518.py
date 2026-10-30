import json,subprocess,os,glob
F="【429 立部】立＝从大从一，大象人跨立、一为地面，象事指人站立、到临、占据某处不动；《说文》「住也」。转义：站不久→即刻、马上；占据→存在、成就；又通粒、位。音源：借音字，义音同「异」（翼/翌），立如握笔亦通「聿」。字族两支：①站立竖起②颗粒摧折。"
N="字形：古文字字形库未收。"
D=[("立","lì","人跨立地面，站立、到临、占据；引申即刻、成、粒、位。","l「拢离」取「离」：足离地而立。"),
("笠","lì","《说文》「簦无柄也」——斗笠；南宋李迪《风雨牧归图》中即此。","l取离：笠覆而离雨。"),
("位","wèi","《说文》「列中庭之左右谓之位」——人立之处、位置；《篇海》古「位」字从立。","w「零声母」从立取位：人所立处。"),
("鴗","lì","《说文》「天狗也」——翠鸟，又名山鴗、鱼狗、叼鱼郎，喙极长而尾短。","l取离：立枝待鱼。"),
("颯","sà","《说文》「翔风也」——回旋之风。","s「失收」取「收」：风回而收。"),
("蒞","lì","《韵会》「临也」——到、临视。","l取离：亲临而至。"),
("鉝","lì","《集韵》「食器」，林邑王献流离苏鉝——古扶南国食器。","l取离：器立而盛。"),
("岦","lì","《广韵》「岦岌，山貌」——山势高立。","l取离：山立而拔。"),
("菈","lā","《方言》东鲁呼芦菔（萝卜）为菈𦾽子——块茎常长出地表，故从立。","l取离：块茎离土。"),
("苙","lì","《方言》「苙，圂也」——垫猪栏的草（已脱粒秸秆）；又白芷、白及。","l取离：草离穗而垫。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取立部「人／物直立不动」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lb-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第429部「立部」（卷七十一 聿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡429a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡429a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡429a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))