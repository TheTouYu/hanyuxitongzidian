import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第558部「先部」】先＝从「止」在「人」頭頂，象人走在前面；部内余字多為「先」聲而各取一義面（魚、豕、散、欣、癬、粉、盛、老弱、覗、守門、金澤）。"
N="字形：古文字字形库未收。"
D=[("𩶤","xiǎn",FH,"从魚先聲：魚名（《廣韻》「魚名」）。","x「续消」取「续」：魚续而消。"),
("𧱀","xiān",FH,"从豕先聲：豕類（《集韻》「豕類」）。","x取续消：豕行而续。"),
("㪇","xiàn",FH,"从攴先聲：散也（《玉篇》「散也」）。","x取续消：散而续。"),
("㰫","chān",FH,"从欠先聲：欣也、惏也（《玉篇》「欣也、惏也」），歡欣與貪婪。","ch「刺持」取「持」：欣而持。"),
("癬","xuǎn",FH,"从疒鮮聲：乾瘍（《說文》「乾瘍」），癬疥；俗省作𢈇。","x取续消：癬而续。"),
("䊁","shēn",FH,"从米先聲：籸，粉滓也、粥凝也（《類篇》）。","sh「失收」取「收」：粉收而聚。"),
("㮱","shēn",FH,"从木先聲：艸木盛皃（《集韻》「艸木盛皃」）。","sh取失收：木盛而收。"),
("憲","xiàn",FH,"从心从目害省聲：敏也（《說文》「敏也」），博聞強記；老弱為別義。","x取续消：敏而续。"),
("㱡","shēng",FH,"从歹先聲：殑㱡，欲死皃（《玉篇》）。","sh取失收：欲死而收。"),
("𩇜","zhēn",FH,"从見先聲：覗也、譯也（《玉篇》），偵察、傳遞情報；正視。","zh「凿总」取「凿」：偵而凿。"),
("𨴐","shèn",FH,"从門先聲：守門也（《玉篇》「守門也」）；生澀不滑皃。","sh取失收：門守而收。"),
("銑","xiǎn",FH,"从金先聲：金之澤者（《說文》「金之澤者」），一曰小鑿，一曰鐘兩角；以金飾弓兩頭。","x取续消：金澤而续。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"先系余字同取「先行、先見、鋒利」一面：𩶤魚、𧱀豕、㪇散、㰫欣、癬瘍、䊁粉、㮱木盛、憲敏、㱡欲死、𩇜偵、𨴐守門、銑金澤；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":558,"name":"先"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxian2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第558部「先部」（卷九十二 辛）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡558b2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡558b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡558b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))