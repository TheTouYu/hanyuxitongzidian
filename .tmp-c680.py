import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第533部「象部」】象＝象大象形（《說文》「南越大獸，長鼻牙」）；引申想象、形象、仿效；音源字（源自象鳴）。字族：①象鼻 ②象身軀。"
FB="【第534部「爿部」】爿（片丬）＝象豎起的床形（長豎為床板、旁為床足），「牀」之初文（《說文》「安身之坐者」）；轉義床面由剖木鋪成→木片（分化作「片」，《廣韻》「析木也」）、剖開（《玉篇》「半也、判也」）。辯證：小篆形似「木」之半，故《說文》釋「片，判木也。从半木」不確。音源借音：古爿、相可通（《詩》「我倉既盈」一本作「箱」）。字族：①床或如床狀 ②剖木片狀。"
N="字形：古文字字形库未收。"
D=[("𩕓","yù",FY,"同「預」（《字彙》）。","y「柔锐」取「锐」：預先而銳。"),
("𨖶","xiàng",FY,"《集韻》「行也」。","x「续消」取「续」：行而續。"),
("𤩪","xiàng",FY,"𤩪柧，同「象觚」，象骨裝飾的酒器。","x取续消：骨飾而續。"),
("䴂","xiàng",FY,"䴂鵰，鸏䴀別名，即冠斑犀鳥（越王鳥）。","x取续消：鳥名而續。"),
("𢊔","lǔ",FY,"《海篇》「庵舍也」，疑㢚字之譌。","l「拢离」取「拢」：舍聚而攏。"),
("𦺨","xiàng",FY,"《玉篇》「草」，疑指橡實（櫟實）。","x取续消：草實而續。"),
("爿","chuáng",FB,"象竖起的床形，牀之初文；引申木片、剖开。","ch「刺持」取「持」：床立而持。"),
("牀","chuáng",FB,"从木爿聲：安身之坐者（《說文》），人所坐臥。","ch取刺持：床安而持。"),
("疒","nè",FB,"甲骨文从爿、人，後加點表血汗，人有病臥床不起。","n「纳弄」取「纳」：病臥而納。"),
("牕","chuāng",FB,"从穴爨（囪）聲：通孔也（《正韻》），窗有框櫺狀如床。","ch取刺持：窗框而持。"),
("戕","qiāng",FB,"从戈爿聲：殘也、殺也（《說文》）。","q「亲缺」取「亲」：刃親而缺。"),
("牄","qiāng",FB,"从倉爿聲：鳥獸來食聲（《說文》）；又空也。","q取亲缺：聲親而缺。")]
for ch,p,F0,xp,sm in D:
    bn=533 if ch in "𩕓𨖶𤩪䴂𢊔𦺨" else 534
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"象部餘字與爿系諧聲字分兩面：床或如床狀（爿／牀／疒／牕）與剖開片狀（戕／牄）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"象" if bn==533 else "爿"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lpanc-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"字卡（第533－534部）：{xp}",
 "boundary":"源自《系統漢語》第533－534部（卷八十九 象）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡534a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡534a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡534a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))