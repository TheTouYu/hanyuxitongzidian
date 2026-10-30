import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F="【第592部「冬部」·亶族】亶＝蟺（黄鳝）之初文：无鳞→袒露平坦、色赤黄、氣腥臊、黏液黏稠、爬動難行；音源本㐭声，义音同「旦」。"
D=[("襢","tǎn",F,"从衣亶聲：肉袒也（《玉篇》「袒，肉袒也，或作襢」），去上服；襢衣，坦然正白無文采。","t「涂突」取「涂」：衣袒而涂。"),
("䡀","zhǎn",F,"从亶（倮）：裸形，無可蔽也（《廣韻》），倮也；又 體搖。","zh「凿总」取「凿」：裸而凿。"),
("繵","dàn",F,"从糸亶聲：束腰大帶（《廣韻》「束𦝫大帶」）；又 繩、紫色、繞。","d「囤动」取「囤」：帶束而囤。"),
("憻","tǎn",F,"从心亶聲：同坦（《字彙》），寬也、明也、平安；又 誠。","t取涂突：心坦而涂。"),
("譠","tán",F,"从言亶聲：譠謾，欺也、慢言也（《玉篇》《方言》），緩語。","t取涂突：言慢而涂。"),
("𢋃","dǎn",F,"从广亶聲：偏舍（《廣韻》），簡陋的偏房。","d取囤动：舍偏而囤。"),
("𤮜","shàn",F,"从瓦亶聲：器縁也（《玉篇》），瓦器之緣。","sh「失收」取「收」：器緣而收。"),
("䕊","tán",F,"从艸亶聲：艸名（《集韻》），艸蔓布地。","t取涂突：草蔓而涂。"),
("璮","tǎn",F,"从玉亶聲：玉名（《集韻》「音坦」）。","t取涂突：玉堅而涂。"),
("旜","zhān",F,"从㫃亶聲：旃之或體（《說文》「旃，或从亶」），通帛為旜，曲柄紅旗。","zh取凿总：旗張而凿。"),
("𣋊","dàn",F,"从日亶聲：曛也（《集韻》），日暗。","d取囤动：日曛而囤。"),
("膻","dàn",F,"从肉亶聲：肉膻也（《說文》），脫衣露上身（同但）；又 羊臭（羶）。","d取囤动：肉腥而囤。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"亶族取「袒露、赤黄、腥臊、黏稠、難行」五面：襢肉袒、䡀裸形、繵束帶、憻坦、譠慢言、𢋃偏舍、𤮜器緣、䕊蔓草、璮玉、旜紅旗、𣋊日曛、膻肉腥；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":592,"name":"冬"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ldong7-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第592部「冬部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p2=r"intake\20261024-字卡592g.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡592g{it}-2026-10-24","risk":"low","claims":cl},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))