import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FZ="【第585部「爵部」】爵＝象酒器爵形（三足兩柱有鋬）；音源借音同「雀」。"
F="【第586部「爪部」】爪＝甲骨文象動物趾（指）爪形，西周金文在趾尖加指示符表示趾甲，《說文》「覆手曰爪」；轉義 形狀類似之物（車蓋之爪、笊籬）、抓掐搔等行為；音源為抓撓聲（指爪在肢體末梢，義音通「小」）。"
N="字形：古文字字形库未收。"
D=[("𨰜","jué",FZ,"从金爵聲：同爵（《漢典》），爵之異體。","j「聚决」取「聚」：器聚而决。"),
("𠘣","jiào",FZ,"从仌爵聲：冰裂（《集韻》「音醮，冰裂」）。","j取聚决：冰裂而决。"),
("爪","zhǎo",F,"象動物趾爪形（金文於趾尖加指示符表趾甲）：覆手曰爪（《說文》）；轉義 形似之物（車蓋之爪、笊籬）、抓掐搔。","zh「凿总」取「总」：指聚而总。"),
("抓","zhuā",F,"从手爪聲：抓癢也（《玉篇》），以指爪撓、掐取。","zh取凿总：指撓而总。"),
("枛","zhào",F,"从木爪聲：木刺也（《玉篇》）。","zh取凿总：木刺而总。"),
("笊","zhào",F,"从竹爪聲：笊籬，漉器（《集韻》），撈物之竹器；又鳥居穴曰笊。","zh取凿总：竹漉而总。"),
("䖣","zǎo",F,"从虫爪聲：𧎮之或體，齧人跳蟲（《說文》），跳蚤（取引起抓撓之意）。","z「凿总」取「总」：蟲小而总。"),
("䝖","zhǎo",F,"从豸爪聲：䝖䝤（《唐韻》），豸也（《玉篇》）。","zh取凿总：獸爪而总。"),
("𤔙","shuǎ",F,"从爪：耍（《字彙補》引《海篇》）。","sh「失收」取「收」：玩弄而收。"),
("𤣺","zhǎo",F,"从爪：瑵之或體（《集韻》「車蓋玉瑵」），車蓋玉飾。","zh取凿总：玉飾而总。"),
("𧦐","yán",F,"从言爪聲：音義與訮同（《字彙補》），爭也、訶也怒也。","y「续消」取「续」：爭言而续。"),
("釽","pī",F,"从金爪聲：裂也（《新附》），破裂；裁木為器（《方言》）、鉤釽。","p「拼辟」取「拼」：金屬而拼。")]
for ch,p,F0,xp,sm in D:
    num,name=(585,"爵") if ch in "𨰜𠘣" else (586,"爪")
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"爪部同取「趾爪、抓撓」一面：抓撓、枛木刺、笊漉器、䖣跳蚤、䝖豸、𤔙耍、𤣺車蓋玉飾、𧦐爭言、釽破裂；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":name}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lzhua-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第585／586部「爵部／爪部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡586a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡586a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))