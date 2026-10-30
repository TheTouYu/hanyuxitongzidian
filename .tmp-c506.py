import json,subprocess,os,glob
rows=[("攊","lì","《广韵》「击口也」——以手击打口部，使张开。"),
("𡳸","lì","《说文》「履下也」——鞋底；多层布叠纳而成，故字从歷。"),
("壢","lì","《集韵》「坑也」——地面陷下成坑。"),
("䥶","lì","《集韵》「鬲，鼎属」——三足炊器；秝部以秸秆作柴烧陶器，故鬲从秝声。"),
("䍽","lì","《集韵》「羖䍽，山羊」；《本草纲目》「多毛曰羖䍽」，或指阉割之羊。"),
("𥌮","lì","《广韵》「𥌮𥉶，视明貌」——目光清亮，看物分明。"),
("儮","lì","《集韵》「人名」——专名用字，借秝之音。")]
cl=[{"id":f"bl4-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}字，{p}。{txt}",
"boundary":"源自《系統漢語》第425部「秝部」（卷七十 亥）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,txt) in enumerate(rows,1)]
json.dump({"schema_version":1,"intent":"字卡425d2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡425d.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡425d.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))