import json,subprocess,os,glob,io
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
B="源自《系統漢語》第387部「幾部」；字卡五步规程。"
K="topic-zika-shizi"
rows=[
("幾","幾 jī／jǐ：部頭从戍𢆶聲，象意細微卻十分重要的事物，表要害關鍵（《法言》「為政有幾」李軌注「幾，要也」）；引申跡象、危機、近、幾何。"),
("機","機 jī：从木幾聲，《說文》主發謂之機（居衣切）；樞機戶軸、機杼織具、桔槔、弩牙、變化關鍵。"),
("鐖","鐖 jī／qí：从金，《玉篇》鉤逆鋩（鉤上倒刺、弩之扣手）；qí 又大鐮；原稿配大河村骨魚鉤圖。"),
("磯","磯 jī：从石幾聲，《說文》大石激水也；水中磧、露出水面的岩石灘，引申激怒觸犯。"),
("譏","譏 jī：从言幾聲，《說文》誹也，隱晦的批評——微言而大義；《廣雅》譴也諫也問也。"),
("饑","饑 jī：从食幾聲，《說文》穀不孰為饑，五穀不熟食物缺乏；飢則為餓。"),
("鞿","鞿 jī：从革幾聲，《玉篇》韁在口（馬嚼子）；《集韻》馬絡頭，牽制束縛之意。"),
("蟣","蟣 jǐ／qí：从虫幾聲，《說文》蝨子也（蝨卵）；一曰齊謂蛭曰蟣（螞蟥）。"),
("璣","璣 jī：从玉幾聲，《說文》珠不圜也（小珠）；《正字通》渾天儀「璣為轉運」；亦北斗第三星。"),
("畿","畿 jī：从田幾省聲，《說文》天子千里地；《增韻》門限，引申疆域界限。"),
("禨","禨 jī／jì：从示幾聲，《集韻》祥也祅祥也，祭鬼神以求福；《正字通》祟也；jì 沐酒。"),
("穖","穖 jǐ／jì：从禾幾聲，《說文》禾穖也，禾穗子實如成串珠璣；jì 稠也。"),
]
cl=[{"id":f"br-{i:03d}","node":"hanzi-yinyuan","topic_id":K,"title":f"{ch}（字卡）","statement":st,
     "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"}
    for i,(ch,st) in enumerate(rows,1)]
json.dump({"schema_version":1,"intent":"字卡387幾部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡387幾部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡387幾部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    files=sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)
    b=os.path.basename(files[-1])[:-5]
    st=json.loads(run("bundle-status",b,"--format","json")); h=st["bundles"][0]["content_hash"]
    print(run("bundle-approve",b,"--apply","--content-hash",h)[:40].replace("\n"," "))
    print(run("bundle-apply",b,"--apply","--content-hash",h)[:40].replace("\n"," "))
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))
# photos
d=Document(r"D:\字谱智能体\第八章  子.docx"); ps=d.paragraphs
for idx,ch in [(190,"鐖"),(201,"璣")]:
    for b_ in ps[idx]._p.findall('.//'+qn('a:blip')):
        rid=b_.get(qn('r:embed')); part=d.part.related_parts.get(rid)
        if part is None or not hasattr(part,'blob'): continue
        im=Image.open(io.BytesIO(part.blob)).convert("RGB")
        os.makedirs(rf"web\public\glyphs\photos\{ch}",exist_ok=True)
        im.save(rf"web\public\glyphs\photos\{ch}\01.jpg","JPEG",quality=90)
        print("photo",ch,im.size)