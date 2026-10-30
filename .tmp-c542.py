import json,subprocess,os,glob
F="【440 必部】必＝丝浸墨取直之器；诸字取「取直、专一、封闭、隐密」诸面。"
N="字形：古文字字形库未收。"
D=[("瑟","sè",F,"《说文》「庖牺所作弦乐也」——弦乐；引「瑟缩」「瑟琴」。","s「失收」取「失」：弦散而收。"),
("珌","bì",F,"《说文》「佩刀下饰，天子以玉」——刀鞘末端玉饰。","b「闭剥」取「剥」：饰缀而分。"),
("閟","bì",F,"《说文》「闭门也」——闭门深藏；幽闭、谨慎。","b取剥：门闭而分。"),
("柲","bì",F,"《说文》「欑也」——兵器的柄；引申弓檠。","b取剥：柄分而直。"),
("密","mì",F,"《说文》「山如堂者」——山形如堂屋；引申稠密、秘密、亲密。","m「蒙末」取「蒙」：覆盖而密。"),
("蜜","mì",F,"《说文》「蠭甘飴也」——蜂酿甜饴。","m取蒙：黏甜而覆。"),
("謐","mì",F,"《说文》「静语也」——安静。","m取蒙：语静而覆。"),
("颒","huì",F,"《说文》「洒面也」——洗面。","h「豁活」取「活」：水洒而活。"),
("鴓","mì",F,"《玉篇》「鸟如鹊」——《集韵》鴓鸔，鸟名。","m取蒙：羽覆而飞。"),
("蔤","mì",F,"《说文》「芙蕖本」——荷花地下茎（藕）。","m取蒙：节藏泥中。"),
("宓","mì",F,"《说文》「安也」——安宁；伏羲亦作宓羲，借为「伏」。","m取蒙：安伏而覆。"),
("汨","mì",F,"《说文》「长沙汨罗渊也」——水名，屈原所沉；又汩没。","m取蒙：水没而覆。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取必部「取直／隐密」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbp-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第440部「必部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡440b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡440b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡440b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))