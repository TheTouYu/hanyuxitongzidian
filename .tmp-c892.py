import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未存。"
F="【第592部「冬部」·亶族】亶＝从㐭从旦，象穀倉堆滿（《說文》「多穀也」）；轉義 誠然、信（《爾雅》「亶，信也」）、厚；此族取「穀多、厚實、展轉」三面。"
D=[("亶","dǎn",F,"从㐭从旦：多穀也（《說文》「多穀也」），穀倉堆滿；轉義 誠然、信、厚。","d「囤动」取「囤」：穀多而囤。"),
("壇","tán",F,"从土亶聲：祭壇（《說文》「祭場也」），土築高臺。","t「涂突」取「涂」：土臺而涂。"),
("檀","tán",F,"从木亶聲：木名（《說文》「檀，木也」），材堅。","t取涂突：木堅而涂。"),
("顫","chàn",F,"从頁亶聲：頭不正也（《說文》「頭不正也」），顫動、戰慄。","ch「刺持」取「持」：頭摇而持。"),
("氈","zhān",F,"从毛亶聲：撚毛也（《說文》「撚毛也」），毛氈。","zh「凿总」取「凿」：毛撚而凿。"),
("羶","shān",F,"从羊亶聲：羊臭也（《說文》「羊臭也」），羶腥；又通馨。","sh「失收」取「收」：羊臭而收。"),
("擅","shàn",F,"从手亶聲：專也（《說文》「專也」），擅長、獨斷。","sh取失收：手專而收。"),
("禪","shàn",F,"从示亶聲：祭天也（《說文》「祭天也」）；又 靜、禪讓。","sh取失收：祭而收。"),
("嬋","chán",F,"从女亶聲：嬋娟，美貌（《集韻》）；嬋連，牽連。","ch取刺持：女美而持。"),
("嬗","shàn",F,"从女亶聲：緩也（《說文》「緩也」），更替、傳遞。","sh取失收：更而收。"),
("鱣","zhān",F,"从魚亶聲：鯉屬（《說文》「鱣，鯉屬」），鱘鰉。","zh取凿总：魚大而凿。"),
("澶","chán",F,"从水亶聲：澶淵，地名（《說文》「澶淵，在宋」），水漫。","ch取刺持：水漫而持。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"亶族同取「穀多厚實、展轉相因」一面：亶多穀、壇土臺、檀堅木、顫頭摇、氈撚毛、羶羊臭、擅專、禪祭天、嬋美貌、嬗更替、鱣大魚、澶水漫；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":592,"name":"冬"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ldong5-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第592部「冬部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡592e.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡592e{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))