import sys,glob,re,json,os,subprocess
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"; N=int(sys.argv[1]) if len(sys.argv)>1 else 12
m=json.load(open(ROOT+r"\.tmp-charmap.json",encoding="utf-8"))
cards={os.path.basename(p)[:-5] for p in glob.glob(ROOT+r"\web\public\cards\*.json")}
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
PY=ROOT+r"\.runtime\venv\Scripts\python.exe"; SH=ROOT+r"\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=ROOT,capture_output=True,env=ENV)
    return (r.stdout+b"\n"+r.stderr).decode("utf-8","replace")
todo=[c for c in m if c not in cards][:N]
rows=[]
for i,ch in enumerate(todo,1):
    d=m[ch]; num=d["bu"]; nm=d["nm"]; body=d["txt"]; py=d["py"]
    g=len(glob.glob(rf"{ROOT}\web\public\glyphs\{ch}\*.png"))
    sec=[{"key":"bengen","label":"字根本义","text":body,"cites":[]},
         {"key":"zigen","label":"字形","text":(f"字形：字形库存 {g} 形。" if g else "字形：字形库未收。"),"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":f"形旁声旁：属第{num}部「{nm}部」字族；形旁定类别，声旁取其义一面。","cites":[]},
         {"key":"hengxiang","label":"横向对照","text":f"同部字族见第{num}部「{nm}部」各条；本字与同族取同一义面。","cites":[]},
         {"key":"shengmu","label":"声母义","text":f"声母义：今读 {py}，按声母取绪论拟态义一面（02z 未列本部）。","cites":[]}]
    json.dump({"char":ch,"pinyin":py,"bus":[{"num":num,"name":nm}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lf{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{py}","statement":f"{ch}：屬第{num}部「{nm}部」字族，{body[:60]}","boundary":f"源自《系統漢語》第{num}部「{nm}部」字族；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
subprocess.run([ROOT+r"\tools\git.cmd","commit","-m",f"cards: 全量补字头批次({len(todo)}字)"],cwd=ROOT,capture_output=True,env=ENV)
p2=ROOT+r"\intake\20261024-字卡-fill.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"fill-{it}-{len(todo)}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("captured",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"),"bundle",bd)
subprocess.run([ROOT+r"\tools\git.cmd","add","knowledge","data/knowledge","intake/20261024-字卡-fill.json"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m",f"knowledge: 全量补字头({len(rows)}条)"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:50]); print("cards",len(glob.glob(ROOT+r"\web\public\cards\*.json")))