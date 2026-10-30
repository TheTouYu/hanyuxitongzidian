import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
FQ="【第592部「冬部」·啚族】啚＝甲骨文从㐭从丁（丁即釘），象意釘物挂於牆壁（農村風乾玉米辣椒之法）；轉義 牆上所挂物→圖畫（圖）；挂於壁上→偏遠、狹小、鄙吝（鄙、痞）；辯證《說文》「从囗从㐭」析形不確（口、囗與丁形近）；音源因懸挂之義，義音同「不」（否、鄙通）。"
FB="【第592部「冬部」·稟（㐭）族】稟＝西周金文从米㐭聲（或加攴加禾），象禾晾或穀倉，與嗇同源（《集韻》「穀所振入，或作廩、稟」）；轉義 往上晾禾→敬、下對上報告；收穀入倉→賜穀、賜予、領受；禾晾高處→寒冷淒清（凜）；辯證 俗訛作「禀」（米、示形近）。"
D=[("啚","bǐ",FQ,"从㐭从丁：象釘物挂牆，嗇也（《說文》）；轉義 圖畫、偏鄙。","b「闭剥」取「闭」：挂壁而闭。"),
("𡳄","bǐ",FQ,"从尸从啚：臀也（《玉篇》「𡲀𡳄也，臀也」），懸垂於身後。","b取闭剥：垂後而闭。"),
("𥀜","zī",FQ,"从皮从啚：手足生堅皮也（《廣韻》），即繭，如釘牆風乾之皮革。","z「凿总」取「凿」：皮堅而凿。"),
("圖","tú",FQ,"从囗从啚：畫計難也（《說文》），規畫、謀劃；又 畫形、河圖。","t「涂突」取「涂」：畫而涂。"),
("鄙","bǐ",FQ,"从邑啚聲：五酇為鄙（《說文》），五百家；小邑不能遠通（《釋名》「鄙，否也」）；又 鄙吝。","b取闭剥：邑小而闭。"),
("痞","pǐ",FQ,"从疒否聲（啚之通）：腸中結病（《集韻》「音鄙」），痞塊、痞塞。","p「拼辟」取「拼」：結而拼。"),
("稟","bǐng",FB,"从米㐭聲：賜穀也（《說文》），穀倉；轉義 敬、稟報；又 領受。","b取闭剥：穀聚而闭。"),
("廩","lǐn",FB,"从广稟聲：穀所振入（《說文》「㐭，穀所振入」），倉廩。","l「拢离」取「拢」：穀拢而离。"),
("檁","lǐn",FB,"从木稟聲：屋橫木（《集韻》），桁檁。","l取拢离：木橫而拢。"),
("凜","lǐn",FB,"从仌稟聲：寒也（《玉篇》「凜凜，寒也」），淒清。","l取拢离：寒凝而拢。"),
("懍","lǐn",FB,"从心稟聲：敬也、危懼（《集韻》「懍懍，危懼」）。","l取拢离：心懼而拢。"),
("癛","lǐn",FB,"从疒稟聲：寒病（《集韻》「癛，寒病」），凜冽。","l取拢离：病寒而拢。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"啚族取「挂壁、圖畫、偏鄙」：啚、𡳄臀垂、𥀜繭皮、圖畫、鄙小邑、痞結病；稟族取「穀倉、稟報、凜寒」：稟、廩倉、檁桁、凜寒、懍懼、癛寒病；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":592,"name":"冬"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ldong4-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第592部「冬部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡592d.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡592d{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))