import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FY="【第525部「昜部」】昜＝从日从丂（脖頸象形），象對日呼號、日出；轉義飛舉、乾旱；音源本丂聲。字族三面：日烈／日出／日升。"
N="字形：古文字字形库未收。"
D=[("鐊","yáng",FY,"从金陽聲：馬頭飾（《說文》引《詩》「鉤膺鏤鐊」），經典作「鍚」。","y「圆容」取「圆」：飾馬而周。"),
("畼","chàng",FY,"从田昜聲：不生也、田不耕（《說文》），借為通畼。","ch「刺持」取「持」：田蕪而持。"),
("𥏫","shāng",FY,"从矢昜聲：傷也，箭傷（《說文》）。","sh「失收」取「失」：矢中而失。"),
("慯","shāng",FY,"从心殤省聲：憂也、念也（《說文》）。","sh取失收：心傷而失。"),
("䵮","yàng",FY,"从黑昜聲：赤黑色（《說文》讀若煬）。","y取圆容：色深而渾。"),
("鰑","yáng",FY,"从魚昜聲：鮦也、赤鱺，俗名烏魚（《博雅》）。","y取圆容：魚黑而圓。"),
("煬","yàng",FY,"从火昜聲：炙燥、烘烤（《說文》）；向火、熔化。","y取圆容：火炙而周。"),
("鬺","shāng",FY,"从鬲昜聲：煮也（《說文》），或作䵼。","sh取失收：鼎煮而熟。"),
("餳","xíng",FY,"从食昜聲：飴和饊，糯米熬成之糖（《玉篇》）。","x「续消」取「续」：糖黏而續。"),
("璗","dàng",FY,"从玉湯聲：金之美者，與玉同色（《說文》）。","d「囤动」取「囤」：金聚而色。"),
("崵","yáng",FY,"从山昜聲：崵山在遼西，一曰嵎銕崵谷（《說文》）。","y取圆容：山高而周。"),
("霷","yáng",FY,"从雨昜聲：十月為霷，通作陽（《集韻》）。","y取圆容：雨霽而明。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同部諧聲字分三面：日烈（畼／𥏫／慯）、日出灼熱（鐊／䵮／鰑／煬／鬺／餳）、日升光明（璗／崵／霷）；只列本部字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":525,"name":"昜"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lyang4-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第525部「昜部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡525b2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡525b.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡525b.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))