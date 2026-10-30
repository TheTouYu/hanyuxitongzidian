import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第567部「七部」】七＝甲骨文在「一」中間加指示符，象切、刻之意，「切」之初文（《廣韻》「割也、刻也」）；借為數詞七（源于手势语）；音源為切刻聲。"
N="字形：古文字字形库未收。"
D=[("七","qī",FH,"从一加指示符（丁山「象當中切斷形」），切割之初文，借為數詞七；《說文》「陽之正也」不確。","q「亲缺」取「亲」：切而亲。"),
("切","qiē",FH,"从刀七聲：刌也（《說文》「刌也」），割、截、迫近。","q取亲缺：刀割而亲。"),
("砌","qì",FH,"从石切聲：階甃也（《說文》「階甃也」），台階→壘砌。","q取亲缺：石垒而亲。"),
("沏","jiě",FH,"从水切聲：流皃（《玉篇》），水聲、疾流；又音 qī，沸水沖泡。","q取亲缺：水冲而亲。"),
("䀙","qì",FH,"从目切聲：視也（《玉篇》「視也」），察也、衺視。","q取亲缺：視察而亲。"),
("𦕀","qì",FH,"从耳切聲：䏅也，聦也（《集韻》）。","q取亲缺：聽聪而亲。"),
("苆","qiē",FH,"从艸切聲：麻刀（刮麻皮器具）。","q取亲缺：麻割而亲。"),
("䟙","qiè",FH,"从足切聲：跌也（《集韻》「跌也」）。","q取亲缺：蹉跌而亲。"),
("袃","chài",FH,"从衣切聲：𧀱芥，刺鯁也（《集韻》），或作蔕。","ch「刺持」取「刺」：刺鯁而持。"),
("𢪃","cù",FH,"从手切聲：摩也（《玉篇》「摩也」），磨也。","c取刺持：摩磨而持。"),
("叱","chì",FH,"从口七聲：訶也（《說文》「訶也」），大聲呵斥。","ch取刺持：呵斥而刺。"),
("柒","qī",FH,"从木桼聲：漆之俗字（《集韻》），七的大寫。","q取亲缺：漆黏而亲。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"七系同取「切割、迫近」一面：切割、砌階、沏流、䀙察、𦕀聰、苆麻刀、䟙跌、袃刺、𢪃摩、叱訶、柒漆；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":567,"name":"七"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lqi-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第567部「七部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡567a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡567a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡567a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))