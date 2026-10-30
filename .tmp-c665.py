import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第527部「向部」·堂系（二级字根）】堂（坣㙶）＝从土尚聲：「尚」敞開敞亮，「土」象用土築成的高臺（《玉篇》「土爲屋基也」），或指空闊高大的殿堂（《說文》「殿也」）；轉義顯明、高大（《釋名》「堂，猶堂堂，高顯貌也」）。字族三面：堂之空（顯明空闊）／堂之高（撐起抵距）／堂之聲（鼓鐘之聲）。"
N="字形：古文字字形库未收。"
D=[("堂","táng",FY,"从土尚聲：用土築成的高臺、空闊高大的殿堂；引申顯明、高大。","t「涂突」取「涂」：臺鋪而突。"),
("鼞","tāng",FY,"从鼓堂聲：鼓聲（《說文》引《詩》「擊鼓其鼞」）。","t取涂突：鼓聲震突。"),
("鏜","tāng",FY,"从金堂聲：鐘鼓之聲；又以鐵貫物、鏜孔。","t取涂突：金聲震突。"),
("嘡","tāng",FY,"象聲詞，形容打鐘、敲鑼一類的聲音。","t取涂突：聲響而突。"),
("膛","táng",FY,"《玉篇》「肥皃」；今指胸腔、體腔或器物中空處。","t取涂突：中空而突。"),
("樘","chēng",FY,"从木堂聲：衺柱也（《說文》），斜柱支撐，即「撐」；又音 táng，車樘、門窗框。","ch「刺持」取「持」：柱撐而持。"),
("蹚","tāng",FY,"从足堂聲：行不正皃；又距也（撐）、蹚水、趟。","t取涂突：足蹚而突。"),
("憆","chēng",FY,"从心堂聲：直視也（《集韻》瞠之或體），瞠目。","ch取刺持：目直而持。"),
("摚","chēng",FY,"从手堂聲：距也、撐拒（《集韻》）。","ch取刺持：手撐而持。"),
("漟","táng",FY,"从水堂聲：溪也（《玉篇》）。","t取涂突：水溪而突。"),
("隚","tàng",FY,"从阜堂聲：殿基（《廣韻》）。","t取涂突：基高而突。"),
("饄","táng",FY,"从食堂聲：同「餹」，糖（《正字通》）。","t取涂突：飴甜而突。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"堂系諧聲字分三面：堂之空（膛／漟）／堂之高（樘／隚／摚）／堂之聲（鼞／鏜／嘡／憆／蹚／饄）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":527,"name":"向"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ltang-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第527部「向部」（卷八十八 昜，堂系）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡527e2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡527e.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡527e.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))