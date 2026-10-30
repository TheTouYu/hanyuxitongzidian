import json,subprocess,os,glob,re
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
F="【第594部「彡部」】彡＝三丿，象細長而多之物；參（三）＝三根算籌並列，引申相參、眾多、細密，為本部二級字根。"
D=[("槮","shēn",F,"从木參聲：木長皃（《說文》「木長皃」）；又 積柴水中取魚（罧）。","sh「失收」取「收」：木長而收。"),
("糝","sǎn",F,"从米參聲：以米和羹也（《說文》），米粒、飯粒。","s取失收：米粒而收。"),
("滲","shèn",F,"从水參聲：下漉也（《說文》「下漉也」），水滲透。","sh取失收：水下而收。"),
("黲","cǎn",F,"从黑參聲：淺青黑色（《說文》「淺青黑也」），黯暗。","c「刺持」取「持」：色暗而持。"),
("慘","cǎn",F,"从心參聲：毒也（《說文》「毒也」），慘毒、悲慘。","c取刺持：心毒而持。"),
("謲","cǎn",F,"从言參聲：相怒也（《說文》），言語相責。","c取刺持：言責而持。"),
("墋","chěn",F,"从土參聲：土也（《說文》「土也」），沙土。","ch取刺持：土雜而持。"),
("磣","chěn",F,"从石參聲：食有沙（《集韻》），牙磣。","ch取刺持：沙礫而持。"),
("醦","chěn",F,"从酉參聲：酢也（《集韻》），酸味。","ch取刺持：味酸而持。"),
("鏒","sǎn",F,"从金參聲：金鏒（《集韻》），金器細碎。","s取失收：金碎而收。"),
("驂","cān",F,"从馬參聲：駕三馬也（《說文》「駕三馬也」），驂乘。","c取刺持：三馬而持。"),
("篸","zān",F,"从竹參聲：綴衣針（《說文》「差也」一曰針），簪之初文。","z「凿总」取「凿」：針細而凿。")]
rows=[]
for it in D:
    ch,p,F0,xp,sm=it[0],it[1],it[2],it[3],it[-1]
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"參系同取「細密、相參」一面：槮木長、糝米粒、滲下漉、黲淺黑、慘毒、謲相怒、墋沙土、磣牙磣、醦酸、鏒金碎、驂三馬、篸綴針；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":594,"name":"彡"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lshan3-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第594部「彡部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 594彡部參族12字")[-70:])
p2=ROOT+r"\intake\20261024-字卡594c.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡594c{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡594c.json"); print(git("commit","-m","knowledge: 594彡部參族12条")[-70:])