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
F="【第605部「鳥部」】鳥＝象體形較大之鳥形，飛禽總名（《玉篇》「飛禽緫名也」）；字族多取鳥之鳴聲、羽色、猛鷙一面。"
D=[("鳥","niǎo",F,"象鳥形：飛禽緫名也（《玉篇》），長尾禽總名。","n「纳弄」取「纳」：羽纳而弄。"),
("梟","xiāo",F,"从鳥在木上：不孝鳥也（《說文》「不孝鳥也」），食母；惡聲之鳥。","x「续消」取「续」：惡鳴而消。"),
("鳴","míng",F,"从口从鳥：鳥聲也（《說文》「鳥聲也」），鳥叫、鳴響。","m「蒙末」取「蒙」：聲蒙而出。"),
("鶉","chún",F,"从鳥享聲：鷯鶉也（《說文》），鵪鶉。","ch「刺持」取「持」：鳥持而聚。"),
("鳳","fèng",F,"从鳥凡聲：神鳥也（《說文》「神鳥也」），鳳凰。","f「附分」取「附」：羽附而分。"),
("鶴","hè",F,"从鳥隺聲：鶴，長頸高足之鳥。","h「豁活」取「豁」：頸長而豁。"),
("鵲","què",F,"从鳥昔聲：喜鵲，知來之鳥。","q「亲缺」取「亲」：鳥亲而缺。"),
("鴉","yā",F,"从鳥牙聲：烏鴉，純黑之鳥。","y 零聲母借聲。"),
("鷗","ōu",F,"从鳥區聲：海鷗，水鳥。","零聲母借聲：鷗泛水。"),
("鷹","yīng",F,"从鳥从人：鷹隼，猛鷙之鳥。","零聲母借聲：鷹擊。"),
("鴟","chī",F,"从鳥氐聲：鴟鴞，鴟鴞惡鳥。","ch取刺持：爪持而刺。"),
("鴦","yāng",F,"从鳥央聲：鴛鴦，匹鳥。","零聲母借聲：鴦成雙。")]
rows=[]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"鳥部同取「飛禽之形、鳴聲、羽色」一面：鳥總名、梟惡鳴、鳴鳥聲、鶉鵪鶉、鳳神鳥、鶴長頸、鵲知來、鴉純黑、鷗水鳥、鷹猛鷙、鴟惡鳥、鴦匹鳥。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":605,"name":"鳥"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lniao-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第605部「鳥部」（卷一百 壽）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 605鳥部12字")[-40:])
p2=ROOT+r"\intake\20261024-字卡605a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡605a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡605a.json"); print(git("commit","-m","knowledge: 605鳥部12条")[-40:])