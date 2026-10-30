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
F="【第603部「周部」】周＝象方格內刻畫紋飾之形，指雕刻，「彫」之初文，《說文》「琢文也」；引申周密、周遍、周旋。"
D=[("琱","diāo",F,"从玉周聲：治玉也（《說文》「治玉也」），雕琢玉石。","d「囤动」取「囤」：玉聚而動。"),
("錭","diāo",F,"从金周聲：錭琢，鈍也（《集韻》）；治金。","d取囤动：金聚而動。"),
("蜩","tiáo",F,"从虫周聲：蟬也（《說文》「蟬也」），蜩鳴。","t「涂突」取「涂」：蟲鳴而突。"),
("惆","chóu",F,"从心周聲：失意也（《說文》「失意也」），惆悵。","ch「刺持」取「持」：心失而持。"),
("稠","chóu",F,"从禾周聲：多也（《說文》「多也」），稠密。","ch取刺持：禾聚而持。"),
("綢","chóu",F,"从糸周聲：繆也（《說文》「繆也」），綢繆、纏繞。","ch取刺持：絲纏而持。"),
("裯","chóu",F,"从衣周聲：襌被也（《說文》「襌被也」），牀帳、單被。","ch取刺持：衣覆而持。"),
("調","tiáo",F,"从言周聲：和也（《說文》「和也」），調和、調理。","t取涂突：言和而突。"),
("賙","zhōu",F,"从貝周聲：振贍也（《說文》「振贍也」），賙濟。","zh「凿总」取「凿」：貝施而凿。"),
("週","zhōu",F,"从辵周聲：循環也（後起字），週遍、週年。","zh取凿总：行周而凿。"),
("輖","zhōu",F,"从車周聲：重也（《說文》「重也」），車重。","zh取凿总：車重而凿。"),
("鵃","zhōu",F,"从鳥舟聲：鶻鵃，鳥名（《說文》「鶻鵃也」），似山鵲而小。","zh取凿总：鳥小而凿。")]
rows=[]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"周部同取「刻畫、周匝、聚密」一面：琱治玉、錭治金、蜩蟬、惆失意、稠密、綢纏、裯被、調和、賙贍、週循環、輖車重、鵃鳥。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":603,"name":"周"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lzhou5-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第603部「周部」（卷一百 壽）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 603周部余12字")[-40:])
p2=ROOT+r"\intake\20261024-字卡603b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡603b{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡603b.json"); print(git("commit","-m","knowledge: 603周部余12条")[-40:])