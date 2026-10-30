import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FH="【第566部「尖部」】尖＝从小下大：上細小、下粗大，象錐形物（《玉篇》「小細也、銳也」）；引申在先、超出同類、刺入、聲音刺耳、靈敏刻薄；音借「韱」（鑯之俗）。"
N="字形：古文字字形库未收。"
D=[("尖","jiān",FH,"从小下大：象錐形（《玉篇》「銳也」），末銳也；引申先行、拔尖、刺入、尖刻。","j「聚决」取「聚」：銳聚而决。"),
("𧗰","gá",FH,"（尜）小兒戲物（《字彙補》），兩頭尖中間大之玩具。","g「隔估」取「隔」：兩尖而隔。"),
("𢬅","pū",FH,"古壯字，相當於「拔」（壯語借字）。","p「拼辟」取「拼」：手拔而拼。"),
("𥧤","níng",FH,"从宀？大也、明也（《玉篇》「大也。明也。」）。","n「纳弄」取「纳」：屋大而纳。"),
("𡙑","zhǐ",FH,"出《釋藏·疑字函》（《字彙補》），佛經譯字。","zh「凿总」取「凿」：字僻而凿。"),
("𣴒","tài",FH,"水沖洗（《字彙補》「音義與汏同」），或作汱，墜也、伏水也。","t「涂突」取「突」：水沖而突。"),
("𡙚","zài",FH,"武則天所制「載」字（《字彙補》），从大从車省。","z「凿总」取「总」：載聚而总。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"尖部未形成字族（原稿「未形成字族，不具備表音性」），所列皆零星俗字、借字、武周新字；只列同部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":566,"name":"尖"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ljian-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第566部「尖部」（卷九十二 辛）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡566a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡566a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡566a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))
import docx
f=sorted(glob.glob(r"D:\字谱智能体\卷九十三*.docx"))
print("vol93:",f)
if f:
    dd=docx.Document(f[0]); Q=[p.text.strip() for p in dd.paragraphs]
    import re
    print([ (i,p) for i,p in enumerate(Q) if re.match(r"^\d{3}\.",p)][:10])