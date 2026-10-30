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
OLD="休系同取「依木而息、蔭庇」一面（茠除草、庥庇、髹漆、貅獸）；臼系言坎穴舂米（臼、齨）；只列同族字。"
NEW="休系分兩面：茠除草、庥庇、貅獸取「依木而息、蔭庇」；髹從休借聲、義取漆飾，與休本義無涉。臼系言坎穴舂米（臼、齨）。只列同族字。"
n=0
for ch in "休茠鵂貅庥髹咻烋恘銝臼齨":
    fp=rf"{ROOT}\web\public\cards\{ch}.json"
    if not os.path.exists(fp): continue
    d=json.load(open(fp,encoding="utf-8"))
    for s in d["sections"]:
        if s["text"]==OLD: s["text"]=NEW; n+=1
    json.dump(d,open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cards fixed",n)
git("add","web/public/cards"); print(git("commit","-m","cards: 休部髹改借声措辞")[-40:])
N="字形：古文字字形库未收。"
F2="【第599部「且部」】且＝象俎（肉案）之形，《說文》「薦也」；引申陳列、將近、暫且。"
F3="【第600部「巨部」】巨＝象矩（工字尺）之形，量方形之器；引申大、巨大，借為「詎」。"
D=[("詛","zǔ",F2,"从言且聲：詶也（《說文》「詶也」），詛咒。","z「凿总」取「凿」：言誓而凿。"),
("砠","jū",F2,"从石且聲：石戴土也（《說文》「石戴土也」）。","j「聚决」取「聚」：石聚而决。"),
("蛆","qū",F2,"从虫且聲：蠅之子（《玉篇》），蠅蛆。","q「亲缺」取「亲」：蟲亲而缺。"),
("沮","jǔ",F2,"从水且聲：止也（《說文》「止也」），沮止、沮喪。","j取聚决：水聚而决。"),
("咀","jǔ",F2,"从口且聲：含味也（《說文》「含味也」），咀嚼。","j取聚决：口聚而决。"),
("苴","jū",F2,"从艸且聲：履中艸（《說文》「履中艸」），包裹、麻之有子者。","j取聚决：草聚而决。"),
("殂","cū",F2,"从歺且聲：往死也（《說文》「往死也」），崩殂。","c「刺持」取「刺」：歺刺而持。"),
("罝","jū",F2,"从网且聲：兔网也（《說文》「兔网也」）。","j取聚决：网聚而决。"),
("巨","jù",F3,"象矩之形：規巨也（《說文》「規巨也」），工字尺；引申大。","j取聚决：矩聚而决。"),
("矩","jǔ",F3,"从矢巨聲：規矩（《說文》引「規巨」），法度。","j取聚决：度聚而决。"),
("拒","jù",F3,"从手巨聲：拒也（《說文》「拒也」），抵拒。","j取聚决：手聚而决。"),
("距","jù",F3,"从足巨聲：雞距也（《說文》「雞距也」），距離。","j取聚决：足聚而决。")]
rows=[]
for it in D:
    ch,p,F0,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    num=599 if F0==F2 else 600
    nm="且" if num==599 else "巨"
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"且部取「俎案、陳列、薦祭」：詛言、砠石、蛆蠅、沮止、咀含、苴草、殂死、罝網；巨部取「矩尺量方」：巨矩、矩度、拒抵、距雞。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":nm}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lju-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":f"源自《系統漢語》第{num}部「{nm}部」（卷九十九 且／卷一百 巨）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 599且余+600巨首12字")[-60:])
p2=ROOT+r"\intake\20261024-字卡600a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡600a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡600a.json"); print(git("commit","-m","knowledge: 599余+600巨首12条")[-60:])