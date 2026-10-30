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
F="【第597部「用部」】用＝象蟲蛹形；庸、唐、康三支皆取「中空、外張」一面：唐从口庚聲表大言空大，康从庚从米表穀皮中空（糠），繭从糸表蠶所結之空殼。"
D=[("唐","táng",F,"从口庚聲：大言也（《說文》「大言也」），引申空大荒唐；借為朝代名。","t「涂突」取「涂」：言大而突。"),
("塘","táng",F,"从土唐聲：隄也（《說文》「隄也」），池塘、堤岸。","t取涂突：土隄而突。"),
("糖","táng",F,"从米唐聲：飴也（後起字），以米麥熬成之甘。","t取涂突：米甘而突。"),
("搪","táng",F,"从手唐聲：張也、抵也（《集韻》），搪塞、抵拒。","t取涂突：手張而突。"),
("螗","táng",F,"从虫唐聲：蜩螗，小蟬（《詩》「如蜩如螗」）。","t取涂突：蟬鳴而突。"),
("榶","táng",F,"从木唐聲：木名（《爾雅》「唐棣」亦作榶棣）。","t取涂突：木茂而突。"),
("康","kāng",F,"从庚从米：穀皮也（《說文》「穀皮也」），中空故安樂、康莊；轉義 健康、安寧。","k「口控」取「口」：空受而控。"),
("糠","kāng",F,"从米康聲：穀皮也（《說文》「穀皮也」），米糠。","k取口控：皮空而控。"),
("慷","kāng",F,"从心康聲：慷慨，激昂；心氣空大。","k取口控：心張而控。"),
("漮","kāng",F,"从水康聲：水虛也（《說文》「水虛也」），水空處。","k取口控：水空而控。"),
("繭","jiǎn",F,"从糸从虫：蠶衣也（《說文》「蠶衣也」），蠶所結之殼，中空而藏蛹。","j「聚决」取「聚」：絲聚而决。"),
("襺","jiǎn",F,"从衣繭聲：袍衣也（《說文》「袍衣也」），以絮充衣如繭。","j取聚决：衣裹而决。")]
rows=[]
for it in D:
    ch,p,F0,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"唐康繭三支同取「中空、外張」一面：唐大言、塘隄、糖飴、搪抵、螗小蟬、榶木；康穀皮空、糠米皮、慷心張、漮水虛、繭蠶衣、襺袍衣。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":597,"name":"用"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lyong3-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第597部「用部」（卷九十八 銿）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 597用部唐康繭支12字")[-60:])
p2=ROOT+r"\intake\20261024-字卡597c.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡597c{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡597c.json"); print(git("commit","-m","knowledge: 597用部唐康繭支12条")[-60:])