import json,subprocess,os,glob
F="【439 扁部】扁＝从戶从冊，象意门牌（户籍册与门户对应），本义「署门牌」；轉義四路：不圆→扁平，薄小→轻便，户户皆有→普遍，区分门户→分别排列。音源：本「冊」聲，因有别义音同「辡」。"
N="字形：古文字字形库未收。"
D=[("扁","biǎn",F,"《说文》「署也。从戶、冊。戶冊者，署門戶之文也」——门牌；引申扁平、狭小、普遍、分别。","b「闭剥」取「剥」：门牌分户而别。"),
("編","biān",F,"《说文》「次簡也，从糸扁聲」——依次编联竹简；引申编织、编辑、连接。","b取剥：丝分而编。"),
("篇","piān",F,"《说文》「書也，一曰關西謂榜曰篇」——首尾完整的诗文、书册。","p「拼辟」取「辟」：竹简排比。"),
("㾫","piān",F,"《说文》「半枯也」——半身不遂，赤脉起如编绳。","p取辟：血脉偏分。"),
("𤻶","biàn",F,"《集韵》「骨風病也」——骨节肿大如结。","b取剥：骨结而分。"),
("㲢","biàn",F,"《玉篇》「㲢㲫，毛𣬹也」——毛纠结如编织状。","b取剥：毛纠而分。"),
("斒","bān",F,"《集韵》「斒斕，色不純也」——色彩驳杂。","b取剥：色杂而分。"),
("𩩯","biàn",F,"《玉篇》「骨𩩯生皃」——骨生不齐之貌。","b取剥：骨分而歧。"),
("匾","biǎn",F,"《廣韻》「匾㔸，薄也」；《正字通》「俗扁字」——薄而浅的容器；匾额。","b取剥：器薄而分。"),
("牑","biān",F,"《说文》「床版也，从片扁聲，讀若邊」——床板。","b取剥：板分而铺。"),
("楄","pián",F,"《说文》「楄部，方木也」——方木；《廣韻》「木名，食不噎」。","p取辟：木方而分。"),
("藊","biǎn",F,"《集韻》「豆名」；《本草》「藊本作扁，莢形扁也」——扁豆。","b取剥：荚扁而分。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"同取扁部「门牌分户／扁平」一面，形符各定落点；故声符给义、形符定落点。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lbq-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}，{p}：{xp}",
"boundary":"源自《系統漢語》第439部「扁部」（卷七十三 釆）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡439c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡439c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡439c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))