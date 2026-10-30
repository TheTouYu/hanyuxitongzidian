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
F1="【第598部「亢部」】亢＝象人頸之形，頸直而高；字族多取「高、直、空、乾」一面。"
F2="【第599部「且部」】且＝象俎（肉案）之形，《說文》「薦也」；引申陳列、將近、暫且，借音為語詞。"
D=[("坑","kēng",F1,"从土亢聲：壍也（《玉篇》「壍也」），坑陷、土坑；引伸坑害。","k「口控」取「控」：土陷而控。"),
("沆","hàng",F1,"从水亢聲：莽沆，大水也（《說文》）；沆瀣，清露之氣。","h「豁活」取「豁」：水大而豁。"),
("肮","āng",F1,"从肉亢聲：頸也（《廣韻》「頸也」）；又骯髒，高亢貶人。","k取口控：頸直而控。"),
("航","háng",F1,"从舟亢聲：船行（《廣韻》）。","h取豁活：舟行而豁。"),
("頏","háng",F1,"从頁亢聲：頡頏，鳥飛上下（《詩》「頡之頏之」）。","h取豁活：鳥上下而豁。"),
("炕","kàng",F1,"从火亢聲：乾也（《說文》「乾也」），以火乾物；北方臥具。","k取口控：火乾而控。"),
("且","qiě",F2,"象俎（肉案）之形：薦也（《說文》「薦也」），陳列祭肉之器；引申陳列、將近、暫且。","q「亲缺」取「亲」：陳肉而亲。"),
("祖","zǔ",F2,"从示且聲：始廟也（《說文》「始廟也」），祖廟、祖先。","z「凿总」取「凿」：祭始而凿。"),
("組","zǔ",F2,"从糸且聲：綬屬（《說文》「綬屬」），絲帶；組織、編組。","z取凿总：絲編而凿。"),
("租","zū",F2,"从禾且聲：田賦也（《說文》「田賦也」），地租、租借。","z取凿总：田賦而凿。"),
("粗","cū",F2,"从米且聲：疏也（《說文》「疏也」），粗疏、粗大。","c「刺持」取「刺」：米疏而刺。"),
("阻","zǔ",F2,"从阜且聲：險也（《說文》「險也」），阻隔、險阻。","z取凿总：阜險而凿。")]
rows=[]
for it in D:
    ch,p,F0,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    num=598 if F0==F1 else 599
    nm="亢" if num==598 else "且"
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"亢部取「頸直而高、空乾」：坑陷、沆水、肮頸、航行、頏飛、炕乾；且部取「陳列、薦祭」：且俎、祖廟、組絲、租賦、粗疏、阻險。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":num,"name":nm}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lkang2-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":f"源自《系統漢語》第{num}部「{nm}部」（卷九十八 銿／卷九十九 且）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 598尾+599且首12字")[-60:])
p2=ROOT+r"\intake\20261024-字卡599a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡599a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡599a.json"); print(git("commit","-m","knowledge: 598尾+599且首12条")[-60:])