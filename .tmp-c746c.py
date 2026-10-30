import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
D=[("顦","qiáo","从頁焦聲：顦顇也（《說文》「顦顇也」），枯瘦憔悴。","q「亲缺」取「缺」：面枯而缺。"),
("嫶","qiáo","从女焦聲：憔悴瘦弱（《集韻》），面上枯瘦。","q取亲缺：女瘦而缺。"),
("蟭","jiāo","从虫焦聲：蟭螟，螳螂之卵房（《集韻》）。","j「聚决」取「聚」：蟲聚而决。"),
("潐","jiào","从水焦聲：盡也（《說文》「盡也」），水盡。","j取聚决：水盡而决。"),
("鐎","jiāo","从金焦聲：鐎斗也（《說文》「鐎斗也」），溫器。","j取聚决：金聚而决。")]
cl=[{"id":f"lhuo7-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{s}","boundary":"源自《系統漢語》第550部「火部」（卷九十一 火）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,s,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡550g2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡550g.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡550g.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))