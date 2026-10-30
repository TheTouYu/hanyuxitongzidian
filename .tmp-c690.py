import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
D=[("臧","zāng","以戈守臣为善（《說文》「善也」），后通「藏」。"),
("藏","cáng","匿也（《說文》），戰國古文从宀醬聲，指密放醬菜之所。"),
("臟","zàng","五臟也（《正字通》），胸內藏精藏神之器官。"),
("贓","zāng","納賄曰贓（《廣韻》），非理所得財物。"),
("㵴","cáng","沒也（《集韻》），从水臧聲，沉沒。"),
("倉","cāng","象穀倉形（《說文》「穀藏也」），上蓋下口。"),
("艙","cāng","从舟倉聲，船中載人貨的空間。"),
("滄","cāng","寒也（《說文》），从水倉聲；又滄海。"),
("凔","cāng","寒也（《說文》），从仌倉聲。"),
("鎗","chēng","鐘聲也（《說文》），从金倉聲；又兵器。"),
("愴","chuàng","傷也（《說文》），从心倉聲，悲傷。"),
("戧","qiāng","傷也（《說文》），从戈倉聲；又撑、逆。")]
cl=[{"id":f"lz2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{s}","boundary":"源自《系統漢語》第534部「爿部」（卷八十九 象）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,s) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡534zangb2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡534zang2.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡534zang2.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
else:
    print(out[-600:])