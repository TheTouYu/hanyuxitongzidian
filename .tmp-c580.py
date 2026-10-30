import json,subprocess,os,glob
F="【464 尤部】尤＝从「又」的指头部分加一，象事字，指多出一指（枝指），为「肬」之初文；转为特异、突出、过失、怨恨；音源仍同「又」；辩证：小篆讹为从乙，《说文》析形不确。"
N="字形：古文字字形库未收。"
D=[("尤","yóu",F,"本部部首字：六指（枝指）→特异→过失、怨恨；《玉篇》「過也、責也、多也、怨也」。","y「柔锐」取「锐」：枝指突出。"),
("优","yóu",F,"从人尤声——五谷精白如人发白；今为「優」之简化字，美好、特出。","y取锐：优而锐。"),
("魷","yóu",F,"从魚尤声——鱿鱼，有触须如手。","y取锐：须张而锐。"),
("沋","yóu",F,"从水尤声——沋河，渭河支流，出秦岭北麓。","y取锐：水出而锐。"),
("駀","yóu",F,"从馬尤声——马名；又训马行。","y取锐：马行而锐。"),
("紌","qiú",F,"从糸尤声——蜀锦之名，《蜀都赋》「紌繏𦃄䋶」。","q「亲缺」取「缺」：锦文而缺。"),
("㚭","yóu",F,"从女尤声——女字（人名用字）。","y取锐：借声记名。"),
("𦬓","yóu",F,"从艸尤声——草名，或作「𦸙」。","y取锐：草锐而锐。"),
("𨇳","cù",F,"从足尤声——《龙龛》「俗；蹙，正」，迫、急、近。","c「亲缺」取「亲」：迫而亲。"),
("𨑫","yóu",F,"从辵尤声——《集韵》「經過也」，俗「由」字。","y取锐：行过而锐。"),
("𩾵","jiù",F,"从鳥尤声——即「鷲」，大型猛禽，头颈裸出。","j「聚决」取「决」：猛禽决。"),
("𧌌","xiū",F,"从虫尤声——《玉篇》「蜘蛛也」，蜘蛛八足，多于昆虫。","x「续消」取「续」：蛛丝续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取尤部「多出、突出」一面，形符各定落点：人与魚馬取突出之状，水系、糸系取名物，足与辵取迫近。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbv-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第464部尤部（卷七十六 又）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡464a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡464a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡464a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))