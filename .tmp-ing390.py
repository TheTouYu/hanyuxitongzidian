import json,subprocess,os,glob,io
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
B="源自《系統漢語》第388部「子部」；字卡五步规程。"; K="topic-zika-shizi"
rows=[("字","字 zì：从子在宀下，子亦聲，《說文》乳也（疾置切）；生育孵化、女子許嫁曰字、文字者孳也六義相生無窮。"),
("牸","牸 zì：从牛字聲，《廣韻》牝牛（母牛）；《廣雅》雌也。"),
("芓","芓 zì／zǐ：从艸子聲，《說文》麻母也（疾吏切），麻子之母株；zǐ 通秄，壅禾本。"),
("秄","秄 zǐ／zì：从禾子聲，《說文》壅禾本（卽裡切），給禾麥根部培土；俗謂禾猥生曰秄。"),
("耔","耔 zǐ：从耒子聲，《廣韻》擁苗本也；《龍龕》擁苗器也。"),
("孳","孳 zī：从子茲聲，《說文》汲汲生也（子之切），生育繁殖；《廣韻》孳息、《廣雅》孿也。"),
("孜","孜 zī：从攴子聲，《說文》汲汲也，勤勉不殆；《周書》「孜孜無怠」。"),
("李","李 lǐ：从木子聲，《說文》果也；味酸而孕婦喜食，喜食李意味著有子，與梅同例，或為婚育之神靈。"),
("汓","汓 qiú／yóu：从水从子，《說文》浮行水上也（似由切），嬰兒能浮於水；亦作泅、遊。"),
("籽","籽 zǐ：从米子聲，某些植物的種子；果中有子，與字之生殖同源。"),
("孖","孖 zī／mā：从二子，《廣韻》雙生子也；《玉篇》亦作滋、蕃長也，相連成對。"),
("吇","吇 zǐ／jí：从口子聲，《集韻》吇吇鳥聲；《正字通》又與唧通。")]
cl=[{"id":f"bt-{i:03d}","node":"hanzi-yinyuan","topic_id":K,"title":f"{ch}（字卡）","statement":st,
     "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"}
    for i,(ch,st) in enumerate(rows,1)]
json.dump({"schema_version":1,"intent":"字卡388子部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡388子部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡388子部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    files=sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)
    b=os.path.basename(files[-1])[:-5]
    st=json.loads(run("bundle-status",b,"--format","json")); h=st["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))
# photo: 彩瓷繈褓俑
d=Document(r"D:\字谱智能体\第八章  子.docx"); ps=d.paragraphs
txt=[(p.text or "").strip() for p in ps]
for i,t in enumerate(txt):
    if t.startswith("▲") and "繈褓" in t:
        for j in range(max(0,i-4),i+1):
            for bl in ps[j]._p.findall('.//'+qn('a:blip')):
                rid=bl.get(qn('r:embed')); part=d.part.related_parts.get(rid)
                if part is None or not hasattr(part,'blob'): continue
                im=Image.open(io.BytesIO(part.blob)).convert("RGB")
                if max(im.size)<200: continue
                os.makedirs(r"web\public\glyphs\photos\子",exist_ok=True)
                im.save(r"web\public\glyphs\photos\子\01.jpg","JPEG",quality=90)
                print("photo 子 p",j,im.size); raise SystemExit
print("no photo")