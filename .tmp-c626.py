import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第511部「心部」】心＝象動物心臟形（《說文》「人心，土藏，在身之中，象形」息林切）；音源為心跳聲，古心、刅通用。字族衍義①中心②心臟心思③心跳而滲入、插入、透出。"
N="字形：古文字字形库未收。"
D=[("𢛓","lán",F,"《廣韻》「地名」。","l「拢离」取「离」：地分而名。"),
("訫","xìn",F,"《集韻》「信，《說文》：誠也。古作㐰、訫」——言而有信。","x「续消」取「续」：言續而信。"),
("孞","xìn",F,"《字彙補》「同信」——信之異體。","x取续：言續而誠。"),
("吢","qìn",F,"《集韻》「唚，犬吐。或作𢙈，亦書作吣」——貓狗嘔吐；反胃在心窩，常誤作心痛。","q「亲缺」取「缺」：气逆而缺。"),
("沁","qìn",F,"《說文》「水。出上黨羊頭山，東南入河。从水心聲」——沁水；引申滲入、清涼。","q取亲缺：水滲而缺。"),
("抋","qìn",F,"《集韻》「𢱶，挿也。或从心」；《字彙》「播也」——插入、播散。","q取亲缺：手插而缺。"),
("𠖶","qìn",F,"《集韻》「㓎，冷氣。或从心」——寒氣侵人。","q取亲缺：寒侵而缺。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諸字皆以心為聲：杺取木心、芯取燈心、沁取水滲、抋取插入、𠖶取寒氣，各取「心跳透出」一面；故聲符給義、形符定落點。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":511,"name":"心"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxi-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）{xp}",
 "boundary":"源自《系統漢語》第511部「心部」（卷八十四 心）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡511e2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡511e.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡511e.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))