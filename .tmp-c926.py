import sys,json,subprocess,os,glob,re
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
def git(*a):
    r=subprocess.run([ROOT+r"\tools\git.cmd"]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
N="字形：古文字字形库未收。"
F="【第606部「寸部」】寸＝象事字，在「又」（手）之下加一指示符，指手掌下的寸口（診脈處）；古人以手為尺，稱「同身寸」；引申思量（忖）、短、截斷，又由曲肘引申聚束、包裹。"
D=[("寸","cùn",F,"象事字：又（手）下加指示符，指寸口脈位；引申長度單位、短小。","c「刺持」取「刺」：手刺而量。"),
("酎","zhòu",F,"从酉从肘省：三重醇酒也（《說文》），多次重釀之醇酒。","zh「凿总」取「凿」：酒重而凿。"),
("討","tǎo",F,"从言从寸：治也（《說文》「治也」），整治、聲討（反復申述）。","t「涂突」取「涂」：言治而突。"),
("𨥇","zhòu",F,"同「鑄」，鑄造（《五音篇海》）。","zh取凿总：金鑄而凿。"),
("忖","cǔn",F,"从心寸聲：度也（《說文》「度也」），揣度、思量。","c取刺持：心度而持。"),
("尋","xún",F,"从又从寸（《字彙補》「與尋同」）：尋繹、探尋，八尺曰尋。","x「续消」取「续」：尋续而消。"),
("刌","cǔn",F,"从刀寸聲：切也（《說文》「切也」），細切、割截。","c取刺持：刀切而持。"),
("吋","cùn",F,"英寸舊稱（《字彙》「叱也」另義）。","c取刺持：量而叱。"),
("籿","cùn",F,"公制長度單位，分米之舊譯。","c取刺持：量而分。"),
("肘","zhǒu",F,"从肉从寸：臂節也（《說文》「臂節也」），上臂下臂交接可彎處；甲骨文作「九」象曲臂。","zh取凿总：臂曲而凿。"),
("紂","zhòu",F,"从糸肘省聲：馬緧也（《說文》「馬緧也」），駕車馬後之皮帶。","zh取凿总：皮帶而凿。"),
("村","cūn",F,"从邑屯聲（俗作村）：聚落也（《集韻》「聚也」），村莊。","c取刺持：聚落而持。")]
rows=[]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"寸部三面：探脈思量（忖、討、酎）、一寸截斷（刌、吋、籿）、曲肘聚束（肘、紂、村）。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":606,"name":"寸"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lcun-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第606部「寸部」（卷一百 壽）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 606寸部12字")[-40:])
p2=ROOT+r"\intake\20261024-字卡606a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡606a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡606a.json"); print(git("commit","-m","knowledge: 606寸部12条")[-40:])