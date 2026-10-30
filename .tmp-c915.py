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
F="【第597部「用部」】用＝象蟲蛹形，蛹之初文；蛹中空而靜，引申施行使用、器物、平凡（平庸）、雇傭（蛹掛而不動故曰庸）；部內庚、庸、唐、康各支皆取「中空之器」一面。"
D=[("庚","gēng",F,"象有柄之鐘（甬鐘形），借為天干第七，又 更也（庚、更通）。","g「隔估」取「隔」：鐘懸而隔。"),
("賡","gēng",F,"从貝庚聲：續也（《說文》「續也」），賡續。","g取隔估：續而隔。"),
("鶊","gēng",F,"从鳥庚聲：鶬鶊，黃鳥（黃鸝）。","g取隔估：鳥鳴而隔。"),
("庸","yōng",F,"从庚从用：大鐘之用，引申 用也、常也（平庸）、雇也（庸保）。","y零聲母：用引而平。"),
("傭","yōng",F,"从人庸聲：均也、雇也（《說文》「均也」），傭工。","y零聲母：人雇而引。"),
("鏞","yōng",F,"从金庸聲：大鐘也（《說文》「大鐘」），懸於架。","y零聲母：金空而引。"),
("墉","yōng",F,"从土庸聲：城垣也（《說文》「城垣也」），高牆。","y零聲母：土圍而引。"),
("容","róng",F,"从宀从谷：容受也（《說文》「盛也」），容貌、容納。","r「柔銳」取「柔」：谷受而柔。"),
("熥","tōng",F,"从火甬聲：以火煖物也（《集韻》），烘烤、蒸。","t「涂突」取「涂」：火煖而突。"),
("埇","yǒng",F,"从土甬聲：地名，在淮泗；一曰道上加土（《集韻》）。","y零聲母：道土而引。"),
("恿","yǒng",F,"从心甬聲：勸也（《說文》「勸也」），慫恿。","y零聲母：心勸而引。"),
("悀","yǒng",F,"从心甬聲：怒也、滿也（《集韻》），心滿而出。","y零聲母：心滿而引。")]
rows=[]
for it in D:
    ch,p,F0,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"用部同取「中空、可容、可用」一面：庚鐘、賡續、鶊鳥、庸用常雇、傭均雇、鏞大鐘、墉城垣、容容受、熥火煖、埇加土、恿心勸、悀心滿；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":597,"name":"用"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lyong2-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第597部「用部」（卷九十八 銿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 597用部庚庸支12字")[-60:])
p2=ROOT+r"\intake\20261024-字卡597b.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡597b{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡597b.json"); print(git("commit","-m","knowledge: 597用部庚庸支12条")[-60:])