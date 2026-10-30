import json,subprocess,os,glob
rows=[("醱","pō","酒再酿谓之「酦」，今作「发酵」的「酦」；本义是酒液再次酝酿而起的变化。"),
("𩯌","bō","鬃毛纷张之貌——「𩯌䰖，鬓多毛」；取拨动时毛发被分张的样子。"),
("𩞽","bó","同「餺」，餺饦即饼；本义是麦粉分张压成片再蒸熟的面食。"),
("蕟","fà","一名草，又指粗竹席（籧篨）；草茎分张而编成席。"),
("櫠","fèi","《尔雅》「櫠、椵，柚属」——柚子一类果树，木材坚硬。"),
("𢠺","bó","心起也——心动而起伏；取拨动之义落在心上。"),
("𤗳","bō","挡风版；版片分张而立，以遮风。"),
("驋","bō","马走、马怒、马摇首——马蹄拨地、鬃毛分张之状。")]
cl=[{"id":f"fg-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}字，{p}。{txt}",
"boundary":"源自《系統漢語》第424部「癹部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,txt) in enumerate(rows,1)]
json.dump({"schema_version":1,"intent":"字卡424d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡424d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡424d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))