import json,subprocess,os,glob
B="源自《系統漢語》第385部「㬎部」；字卡五步规程。"
K="topic-zika-shizi"
rows=[
("濕","濕 tà／shī／xí：从水㬎聲，本指水名（今山東徒駭河，他合切），經典借為「溼」水霑也；又「濕濕」牛呞動耳皃。"),
("隰","隰 xí：从𨸏㬎聲，阪下濕也（似入切），山坡下低濕之地；xiè 又為人名。"),
("㙷","㙷 zhí：从土㬎聲，《說文》下入也（敕立切），低窪地；《玉篇》墊也、田塍埓，《類篇》累土。"),
("灦","灦 xiǎn：从水，《玉篇》水也，《集韻》灦渙水皃、水澄深也。"),
("㬤","㬤 qī：从日㬎聲，《玉篇》欲乾也、《廣韻》欲燥、《集韻》曝也，或作𣉓；此為部頭「日曬漂白」之直證。"),
("顯","顯 xiǎn：从頁㬎聲，《說文》頭明飾也（呼典切）；《玉篇》光也、見也、明也、著也，明著於面。"),
("𩎍","𩎍 xiǎn：从革顯聲，《說文》著掖鞥也；《釋名》「韅，經也，橫經其腹下也」，即附著馬兩腋的皮革件。"),
("䗾","䗾 xiàn：从虫顯聲（呼典切音顯），縊女也；郭璞云小黑蟲赤頭，喜自縊死，即吐絲自懸的蝶類幼蟲。"),
("𢷑","𢷑 xiǎn／zhěn：从手，《玉篇》戾也；《集韻》抮偝也或作𢷑；zhěn 引戾也、牽引。"),
("儑","儑 án／àn：从人㬎聲，《玉篇》不慧也、灰心喪氣；《集韻》傝儑不自安、無儀檢；《字彙》謔言。"),
("䏉","䏉 shī：从耳，《玉篇》耳動搖之皃；《集韻》牛耳動皃。"),
("礘","礘 è／qì：从石㬎聲，《廣韻》動礘礘；《集韻》礘礘石皃，或作硆砐；qì 砬礘石聲。"),
("䝃","䝃 zhé：从豆，《集韻》豆也；㬎部旁支，以豆定其類。"),
]
cl=[{"id":f"bo-{i:03d}","node":"hanzi-yinyuan","topic_id":K,"title":f"{ch}（字卡）","statement":st,
     "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"}
    for i,(ch,st) in enumerate(rows,1)]
json.dump({"schema_version":1,"intent":"字卡385㬎部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡385㬎部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡385㬎部.json","--format","json")
print("cap:", "PLAN_DUPLICATE" in out, out[-90:].replace("\n"," "))
if "PLAN_DUPLICATE" not in out:
    files=sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)
    b=os.path.basename(files[-1])[:-5]
    st=json.loads(run("bundle-status",b,"--format","json")); h=st["bundles"][0]["content_hash"]
    print(run("bundle-approve",b,"--apply","--content-hash",h)[:60].replace("\n"," "))
    print(run("bundle-apply",b,"--apply","--content-hash",h)[:60].replace("\n"," "))
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"errors",v.get("errors"))