import json,subprocess,os,glob,re
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
N="字形：古文字字形库未收。"
F="【第592部「冬部」·亶族】亶＝蟺之初文：无鳞袒露、黏滑鑽洞、赤黄腥臊；本批取「黏稠、爬動難行」一面。"
D=[("蟺","shàn",F,"从虫亶聲：夗蟺也（《說文》），黃鱔（似蛇無鱗）；引申 蚯蚓、土蜂。","sh「失收」取「收」：蟲屈而收。"),
("饘","zhān",F,"从食亶聲：糜也（《說文》「糜也，周謂之饘，宋謂之餬」），稠粥。","zh「凿总」取「凿」：粥稠而凿。"),
("𧾍","zhān",F,"从走亶聲：趁也（《說文》「趁也」），行難、顫巍巍；又 移、趣。","zh取凿总：行難而凿。"),
("邅","zhān",F,"从辵亶聲：迍邅，難行不進皃（《集韻》）；又 轉、移。","zh取凿总：曲折而凿。"),
("驙","zhān",F,"从馬亶聲：駗驙也（《說文》引《易》「乘馬驙如」），馬負重行難；又 白馬黑脊。","zh取凿总：馬重而凿。"),
("鸇","zhān",F,"从鳥亶聲：鷐風也（《說文》），鷂鷹類猛禽，嚮風搖翅、疾擊燕雀。","zh取凿总：鳥擊而凿。"),
("䁴","zhǎn",F,"从目亶聲：視而止也（《說文》），看一下即止；又 視面色變。","zh取凿总：視止而凿。"),
("𨭖","zhǎn",F,"从金亶聲：伐擊也（《說文》「伐擊也」），割；齊謂相𥬸曰𨭖，即戰。","zh取凿总：擊而凿。"),
("䆄","zhǎn",F,"从禾亶聲：禾束（《廣韻》），束也。","zh取凿总：禾束而凿。"),
("儃","chán",F,"从人亶聲：儃何也（《說文》），徘徊不前；又 疾、態；通禪讓。","ch「刺持」取「持」：徘徊而持。"),
("𦒜","xiān",F,"从飛亶聲：飛皃（《玉篇》），𦒜翧，飛也。","x「续消」取「续」：飛而续。"),
("𤺺","dǎn",F,"从疒亶聲：風病（《集韻》），中風手足發顫；又 癬、疫。","d「囤动」取「囤」：病顫而囤。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"亶族取「黏稠、難行、顫動」一面：蟺黄鳝、饘稠粥、𧾍行難、邅迍邅、驙马重、鸇猛禽、䁴视止、𨭖伐击、䆄禾束、儃徘徊、𦒜飞、𤺺风病；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":592,"name":"冬"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"ldong8-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}·{p}","statement":f"{ch}：{xp}","boundary":"源自《系統漢語》第592部「冬部」（卷九十七 殸）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
p2=r"intake\20261024-字卡592h.json"
for it in range(10):
    json.dump({"schema_version":1,"intent":f"字卡592h{it}-2026-10-24","risk":"low","claims":cl},open(p2,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    out=run("knowledge-plan","capture","--file",p2,"--format","json")
    if "PLAN_DUPLICATE" not in out:
        print("ok claims",len(cl)); break
    idx=int(re.search(r"claims\[(\d+)\]",out).group(1)); print("drop",cl[idx]["title"]); cl.pop(idx)
bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))