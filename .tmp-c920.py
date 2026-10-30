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
F="【第602部「𠃬部」】𠃬＝从水流過上下兩口，象將水或水狀物灌注進口或口狀物裏：田疇（疇之初文）、敬酒（醻之初文）、鑄範注液（鑄之初文）三義；由倒酒敬神引申求告、叩擊，由鑄件經久引申長久。"
D=[("壽","shòu",F,"𠃬部字族：由鑄件經久耐用引申長久，《集韻》「乆也。古作𠷎」；壽命、壽考。","sh「失收」取「收」：久收而存。"),
("醻","chóu",F,"从酉𠷎聲：主人進客也（《說文》「主人進客也」），主客應酬，後作「酬」。","ch「刺持」取「持」：酒持而報。"),
("禱","dǎo",F,"从示壽聲：告事求福也（《說文》「告事求福也」），祈禱。","d「囤动」取「囤」：告聚而動。"),
("鑄","zhù",F,"从金壽聲：銷金也（《說文》「銷金也」），冶金寫之範中以為器，甲骨文本象捧熔液倒入範中。","zh「凿总」取「凿」：熔注而凿。"),
("濤","táo",F,"从水壽聲：大波也（《說文》「大波也」），波濤。","t「涂突」取「涂」：波大而突。"),
("幬","chóu",F,"从巾𠷎聲：禪帳也（《說文》「禪帳也」），單層帳幕；dào，覆也。","ch取刺持：帳垂而持。"),
("燾","dào",F,"从火壽聲：溥覆照也（《說文》「溥覆照也」），覆照、覆蓋。","d取囤动：火覆而動。"),
("儔","chóu",F,"从人壽聲：翳也（《說文》「翳也」），華蓋；伴侶、同輩。","ch取刺持：人聚而持。"),
("籌","chóu",F,"从竹壽聲：壺矢也（《說文》「壺矢也」），投壺之箭；籌碼、計謀。","ch取刺持：竹持而算。"),
("翿","dào",F,"从羽𣪐聲：翳也，所以舞也（《說文》），羽舞葬禮所用旌旗（羽葆幢）。","d取囤动：羽聚而動。"),
("薵","chóu",F,"从艸壽聲：薵藸，葱名（《集韻》）。","ch取刺持：草聚而持。"),
("疇","chóu",F,"从田壽聲：田疇，耕治之田（𠃬之初文，象田間溝畔形）。","ch取刺持：田分而持。")]
rows=[]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"𠃬部三面：注田疇（疇）、注酒敬客（醻/禱）、注範鑄器（鑄）；其餘取「久、覆、聚」：壽久、濤波、幬帳、燾覆、儔侶、籌箭、翿旗、薵葱。只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":602,"name":"𠃬"}],"sections":sec},open(rf"{ROOT}\web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append({"id":f"lzhou3-{len(rows)+1:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第602部「𠃬部」（卷一百 壽）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
git("add","web/public/cards"); print(git("commit","-m","cards: 602𠃬部12字")[-40:])
p2=ROOT+r"\intake\20261024-字卡602a.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡602a{it}-2026-10-24","risk":"low","claims":rows},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out: print("ok",len(rows)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",rows[idx]["title"]); rows.pop(idx)
bd=os.path.basename(sorted(glob.glob(ROOT+r"\data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",bd,"--format","json")).group(1)
print("bundle",bd); run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); print("err",json.loads(run("validate","--format","json")).get("errors"))
git("add","knowledge","data/knowledge","intake/20261024-字卡602a.json"); print(git("commit","-m","knowledge: 602𠃬部12条")[-40:])