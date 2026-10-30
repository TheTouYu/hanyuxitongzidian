import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
B="源自《系統漢語》第523部「羊部」·養系（卷八十七 羊）；字卡五步规程。"
C=[("癢","yǎng","疒＋養。皮膚欲搔，取羊患疥癬、蹭樁牆之一面。"),
("𧓲","yǎng","虫＋養。蛘之或体，指叮咬致癢的蟎蝨一類小蟲。"),
("懩","yǎng","心＋養。心中有所欲求而騷動不定，取羊求牝之躁。"),
("攁","yǎng","手＋養。動手發動，取牧人驅羊之勢。"),
("瀁","yàng","水＋養。水漫無涯、蕩漾不定，取羊群散行之狀。"),
("𩜒","nǎng","食＋養。近在咫尺、忽然而見，取羊就近就食。"),
("𥶑","qiǎng","竹＋養。竹之一種，取羊角挺出之形。"),
("㔦","yǎng","力＋養。勸勉用力，取牧者呼羊使前。"),
("䑆","yǎng","肉＋養。胸中泛惡欲吐，取羊反芻上涌。"),
("鱶","xiǎng","魚＋養。剖而晾乾之魚腊，取羊腊同法。"),
("䭥","yàng","食＋養。糕餅之屬，取羊脂和麵。")]
cl=[{"id":f"ly3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{s}",
 "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,s) in enumerate(C,1)]
json.dump({"schema_version":1,"intent":"字卡養系补条2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡養系补.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
o=run("knowledge-plan","capture","--file",r"intake\20261023-字卡養系补.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in o)
if "PLAN_DUPLICATE" in o:
    import re as _re
    print(o[o.find("PLAN_DUPLICATE")-200:o.find("PLAN_DUPLICATE")+300])
else:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))