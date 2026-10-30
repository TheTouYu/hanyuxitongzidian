import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FQ="【第540部「秋部」】秋＝蟋蟀象形借為秋季，另造从禾从炅之秋（禾穀成熟）；轉義焦枯、悲愁、時節、聚束。"
FQ2="【第541部「求部」】求＝象獸皮衣之形（毛在外），「裘」之初文，《說文》「皮衣也」；引申求索、請求（借為干求之求）。"
N="字形：古文字字形库未收。"
D=[("揫","jiū",FQ,"从手秋聲：束也（《說文》），收束、聚集。","j「聚决」取「聚」：束聚而决。"),
("甃","zhòu",FQ,"从瓦秋聲：井壁也（《說文》），以磚砌井。","zh「凿总」取「凿」：砖砌而凿。"),
("鍬","qiāo",FQ,"从金秋聲：鍬，掘土之器（鍫之或体）。","q「亲缺」取「亲」：刃親而缺。"),
("鞦","qiū",FQ,"从革秋聲：鞦韆（繩戲）；又馬鞦（後鞦）。","q取亲缺：革系而缺。"),
("偢","chǒu",FQ,"从人秋聲：偢，傻、不慧（《集韻》）。","ch「刺持」取「持」：人呆而持。"),
("蝵","qiū",FQ,"从虫秋聲：蝵，蜘蛛（蛛蝥）。","q取亲缺：蟲结而缺。"),
("求","qiú",FQ2,"象兽皮衣，裘之初文；引申求索、请求。","q取亲缺：求而親。"),
("裘","qiú",FQ2,"从衣求聲：皮衣也（《說文》），毛在外。","q取亲缺：衣親而实。"),
("逑","qiú",FQ2,"从辵求聲：聚斂也（《說文》）；又匹也（君子好逑）。","q取亲缺：行聚而缺。"),
("球","qiú",FQ2,"从玉求聲：玉磬（《說文》「玉也」）；今指圓球。","q取亲缺：玉圓而缺。"),
("救","jiù",FQ2,"从攴求聲：止也（《說文》），救助、止其危。","j「聚决」取「聚」：止聚而决。"),
("俅","qiú",FQ2,"从人求聲：冠飾貌（《說文》引《詩》「戴弁俅俅」）。","q取亲缺：冠饰而親。")]
for ch,p,F0,xp,sm in D:
    bn=540 if ch in "揫甃鍬鞦偢蝵" else 541
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"秋系同取「收斂、就成」一面（揫束、甃井、鍬掘、鞦繩）；求系同取「皮衣、干求」一面（裘衣、逑聚、球玉、救止）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"秋" if bn==540 else "求"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lqiu2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第540－541部（卷九十 秋）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡541a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡541a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡541a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))