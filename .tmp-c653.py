import json,subprocess,os,glob,re,docx
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第524部「永部」】永、𠂢同源，从人从彳，象人行於道，表道路之遠；轉義分支（𠂢）。"
N="字形：古文字字形库未收。"
D=[("栐","yǒng",FY,"从木永聲：木可用為笏，記事之版（《玉篇》）。","y「圆容」取「圆」：木長而周。"),
("㭛","pài",FY,"从木𠂢聲：榺屬，一曰木皮，蜀人以為布（《集韻》）。","p「拼辟」取「拼」：皮析而拼。"),
("𥯠","pài",FY,"从竹𠂢聲：竹片也（《集韻》）。","p取拼辟：竹析而拼。"),
("𤖼","pò",FY,"从片𠂢聲：破物也、分也，通「劈」（《集韻》）。","p取拼辟：分而拼。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部取「分支分散」一面：栐（木）／㭛（木皮）／𥯠（竹片）／𤖼（破分），形符各定落點；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":524,"name":"永"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyong2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第524部「永部」（卷八十七 羊）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡524余2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡524余.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
o=run("knowledge-plan","capture","--file",r"intake\20261023-字卡524余.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in o)
if "PLAN_DUPLICATE" not in o:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
# scan 卷八十八
fs=[f for f in glob.glob(r"D:\字谱智能体\卷八十八*.docx")]
print("FILES",[os.path.basename(f) for f in fs])
for f in fs:
    ps=[p.text.strip() for p in docx.Document(f).paragraphs if p.text.strip()]
    print("== ",os.path.basename(f))
    for i,t in enumerate(ps):
        if re.match(r"^\d{2,3}\.",t): print(" HEAD",i,t[:40])
    for i,t in enumerate(ps):
        if t.startswith("本義") or t.startswith("字族衍義"): print(" P",i,t[:60])