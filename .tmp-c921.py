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
F2="【第600部「巨部」】巨＝象矩（工字尺）之形，量方形之器；引申大、巨大。"
F3="【第601部「麤部」】麤＝从鹿二疊：鹿角枝杈、腿細善走、性警惕，二疊表極致——行超遠／角粗大／相背而食；引申粗糙，俗作麤/粗。"
D=[("鉅","jù",F2,"从金巨聲：大剛也（《說文》「大剛也」），巨鐵；引申巨大。","j「聚决」取「聚」：鐵聚而决。"),
("詎","jù",F2,"从言巨聲：詎猶豈也（《廣韻》），反詰詞；不可、至。","j取聚决：言聚而决。"),
("柜","jǔ",F2,"从木巨聲：柜柳，木名（《爾雅》），杞柳之一種。","j取聚决：木聚而决。"),
("岠","jù",F2,"从山巨聲：大山（《集韻》），山名。","j取聚决：山聚而决。"),
("歫","jù",F2,"从止巨聲：止也（《說文》「止也」），歫止、距離。","j取聚决：止聚而决。"),
("蚷","jù",F2,"从虫巨聲：馬蚷，蟲名（《莊子》「馬蚷」），即馬陸。","j取聚决：蟲聚而决。"),
("粔","jù",F2,"从米巨聲：粔籹，環餅（《說文》），以蜜和米煎之。","j取聚决：米聚而决。"),
("秬","jù",F2,"从禾巨聲：黑黍也（《說文》「黑黍也」），黑黍。","j取聚决：禾聚而决。"),
("麤","cū",F3,"从三鹿：行超遠也（《說文》「行超遠也」）；又角粗大、相背而食（《字統》「警防也」）；引申粗糙。","c「刺持」取「刺」：鹿奔而刺。"),
("𧆓","cū",F3,"从艸麤聲：艸履也（《說文》「艸履也」），草鞋。","c取刺持：草持而刺。"),
("麁","cū",F3,"从鹿从昔？《廣韻》：「踈也、大也、物不精也。本亦作麤」。","c取刺持：粗大而刺。"),
("𥼡","cū",F3,"从米麤聲：米不精也（《廣韻》「米不精也」），糙米。","c取刺持：米粗而刺。")]
rows=[]
for ch,p,F0,xp,sm in D:
    num=600 if F0==F2 else 601
    nm="巨" if num==600 else "麤"
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"巨部取「矩尺、巨大」：鉅鐵、詎詰、柜柳、岠山、歫止、蚷蟲、粔餅、秬黍；麤部取「鹿行超遠、粗大」：麤奔、𧆓草履、麁粗、𥼡糙米。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":nm}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lju2-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":f"源自《系統漢語》第{num}部「{nm}部」（卷九十九 且）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 600巨余+601麤部12字")[-40:])
p2=ROOT+r"\intake\20261024-字卡601a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡601a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡601a.json"); print(git("commit","-m","knowledge: 600余+601麤部12条")[-40:])