import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第585部「爵部」】爵＝象酒器爵形：三足、側有鋬、上有兩柱（側視或顯一柱）、侈口有嘴；《說文》「禮器也，所以飲器象雀者，取其鳴節節足足也」；轉義 酒、舀酒器、爵位（爵有五種，貴者獻爵、賤者獻散）；辯證《說文》以爵為雀之象形不確（有「其鳴節節足足」語，段注改「雀」為「爵」）；音源借音，因爵形如雀，義音同「雀」。"
N="字形：古文字字形库未收。"
D=[("爵","jué",F,"象酒器爵形（三足兩柱有鋬）：禮器也（《說文》）；轉義 酒（《易》「我有好爵」）、舀酒器、爵位（貴者獻爵）。","j「聚决」取「聚」：器聚而决。"),
("斝","jiǎ",F,"从吅从斗、冂象形：玉爵也（《說文》「夏曰琖，殷曰斝，周曰爵」），三足兩柱、圓口而大。","j取聚决：器大而决。"),
("爝","jiào",F,"从火爵聲：苣火，祓也（《說文》引呂不韋），火炬（束葦燒之以除惡）。","j取聚决：火聚而决。"),
("𥷮","zhuó",F,"从竹爵聲：䇇也（《集韻》），魚罩；又罺之或體，撩罟。","zh「凿总」取「总」：罩聚而总。"),
("䂃","jiào",F,"从目爵聲：瞋目也（《集韻》），怒目；一曰目冥。","j取聚决：目張而决。"),
("釂","jiào",F,"从酉爵聲：㱃酒盡也（《說文》「㱃酒盡也」），用爵乾杯。","j取聚决：酒盡而决。"),
("灂","zhuó",F,"从水爵聲：水小聲（《說文》「水小聲」），水聲雨聲。","zh取凿总：水激而总。"),
("嚼","jiáo",F,"从口爵聲：噍之或體，齧也（《說文》），咀嚼；又飲酒乾杯。","j取聚决：齒齧而决。"),
("㩱","jué",F,"从手爵聲：擇也（《博雅》）；一曰捎也、掆也；又削也。","j取聚决：擇取而决。"),
("皭","jiào",F,"从白爵聲：白色（《集韻》）；一曰淨皃。","j取聚决：色白而决。"),
("穱","zhuō",F,"从禾爵聲：小也（《玉篇》），又早熟；刈稻之地種麥。","zh取凿总：禾小而总。"),
("𢥚","jiào",F,"从心爵聲：性急也（《集韻》「音醮，性急」）。","j取聚决：性急而决。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"爵部同取「器形、小淨快」一面：斝大器、爝火炬、𥷮魚罩、䂃瞋目、釂乾杯、灂水聲、嚼咀嚼、㩱擇取、皭白色、穱小禾、𢥚性急；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":585,"name":"爵"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ljue-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第585部「爵部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡585a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡585a{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))