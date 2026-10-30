import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F1="【第564部「進部」】進＝从止从隹：止指行走、隹指鳥，象鳥一樣行進；鳥只能向前不能後退，故表前進；引申進步、晉級、呈獻。"
F2="【第565部「兟部」】兟＝从二先，甲骨文象人牽引另一人（引導），《說文》「進也」；㚘＝从二夫（簪髮成年男子），並行、伴侶；部族以「贊」為重點（贊禮司儀，引申分散、稱頌、聚集）。"
N="字形：古文字字形库未收。"
D=[("進","jìn",F1,564,"从止从隹：象鳥行進，前也、升也、登也（《玉篇》），引申呈獻。","j「聚决」取「聚」：鳥聚而决。"),
("暹","xiān",F1,564,"从日進聲：日光升也（《集韻》「日光升也」）。","x「续消」取「续」：日升而续。"),
("䗯","jìn",F1,564,"从虫進聲：蛤類（《集韻》），似蛤而扁有毛。","j取聚决：蛤聚而决。"),
("𧔷","jìn",F1,564,"从虫晉聲：𧍧𧔷，似蛤而扁（《字彙補》），同䗯。","j取聚决：蛤扁而决。"),
("璡","jīn",F1,564,"从玉進聲：石之似玉者（《說文》「石之似玉者」）。","j取聚决：玉润而决。"),
("𥳟","jiǎn",F1,564,"从竹進聲：竹名（《集韻》「竹名」）。","j取聚决：竹直而决。"),
("擓","kuǎi",F1,564,"从手淮聲：揩摩也（《集韻》），形近「淮」之訛。","k「口控」取「控」：手摩而控。"),
("兟","shēn",F2,565,"从二先：進也（《說文》「進也。从二先」），象人牽引前行；又眾多皃。","sh「失收」取「收」：行聚而收。"),
("兓","qīn",F2,565,"从二旡：旡本與欠同（張口），二疊表大聲、會說。","q「亲缺」取「亲」：口張而亲。"),
("㚘","bàn",F2,565,"从二夫：竝行也（《說文》「竝行也」），讀若伴侶之伴。","b「闭剥」取「闭」：伴行而闭。"),
("贊","zàn",F2,565,"从貝从兟：贊禮司儀（《周禮·司儀》），引導賓客、導引；引申分散、稱頌、聚集。","z「凿总」取「总」：聚而总。"),
("攢","zǎn",F2,565,"从手贊聲：聚也（《集韻》「聚也」），攢聚。","z取凿总：手聚而总。")]
for ch,p,F0,num,xp,sm in D:
    nm={564:"進",565:"兟"}[num]
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"進／兟系同取「向前導引、聚而復散」一面：暹日升、䗯蛤、璡玉、𥳟竹、兟牽引、兓會說、㚘並行、贊司儀、攢聚；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":nm}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ljin-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":f"源自《系統漢語》第{num}部「{ {564:'進',565:'兟'}[num] }部」（卷九十二 辛）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,num,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡564a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡564a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡564a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))