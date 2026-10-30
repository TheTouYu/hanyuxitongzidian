import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【第586部「爪部」·叉支】叉＝商代金文从又的拇指與食指中間加一點，象虎口；《說文》「手指相錯也」；轉義 張開岔開的物體（首笄曰叉→釵；樹幹歧枝）、叉取；辯證《說文》「手指相錯」應是兩手，與字形不符，交錯之意應引申自以叉取物（《段注》「凡布指錯物閒而取之曰叉」）；音源為叉物時所發之聲。"
N="字形：古文字字形库未收。"
D=[("叉","chā",F,"从又（手）拇指食指间一点，象虎口：手指相错（《说文》）；转义 分叉之物、叉取。","ch「刺持」取「持」：指错而持。"),
("釵","chāi",F,"从金叉聲：笄屬（《新附》「本只作叉，此字後人所加」），婦人歧笄（《釋名》「釵，叉也，象叉之形」）。","ch取刺持：笄歧而持。"),
("杈","chā",F,"从木叉聲：枝也（《說文》），枝杈；杈杷（平田具）；行馬（官府門前障礙）。","ch取刺持：枝歧而持。"),
("汊","chà",F,"从水叉聲：水岐流也（《集韻》），河流分岔。","ch取刺持：水分而持。"),
("衩","chǎ",F,"从衣叉聲：衣衩（《玉篇》），衣裙下側開口；褲衩。","ch取刺持：衣開而持。"),
("訍","chài",F,"从言叉聲：疑也（《集韻》），又訍持人短（攻訐）；插話。","ch取刺持：言疑而持。"),
("扠","chāi",F,"从手叉聲：以拳加人（《廣韻》「亦作搋」），打、挾取；又拃（張指量尺寸）。","ch取刺持：拳加而持。"),
("靫","chá",F,"从革叉聲：箭室也（《玉篇》），盛箭器。","ch取刺持：箭藏而持。"),
("䑡","chá",F,"从舟叉聲：艖之或體，舟名（《集韻》）。","ch取刺持：舟小而持。"),
("肞","chā",F,"从肉叉聲：䐤之俗，腶肞，脯也（《龍龕》），乾肉。","ch取刺持：肉乾而持。"),
("芆","chāi",F,"从艸叉聲：鬼芆，草名（《廣韻》）；又草芽（《玉篇》）。","ch取刺持：草芽而持。"),
("䂘","chāi",F,"从石叉聲：小石（《集韻》）。","ch取刺持：石小而持。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"叉支同取「分叉、叉取」一面：釵歧笄、杈枝、汊水流、衩衣開、訍疑言、扠拳加、靫箭室、䑡舟、肞乾肉、芆草芽、䂘小石；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":586,"name":"爪"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lcha-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第586部「爪部」（卷九十六 雀）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p=r"intake\20261024-字卡586b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡586b{it}-2026-10-24","risk":"low","claims":cl},open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))