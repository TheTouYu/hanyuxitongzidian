import json,subprocess,os,glob,re
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a,dec=True):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
def git(*a):
    r=subprocess.run([ROOT+r"\tools\git.cmd"]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
N="字形：古文字字形库未收。"
F="【第594部「彡部」】彡＝三丿，象細長而多之物；㐱（zhěn）＝从人从彡，毛髮稠密（《說文》「稠髮也」），引申細密、細緻，為本部二級字根。"
D=[("診","zhěn",F,"从言㐱聲：視也（《說文》「視也」），診視、診斷。","zh「凿总」取「凿」：視密而凿。"),
("畛","zhěn",F,"从田㐱聲：井田間陌也（《說文》「井田間陌也」），田間小路。","zh取凿总：田密而凿。"),
("趁","chèn",F,"从走㐱聲：𧾍也（《說文》「𧾍也」），趁逐、趕趁。","ch「刺持」取「持」：走密而持。"),
("珍","zhēn",F,"从玉㐱聲：寶也（《說文》「寶也」），珍寶。","zh取凿总：玉密而凿。"),
("昣","zhěn",F,"从日㐱聲：明也（《集韻》），日明。","zh取凿总：日密而凿。"),
("聄","zhěn",F,"从耳㐱聲：視也（《集韻》），耳聽。","zh取凿总：耳密而凿。"),
("胗","zhēn",F,"从肉㐱聲：脣瘍也（《說文》「脣瘍也」），唇瘡；又 鳥獸胃。","zh取凿总：肉密而凿。"),
("沴","lì",F,"从水㐱聲：水不利也（《說文》「水不利也」），水氣不和、災氣。","l「拢离」取「拢」：水聚而拢。"),
("眕","zhěn",F,"从目㐱聲：目有所恨而止也（《說文》），目重而止。","zh取凿总：目密而凿。"),
("紾","zhěn",F,"从糸㐱聲：轉也（《說文》「轉也」），糾轉；又 單衣。","zh取凿总：絲密而凿。"),
("軫","zhěn",F,"从車㐱聲：車後橫木也（《說文》「車後橫木也」），轉義 哀痛（軫念）。","zh取凿总：木密而凿。"),
("殄","tiǎn",F,"从歺㐱聲：盡也（《說文》「盡也」），滅絕。","t「涂突」取「涂」：盡而突。")]
rows=[]
for it in D:
    ch,p,F0,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"㐱系同取「細密、稠多」一面：診視、畛陌、趁逐、珍寶、昣明、聄聽、胗瘡、沴災、眕止、紾轉、軫木、殄盡；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":594,"name":"彡"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lshan2-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第594部「彡部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
print(git("add","web/public/cards")[-60:])
print(git("commit","-m","cards: 594彡部㐱族12字")[-80:])
p2=ROOT+r"\intake\20261024-字卡594b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡594b{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
print(git("add","knowledge","data/knowledge","intake/20261024-字卡594b.json")[-40:])
print(git("commit","-m","knowledge: 594彡部㐱族12条")[-80:])