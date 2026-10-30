import json,subprocess,os,glob,io
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
rows=[("痵","氣不定"),("悸","心動"),("㳵","水名"),("㻑","玉名存疑"),("鯚","鱖魚"),
("記","疏也記録"),("紀","絲別頭緒"),("杞","枸杞杞柳"),("屺","山無草木"),("圮","岸毀傾覆")]
BK=("源自《系統漢語》第388部「季部」；字卡五步规程。")
BJ=("源自《系統漢語》第389部「己部」；字卡五步规程。")
cl=[]
for i,(ch,g) in enumerate(rows,1):
    B=BK if i<=5 else BJ
    st=f"{ch}（{g}）：取部头「{'禾穗起伏不定' if i<=5 else '磚石壘疊接續'}」一面，形符定其落點——「{ch}」即由此分張；参见 `web/public/cards/{ch}.json`。"
    cl.append({"id":f"bt2-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡）",
      "statement":st,"boundary":B,"permission":"public","fact_classes":["evidence_scope"],
      "duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡388季支389己部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡389己部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡389己部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    f=sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1]
    b=os.path.basename(f)[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))
d=Document(r"D:\字谱智能体\第八章  子.docx"); ps=d.paragraphs
for i,p in enumerate(ps):
    if (p.text or "").strip().startswith("▲杞柳"):
        for j in range(max(0,i-4),i+1):
            for bl in ps[j]._p.findall('.//'+qn('a:blip')):
                rid=bl.get(qn('r:embed')); part=d.part.related_parts.get(rid)
                if part is None or not hasattr(part,'blob'): continue
                im=Image.open(io.BytesIO(part.blob)).convert("RGB")
                if max(im.size)<200: continue
                os.makedirs(r"web\public\glyphs\photos\杞",exist_ok=True)
                im.save(r"web\public\glyphs\photos\杞\01.jpg","JPEG",quality=90)
                print("photo 杞",im.size); raise SystemExit
print("no photo")