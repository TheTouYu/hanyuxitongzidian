import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F="【第592部「冬部」】冬＝甲骨文象兩端垂珠之冰淩形，表結冰時節（上古只分春秋，冬在秋末，故有終義）；轉義 最後、完結（《釋名》「終也，物終成也」）；辯證 甲骨文後演化似夂，小篆又加仌，故《說文》「从仌从攵」；音源＝敲擊冰淩聲（古冬、仌、東通用，因懸冰如磬，義音同殸）。"
D=[("冬","dōng",F,"象冰淩形：四時之末（《廣韻》），結冰時節；轉義 終盡。","d「囤动」取「囤」：寒凝而囤。"),
("昸","dōng",F,"从日冬聲：同冬（《字彙補》「與冬同」），冬日。","d取囤动：日短而囤。"),
("苳","dōng",F,"从艸冬聲：艸也（《說文》），苣苳，冬生。","d取囤动：草冬而囤。"),
("赨","tóng",F,"从赤冬聲：赤色也（《說文》），凍得通紅之狀。","t「涂突」取「涂」：色赤而涂。"),
("鉖","tóng",F,"从金冬聲：釣鉖（《玉篇》），本作筒、筩，俗作鉖。","t取涂突：釣具而涂。"),
("㤏","tóng",F,"从心冬聲：憂也（《玉篇》），恎㤏，惶遽。","t取涂突：心惶而涂。"),
("炵","tōng",F,"从火冬聲：火焱也（《玉篇》），火色盛。","t取涂突：火盛而涂。"),
("佟","tóng",F,"从人冬聲：姓也（《廣韻》）。","t取涂突：人姓而涂。"),
("㚵","dōng",F,"从女冬聲：女字（《集韻》）。","d取囤动：女字而囤。"),
("䈺","zhōng",F,"从竹冬聲：竹名（《玉篇》）；戎人呼篋曰䈺。","zh「凿总」取「凿」：竹篋而凿。"),
("疼","téng",F,"从疒冬聲：痛也（《廣韻》），氣疼疼然煩（《釋名》）；或指愛憐。","t取涂突：痛而涂。"),
("蔠","zhōng",F,"从艸冬聲：蔠葵，蘩露（《爾雅》），落葵，纏繞草本，嫩葉可食。","zh取凿总：藤纏而凿。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"冬部同取「結冰、終盡」一面：昸冬日、苳冬生草、赨凍赤、鉖釣具、㤏惶遽、炵火盛、佟姓、㚵女字、䈺竹篋、疼痛、蔠纏草；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":592,"name":"冬"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ldong-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第592部「冬部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡592a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡592a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))