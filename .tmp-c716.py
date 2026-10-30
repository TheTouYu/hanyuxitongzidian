import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第543部「玉部」】玉＝象玉串形，《說文》「石之美」。"
FL="【第544部「老部」】老＝甲骨文象人長髮拄杖之形，七十曰老（《說文》「考也，七十曰老」）；轉義年長、衰暮、久舊；音源借音（老、考同源互通）。"
N="字形：古文字字形库未收。"
D=[("瓄","dú",FY,"从玉賣聲：玉名（《集韻》）。","d「囤动」取「囤」：玉實而囤。"),
("璪","zǎo",FY,"从玉澡聲：玉飾如水藻之文（《說文》「玉飾如水藻之文」）。","z「凿总」取「凿」：藻紋而凿。"),
("璫","dāng",FY,"从玉當聲：耳珠也（《說文》「華飾也」），今婦人耳飾。","d取囤动：垂耳而囤。"),
("璵","yú",FY,"从玉與聲：璵璠，魯寶玉（《說文》）。","y「柔锐」取「锐」：寶玉而锐。"),
("老","lǎo",FL,"象人长发拄杖，七十曰老；引申年长、衰暮、久旧。","l「拢离」取「拢」：齿聚而离。"),
("考","kǎo",FL,"从老省从丂：老也（《說文》「老也」），父考、考核（借义）。","k「口控」取「控」：杖控而考。"),
("孝","xiào",FL,"从老省从子：善事父母者（《說文》「善事父母者」）。","x「续消」取「续」：事亲而續。"),
("耆","qí",FL,"从老省旨聲：老也（《說文》「老也」），六十曰耆。","q「亲缺」取「亲」：老亲而缺。"),
("耄","mào",FL,"从老省毛聲：年九十曰耄（《說文》「年九十曰耄」）。","m「蒙末」取「末」：老末而蒙。"),
("耋","dié",FL,"从老省至聲：年八十曰耋（《說文》「年八十曰耋」）。","d取囤动：老至而囤。"),
("耇","gǒu",FL,"从老省句聲：老人面凍黎若垢（《說文》），壽耇。","g「隔估」取「隔」：面垢而隔。")]
for ch,p,F0,xp,sm in D:
    bn=543 if ch in "瓄璪璫璵" else 544
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"玉系余字言玉飾（瓄名、璪藻紋、璫耳珠、璵寶玉）；老系同取「老而持杖」一面（考父、孝事亲、耆耄耋以年數分）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":bn,"name":"玉" if bn==543 else "老"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"llao-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第543－544部（卷九十 秋）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡544a2026-10-24","risk":"low","claims":cl},open(r"intake\20261024-字卡544a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261024-字卡544a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))