import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第527部「向部」】向＝从宀从口，宀屋、口窗，本義窗（《玉篇》「窻也」）；轉義窗所朝→方向、相向而動；音源借音（向陽有光，義音同昜）。字族三面：窗朝外（趨向相對）／窗明亮（形近冋之訛）／形近舟冏咼之訛。"
N="字形：古文字字形库未收。"
D=[("餉","xiǎng",FY,"从食向聲：饟也，以酒食款待（《說文》）。","x「续消」取「续」：食饋而續。"),
("𥹝","xiàng",FY,"从米向聲：餉之或體，饟也（《集韻》）。","x取续消：糧續而饋。"),
("珦","xiàng",FY,"从玉向聲：玉也（《說文》）。","x取续消：玉潤而續。"),
("恦","xiàng",FY,"从心向聲：念也、想也（《集韻》）。","x取续消：心向而念。"),
("姠","xiàng",FY,"从女向聲：女字（《集韻》）。","x取续消：借聲為字。"),
("晌","shǎng",FY,"从日向聲：日向明也，半晌、晌午（《正字通》）。","sh「失收」取「收」：日斜而收。"),
("䖮","xiǎng",FY,"从虫向聲：蠁，知聲蟲（《說文》司馬相如作䖮）。","x取续消：蟲鳴相續。"),
("嚮","xiàng",FY,"从鄉从向：面也、與向通用，又嚮往（《集韻》）。","x取续消：向而相續。"),
("𩐢","xiǎng",FY,"从音向聲：或作「響」，回音、大聲（《龍龕》）。","x取续消：聲應而續。"),
("𤵼","shāng",FY,"从疒向聲：憂疾（《集韻》），或从商。","sh取失收：病憂而失。"),
("𣂝","xiàng",FY,"从斤向聲：斤之所向，對砍之意（《五音篇海》）。","x取续消：斧向而續。"),
("扄","xiàng",FY,"从戶向聲：戶耳也、門耳（《玉篇》）；俗作扃。","x取续消：戶閉而續。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"向族諧聲字分三面：窗朝外（餉／𥹝／珦／恦／姠／晌／嚮／𩐢）、窗明亮（𤵼／𣂝／扄）、知聲之蟲（䖮）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":527,"name":"向"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第527部「向部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡527a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡527a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡527a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))