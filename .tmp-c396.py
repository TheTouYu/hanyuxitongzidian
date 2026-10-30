import json,subprocess,os,glob
B=("己（𢀒jǐ）：象磚石等壘疊所形成的縫隙形，表示累積、堆疊（《釋名》「紀也，皆有定形，可紀識也」）。轉義：相對的個體→自己本身；累疊之狀→傾覆崩塌（分化為圮）。"
   "字族衍義：①磚縫→堆疊、編結、接續；②形近「厶、尸、弓」之訛。")
D=[
("忋","gǎi","从心己聲，《玉篇》「恃也，仰也」——依靠、仰賴。","①組：與記紀等同取「接續」，以心定落點——心有所依。","g「隔估」取「估」：心依而估之。"),
("玘","qǐ","从玉己聲，《說文》「玉也」（去裡切），《廣韻》佩玉。","①組：玉成串相佩如己之相續。","q「親缺」取「親」：佩玉相親。"),
("芑","qǐ","从艸己聲，《說文》「白苗嘉榖」（驅裡切），疑因形近誤同「𦬊」；《爾雅》𦬊白苗，郭注今白粱粟；本指爬山虎之類攀牆植物。","①組：藤蔓攀牆、蔓延相接，正是「接續」在艸一面的落點。","q「親缺」取「親」：蔓附牆而親。"),
("邔","qǐ","从邑己聲，《說文》南陽縣（居擬切），今湖北宜城。","①組：地名只借聲，形符標邑里，不強講取義。","q「親缺」取「親」：邑聚而親。"),
("𢀵","hàn","从二己，《海篇》「音旱」——己的二迭，裂縫多之意；疑指乾旱（旱則地裂如己）。","①組之疊：己象磚縫，二己則縫多，故為旱裂。","h「豁活」取「豁」：地豁裂。"),
("𢀶","jì","从己，《字彙補》引《道書》「眞陽之炁曰𢀶龍」。","①組：道書用字，記其音義，不強解形。","j「聚決」取「聚」：眞陽之氣聚。"),
("𥫟","qǐ","从竹己聲，《集韻》「口已切，音起」——簟也（竹席）；《正字通》疑為譌字，然竹席織紋正作己狀。","①組之反證：織紋如己，是「己」本象編疊之形的旁證。","q「親缺」取「親」：篾條相親而織。"),
("𠮯","jǐ","从口己聲，《玉篇》「說也」，《集韻》「言也、平也」；《正字通》謂「台字之訛」。","②組：形近「台」之訛，記作讹變借形。","j「聚決」取「決」：言出而決。"),
("𩾠","yǐ","从鳥己聲，《玉篇》「居里切，音紀」，鳥名；《正字通》謂「鳲字之訛」——布穀鳥。","②組：形近鳲之訛，借形不取義。","y「延逾」取「延」：鳥鳴聲延。"),
("𣢇","hāi","从欠己聲，《玉篇》「笑不壞顏也」——微笑；《集韻》𣢑𣢑戲笑皃，或作咥；《正字通》謂即「弞」字之譌。","②組：形近弞之訛，記微笑一義而不強解己聲。","h「豁活」取「豁」：笑而氣豁。"),
]
def card(ch,p,a,b,c):
    return {"char":ch,"pinyin":p,"bus":[],"sections":[
      {"key":"bengen","label":"字根本義","text":B,"cites":[]},
      {"key":"zigen","label":"字形","text":"字形：古文字字形庫未收；原稿該條前後無獨立插圖。","cites":[]},
      {"key":"xingpang","label":"形旁声旁","text":a,"cites":[]},
      {"key":"hengxiang","label":"横向对照","text":b,"cites":[]},
      {"key":"shengmu","label":"声母义","text":c,"cites":[]}]}
for ch,p,a,b,c in D:
    json.dump(card(ch,p,a,b,c),open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("写卡",len(D))
# 忌支 10 条 Claim
DJ=[
("忌","由跪而畏而諱而止：己象跪時腿之相迭，心定其落點。"),
("跽","忌之本字加足，跪之形顯；《釋名》「見所敬忌，不敢自安也」。"),
("鵋","腿短身豎、狀如跪著，故以鳥定落點（鵋䳢即鵂鶹）。"),
("𠲹","跪在席上吃飯，以口定其落點。"),
("𡷞","山勢上聳而根腳蜷曲如跪者之股，以山定落點。"),
("𦮼","莖稈曲而下垂，通萁（豆莖禾稈可飼），以艸定落點。"),
("䋟","繩索交結成紐（秤紐），與己之編結相合，以糸定落點。"),
("誋","要對方跪著而告誡之，以言定落點。"),
("𡜱","與誋同取訓誡憤怒，以女定落點。"),
("𥭜","形近台之訛，記作讹變借形，不涉取義。"),
]
BK="源自《系統漢語》第389部「己部」忌支；字卡五步规程。"
cl=[{"id":f"bt4-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
     "statement":f"{d[0]}：{d[1]}", "boundary":BK,"permission":"public","fact_classes":["evidence_scope"],
     "duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(DJ,1)]
json.dump({"schema_version":1,"intent":"字卡389忌支2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡389忌支.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡389忌支.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))