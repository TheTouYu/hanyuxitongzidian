import json,subprocess,os,glob,re
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
def git(*a):
    r=subprocess.run([ROOT+r"\tools\git.cmd"]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
N="字形：古文字字形库未收。"
F="【第594部「彡部」】參系：參本象簪滿珠玉髮飾之跪人，本義插簪，引申參差、眾多、細長垂飾。"
D=[("篸","cēn",F,"从竹參聲：差也（《說文》「差也」），參差不齊；zān 所以綴衣，縫衣針（簪之初文）。","c「刺持」取「持」：參差而持。"),
("鬖","sān",F,"从髟參聲：亂髮也（《集韻》），䰐鬖毛垂、鬖髿髮美。","s「失收」取「收」：髮亂而收。"),
("毿","sān",F,"从毛參聲：毛長皃（《集韻》），與鬖通。","s取失收：毛長而收。"),
("嵾","cēn",F,"从山參聲：嵾差，不齊皃（《廣韻》），嵾嵳山不齊；嵾嶺即武當山。","c取刺持：山雜而持。"),
("蔘","shēn",F,"从艸參聲：人蔘，藥也（《本草》「根如人形」），浸漸長成。","sh取失收：根長而收。"),
("縿","shān",F,"从糸參聲：旌旗之斿也（《說文》「旌旗之斿也」），旗正幅垂飾。","sh取失收：旗垂而收。"),
("幓","shān",F,"从巾參聲：旌旗之游也（《集韻》引《說文》），一曰正幅；襂纚，衣裳毛羽垂皃。","sh取失收：巾垂而收。"),
("𩌰","shān",F,"从革參聲：旌旗旒也（《玉篇》），鞍𩌰垂皃。","sh取失收：鞍垂而收。"),
("鯵","shēn",F,"从魚參聲：鱢字之訛（《字彙》），腥臭。","sh取失收：腥聚而收。"),
("剼","shān",F,"从刀參聲：刈也（《集韻》）；《正字通》謂「劋」之訛，絶也。","sh取失收：刀刈而收。"),
("嘇","shān",F,"从口參聲：口臽嘇物也（《玉篇》），唅嘇，物在口中。","sh取失收：口含而收。"),
("贂","chěn",F,"从貝參聲：賭也（《字彙》），以財相賭。","ch取刺持：賭財而持。")]
rows=[]
for it in D:
    ch,p,F0,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"參系尾组同取「參差、細長垂飾」一面：篸參差、鬖亂髮、毿毛長、嵾山不齊、蔘根長、縿旗斿、幓正幅、𩌰旗旒、鯵腥臭、剼刈、嘇口含、贂賭；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":594,"name":"彡"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lshan6-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第594部「彡部」·參系（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 594彡部參系尾12字")[-60:])
p2=ROOT+r"\intake\20261024-字卡594f.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡594f{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡594f.json"); print(git("commit","-m","knowledge: 594彡部參系尾12条")[-60:])