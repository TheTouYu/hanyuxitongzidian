import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第569部「黍部」】黍＝甲骨文从禾四周有小點，象穗長而穀粒鬆散（糜子、黃黍）；黏者為黍，不黏者為稷；音近「朱」（黏如漆），字族多以「黎」表音，義取離（色黃黑如離）。"
N="字形：古文字字形库未收。"
D=[("黍","shǔ",F,"从禾加點：穗長粒散（《六書精薀》「象細粒散垂之形」），糜子；黏可釀酒。","sh「失收」取「收」：粒散而收。"),
("黎","lí",F,"从黍从勿：履黏也（《說文》），以黍米作糊黏鞋；引申黑色、眾多、老。","l「拢离」取「离」：黏分而离。"),
("邌","lí",F,"从辵黎聲：徐也（《說文》「徐也」），徐緩。","l取拢离：徐行而离。"),
("潻","shǔ",F,"从水黍聲：水名（《玉篇》「水名」），非指黍。","sh取失收：水滞而收。"),
("黐","chī",F,"从黍離聲：黏也（《玉篇》），木膠可黏鳥。","ch「刺持」取「持」：膠黏而持。"),
("犂","lí",F,"从牛黎聲：耕也（《說文》「耕也」），墾田器。","l取拢离：犁地而离。"),
("𨞃","lí",F,"从邑黎聲：殷諸侯國（《說文》），西伯戡𨛫之國。","l取拢离：邑分而离。"),
("䊍","lí",F,"从米黎聲：𪐅，饘也（《集韻》），厚粥。","l取拢离：粥黏而离。"),
("𧑓","shǔ",F,"从蟲黍聲：蟲名（《博雅》），鼠婦蟲（俗稱潮蟲）。","sh取失收：蟲聚而收。"),
("𩁟","lí",F,"从隹黎聲：𩁟黃也（《說文》），即黃鸝，色黎黑而黃。","l取拢离：羽黑而离。"),
("藜","lǐ",F,"从艸黎聲：艸也（《說文》），嫩葉可食、老莖可杖。","l取拢离：草蔓而离。"),
("瓈","lí",F,"从玉黎聲：玻瓈（《玉篇》），寶玉、玻璃。","l取拢离：玉润而离。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"黍部三义：①黏滯遲緩（黎、邌、潻、黐、犂、𨞃、䊍、𧑓）②色黃黑（𩁟、藜）③音譯（瓈）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":569,"name":"黍"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lshu-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第569部「黍部」（卷九十四 七）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡569a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡569a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡569a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))