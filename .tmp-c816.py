import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第575部「𠧪部」】𠧪＝象草木子實垂形；𠧴（逌）＝从𠧪加子房，義同；因𠧪、西形近，諸字多誤从西。"
N="字形：古文字字形库未收。"
D=[("逌","yóu",F,"从辵𠧴聲：氣行皃（《說文》），悠然自得；與「由」通。","y「?」取由声。"),
("由","yóu",F,"从𠧴省：從也、自也（《說文》無，經典通「逌」），原因、緣由。","y取由声。"),
("𤪎","yóu",F,"从玉𠧴聲：玉名（《集韻》），美玉。","y取由声。"),
("𨛕","yóu",F,"从邑𠧴聲：亭名（《集韻》），邮之或體。","y取由声。"),
("麜","lì",F,"从鹿栗聲：麋屬（《說文》「似麋」），鹿類。","l「拢离」取「离」：鹿行而离。"),
("搮","lì",F,"从手栗聲：以手理物（《集韻》）。","l取拢离：手理而离。"),
("𠞉","lì",F,"从刀栗聲：割也（《集韻》）。","l取拢离：割裂而离。"),
("㗚","lì",F,"从口栗聲：聲也（《集韻》），言語聲。","l取拢离：聲散而离。"),
("傈","lì",F,"从人栗聲：傈僳（《正字通》），族名；又謹也。","l取拢离：人列而离。"),
("篥","lì",F,"从竹栗聲：觱篥（《集韻》），胡人吹管。","l取拢离：管鳴而离。"),
("𨍫","lì",F,"从車栗聲：車名（《集韻》），車行聲。","l取拢离：車行而离。"),
("塛","lì",F,"从土栗聲：土塊（《集韻》），墳塛。","l取拢离：土聚而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"𠧴（逌）支取「氣行、緣由」一面：逌、由、𤪎、𨛕；栗支取「堅實、栗然」一面：麜、搮、𠞉、㗚、傈、篥、𨍫、塛；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":575,"name":"𠧪"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ltiao2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第575部「𠧪部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡575b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡575b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))