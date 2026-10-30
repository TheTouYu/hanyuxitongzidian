import json,subprocess,os,glob
F="【424 癹部】癹＝从癶从攴，象拄杖而立、双脚轮换踩踏，指中耕除草；也指用棍挑拨，此义分化作「發」。转义：发射→离去、派遣、生发、启动。音源：借音字，义音同「犮」。"
N="字形：古文字字形库未收。"
D=[("醱","pō","《集韵》「酘谓之醱」——酒再酿；又醱酵（发酵）。","p「拼辟」取「辟」：酒辟而再酿。"),
("𩯌","bō","《玉篇》「𩯌䰖，鬓多毛」——胡须怒张。","b「闭剥」取「剥」：须剥而张。"),
("𩞽","bó","同「餺」——餺饦，饼也。","b「闭剥」取「剥」：面剥而成饼。"),
("蕟","fà","《集韵》「草名」；又粗竹席（䉬）。","f「附分」取「分」：草分而席。"),
("櫠","fèi","《尔雅》「櫠，椵，柚属」——柚子一类，木材坚硬。","f「附分」取「分」：木分而坚。"),
("𢠺","bó","《集韵》「心起也」。","b「闭剥」取「剥」：心剥而动。"),
("𤗳","bō","《字汇》「𤗳风版」——挡风板。","b「闭剥」取「剥」：版剥而挡。"),
("驋","bō","《玉篇》「马走」；《广韵》「马怒」；《集韵》「马摇首」。","b「闭剥」取「剥」：马蹄剥地。"),
("𠷑","pō","《玉篇》「妄说也」——胡说。","p「拼辟」取「辟」：言辟而妄。")]
for ch,p,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取癹部「拨动／发射分张」一面，形符各定其落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
cl=[{"id":f"bdc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）","statement":f"{ch}（{p}）：{xp}",
"boundary":"源自《系統漢語》第424部「癹部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡424c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡424c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡424c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))