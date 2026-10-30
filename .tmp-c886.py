import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F="【第592部「冬部」】冬＝象冰淩垂珠形，結冰時節；轉義 終盡（《釋名》「終也」）；音源＝敲冰聲（懸冰如磬，義音同殸）。本批取「終了終盡」「螽紋」「冬聲」三面。"
D=[("柊","zhōng",F,"从木冬聲：木名（《廣韻》），柊葉寬大如葵，可作粽葉，故从冬。","zh「凿总」取「凿」：葉大而凿。"),
("終","zhōng",F,"从糸冬聲：絿絲也（《說文》「絿絲也」），纏緊絲；引申 極、窮、死、竟、盡。","zh取凿总：絲纏而凿。"),
("𣧩","zhōng",F,"从歹冬聲：歿也（《玉篇》「歿也，今作終」），竟也。","zh取凿总：殘而凿。"),
("鴤","dōng",F,"从鳥冬聲：䳉鳥，好入水食，似鳧形小（《廣韻》）；又鴆，毒鳥。","d「囤动」取「囤」：鳥潛而囤。"),
("𧲴","dōng",F,"从豸冬聲：獸似豹有角（《玉篇》），疑即猞猁，斑紋如豹、兩耳聳立如角。","d取囤动：獸斑而囤。"),
("螽","zhōng",F,"从蟲冬聲：蝗類（《詩》「五月斯螽動股」），股鳴、繁殖成群。","zh取凿总：蟲群而凿。"),
("鼨","zhōng",F,"从鼠冬聲：鼠名（《說文》「豹文鼠也」）。","zh取凿总：鼠斑而凿。"),
("䶱","zhōng",F,"从龜冬聲：龜名（《說文》「龜名」）。","zh取凿总：龜背而凿。"),
("𩂓","dōng",F,"从雨冬聲：雨貌（《集韻》），冬日雨雪。","d取囤动：雨凝而囤。"),
("鼕","dōng",F,"从鼓冬聲：鼕鼕，鼓聲（《廣韻》），象冬冬之聲。","d取囤动：鼓震而囤。"),
("汷","zhōng",F,"从水冬聲：水名（《集韻》「汷，水名」）。","zh取凿总：水流而凿。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"冬部同取「終盡、冬物」一面：柊寬葉、終纏絲、𣧩歿、鴤水鳥、𧲴豹文獸、螽蝗、鼨豹文鼠、䶱龜、𩂓冬雨、鼕鼓聲、汷水名；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":592,"name":"冬"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ldong2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第592部「冬部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡592b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡592b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))