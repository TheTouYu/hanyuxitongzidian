import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
F="【510 典部】典＝从冊从𠬞：冊指書簡，𠬞指兩手捧簡冊，象意有二——尊奉簡籍、捧冊頌讀。部內从典諸字取「厚重、豐滿、羞慚」三面。"
N="字形：古文字字形库未收。"
D=[("敟","diǎn","从攴典聲：主也、常也，為典之加攴分化字。","d「囤动」取「囤」：主而囤定。"),
("捵","chěn","从手典聲：伸也、扯也，取典之引申。","ch「刺持」取「持」：手扯而持。"),
("晪","tiǎn","从日典聲：明也（《集韻》「明也」）。","t「涂突」取「涂」：日明而涂。"),
("琠","tiǎn","从玉典聲：玉名；又通「瑱」，充耳之玉。","t取涂突：玉潤而涂。"),
("錪","tiǎn","从金典聲：小釜（《說文》「朝鮮謂釜曰錪」）。","t取涂突：釜受而涂。"),
("婰","diǎn","从女典聲：女子名用之字。","d取囤：女靜而囤。"),
("賟","tiǎn","从貝典聲：富也（《說文》「富也」）。","t取涂突：貝積而厚。"),
("㥏","tiǎn","从心典聲：慚愧（《說文》「青徐謂慙曰㥏」）。","t取涂突：心厚而慙。"),
("覥","tiǎn","从見典聲：面慚（「覥顏」），取㥏之慚義。","t取涂突：見人而慙。"),
("淟","tiǎn","从水典聲：「淟涊」，污濁（《說文》「垢濁也」）。","t取涂突：水濁而涂。"),
("唺","tiǎn","从口典聲：吞也、吐舌。","t取涂突：口吐而突。"),
("痶","tiǎn","从疒典聲：「痶瘓」，病貌。","t取涂突：病纏而弱。"),
("䠄","tiǎn","从足典聲：行跡、蹈也。","t取涂突：足蹈而突。"),
("碘","diǎn","从石典聲：化學元素，取典之聲（今字）。","d取囤：晶體囤聚。")]
cl=[]
for i,(ch,p,xp,sm) in enumerate(D,1):
    cl.append({"id":f"lcz-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）",
      "statement":f"{ch}字，音{p}，{xp}本部从典諸字同取厚重、豐滿、羞慚之一面，形符定其落點。",
      "boundary":"源自《系統漢語》第510部典部（卷八十三 鼎）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
json.dump({"schema_version":1,"intent":"字卡510c2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡510c.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡510c.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out, "cards:", len(cl))
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))