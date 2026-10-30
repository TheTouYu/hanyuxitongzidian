import sys,json,subprocess,os,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
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
F595="【第595部「㦰部」】㦰＝戈割从足，全部割取→滅盡；轉義 纖細；本組取其「割取、除滅、擦拭、浸漬」一面。"
F596="【第596部「羴部」】羴（shān）＝羊之二疊三疊（或四疊），象群羊；羊肉腥臊，疊體象十分腥臊（《說文》「羊臭也」）；亦可象溫順（歸「善」）、鮮美（歸「鱻/鮮」）；轉義 插入、爭先恐後；音源借音同「亶」。"
D=[("殲","jiān",F595,"从歺韱聲：微盡也（《說文》「微盡也」），殲滅，纖微都盡。","j「聚决」取「聚」：聚盡而决。"),
("㡨","jiān",F595,"从巾韱聲：拭也（《說文》「拭也」），揩拭細微；又 摽識（標籤）。","j取聚决：拭微而决。"),
("䤘","chǎn",F595,"从酉韱聲：酢也（《說文》「酢也」），醋味濃厚。","ch「刺持」取「持」：酸濃而持。"),
("瀸","jiān",F595,"从水韱聲：漬也（《說文》「漬也」），成捆浸漬漚之；《爾雅》「泉一見一否為瀸」。","j取聚决：水漬而决。"),
("懺","chàn",F595,"从心韱聲：自陳悔也（《廣韻》），懺悔；梵文 kṣama（懺摩）音譯之省。","ch取刺持：悔陳而持。"),
("𠠃","qiān",F595,"从刀韱聲：割也（《廣韻》），切也（《集韻》）。","q「亲缺」取「亲」：刀切而缺。"),
("䑎","chǎn",F595,"从肉韱聲：臉䑎，以豬腸屑椒芥醯鹽為之（《集韻》），肉羹。","ch取刺持：肉雜而持。"),
("𡄑","jiān",F595,"从口韱聲：嚱㖩，不廉（《玉篇》），貪食無節。","j取聚决：口貪而决。"),
("羴","shān",F596,"从三羊（或二疊、四疊）：羊臭也（《說文》「羊臭也」），羶之初文；群羊、溫順、鮮美三面。","sh「失收」取「收」：羊聚而收。"),
("羼","chàn",F596,"从羊在尸下（羊相廁）：羊相廁也（《說文》），夾雜、插入；轉義 爭先恐後。","ch「刺持」取「持」：夾廁而持。"),
("𠠮","chǎn",F596,"从刀羼聲：剗之異體，平滅、剷除。","ch取刺持：剷平而持。"),
("𢺟","chàn",F596,"从手羼聲：插入、攙入（《集韻》），以手廁入。","ch取刺持：手插而持。")]
rows=[]
for it in D:
    ch,p,F0,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    num=595 if F0==F595 else 596
    nm="㦰" if num==595 else "羴"
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"㦰部取「割取除滅」：殲微盡、㡨揩拭、䤘醋濃、瀸浸漬、懺悔陳、𠠃切割、䑎肉羹、𡄑貪食；羴部取「羊之腥臊廁雜」：羴羊臭、羼相廁、𠠮剷平、𢺟攙入。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":nm}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lshou1-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":f"源自《系統漢語》第{num}部「{nm}部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 595尾+596羴部首12字")[-60:])
p2=ROOT+r"\intake\20261024-字卡596a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡596a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡596a.json"); print(git("commit","-m","knowledge: 595尾+596羴部首12条")[-60:])