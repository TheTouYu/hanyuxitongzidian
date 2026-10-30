import json,subprocess,os,glob
F="【444 雈部】雈＝苍鹭；诸字取鹭之「曲颈、水泽、玉火」诸面。"
N="字形：古文字字形库未收。"
D=[("壦","xūn",F,"《集韻》「塤，或从雚」——陶制吹奏乐器（埙）。","x「续消」取「消」：土器而消。"),
("𢑆","quán",F,"《说文》「弓曲也，从弓雚聲」——弓弯曲。","q「亲缺」取「缺」：弓曲而缺。"),
("䠰","quán",F,"《廣韻》「曲脊行也」——驼背而行。","q取缺：脊曲而缺。"),
("顴","quán",F,"《集韻》「輔骨曰顴」——颧骨，面颊突起如鹭喙。","q取缺：骨突而缺。"),
("巏","quán",F,"《集韻》「巏嵍，山名」——山名。","q取缺：山高而缺。"),
("䑏","quán",F,"《集韻》「䑏，肥也」——肥貌。","q取缺：肉丰而缺。"),
("瓘","guàn",F,"《说文》「玉也，从玉雚聲」——玉名。","g「隔估」取「隔」：玉润而隔。"),
("䚭","xuān",F,"《集韻》「角皃」——角貌。","x取消：角分而消。"),
("𤼐","huàn",F,"《集韻》「病也」——病名。","h「豁活」取「活」：病而活。"),
("酄","huān",F,"《说文》「魯下邑，从邑雚聲」——在今山东肥城西。","h取活：地名借声。"),
("𦼉","huán",F,"《说文》「薍也，从艸萑聲」——初生之荻，细苇。","h取活：苇生而活。"),
("䟒","quán",F,"《集韻》「行曲也」——行走弯绕。","q取缺：行曲而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取雈部「曲颈／水泽」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lby-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第444部「雈部」（卷七十四 雈）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡444b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡444b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡444b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))