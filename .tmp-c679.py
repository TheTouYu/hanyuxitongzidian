import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第533部「象部」】象＝象大象形（《說文》「南越大獸，長鼻牙，三年一乳」）；殷人曾馴象，象南遷而中原無象，故引申想象、形象、仿效（《正字通》「形象、肖似」）；音源字（源自象鳴）。字族：①象鼻 ②象身軀。"
N="字形：古文字字形库未收。"
D=[("象","xiàng",FY,"象大象形：长鼻牙、四足；引申想象、形象、仿效。","x「续消」取「续」：鼻卷而續。"),
("像","xiàng",FY,"从人从象：似也（《说文》「象也」），摹仿——象鼻看似鼻實則如手之靈。","x取续消：似而續。"),
("蟓","xiàng",FY,"从虫象聲：桑蠶（《玉篇》），吐絲擺動如象鼻。","x取续消：蠶擺而續。"),
("橡","xiàng",FY,"从木象聲：櫟實（《廣韻》），葉可飼柞蠶。","x取续消：實垂而續。"),
("嶑","xiàng",FY,"《集韻》音想，山名。","x取续消：山名而續。"),
("鱌","xiàng",FY,"《廣韻》魚名，似魟，白鼻長——如象鼻。","x取续消：魚鼻而續。"),
("鐌","xiàng",FY,"《玉篇》「鐌鼻，器飾」，器鈕；一曰錦名。","x取续消：器飾而續。"),
("潒","dàng",FY,"从水象聲：水潒瀁也（《說文》），水流搖動；又水大、水急。","d「囤动」取「囤」：水蕩而囤。"),
("襐","xiàng",FY,"从衣象聲：飾也（《說文》），寬大盛裝、未成年者首飾。","x取续消：衣飾而續。"),
("𩞧","shǎng",FY,"从食象聲：晝食也（《說文》），午飯即「餉」——象進食時間長。","sh「失收」取「收」：食而收。"),
("𢠽","dàng",FY,"从心象聲：放也（《說文》），放蕩。","d取囤动：心放而囤。"),
("勨","yǎng",FY,"从力象聲：繇緩也（《說文》），徭役寬緩；又勉也、動也。","y「柔锐」取「柔」：緩而柔。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"象系諧聲字分兩面：象鼻（像／蟓／鱌／鐌）與象身（襐／潒／𩞧／𢠽／勨）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":533,"name":"象"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiang5-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"字卡（第533部象）：{xp}",
 "boundary":"源自《系統漢語》第533部「象部」（卷八十九 象）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡533a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡533a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡533a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))