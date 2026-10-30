import json,subprocess,os,glob
BA="源自《系統漢語》第387部「𢆶部」；字卡五步规程。"
BB="源自《系統漢語》第387部「幽部」；字卡五步规程。"
K="topic-zika-shizi"
rows=[
("𨓁",BA,"𨓁 běng：从辵，《玉篇》出也、《集韻》行急也；言快如抽絲意。"),
("𢆸",BA,"𢆸 bēng：从糸，《集韻》悲萌切音繃，繩以直物，通作絣；言絲之用意。"),
("𪀨",BA,"𪀨 yā：《字彙補》音義與鴉同；言其羽黑，取絲的幽微不明意。"),
("幽",BB,"幽 yōu：甲骨文从火𢆶聲，象火光細微，昏暗不明；轉義深遠、微弱、隱匿、黑色；西周訛从山，故《說文》从山中𢆶析形不確。"),
("𧍘",BB,"𧍘 yōu：从虫幽聲，《說文》𧍘蟉也（於虯切），蟲類宛轉曲折之皃；一曰蚴蟉龍皃。"),
("㗀",BB,"㗀 yōu：《篇海》音幽，鹿鳴也；又咿㗀，吟聲。"),
("𡺖",BB,"𡺖 yōu：《五侯鯖字海·山部》山深沓也；與幽同取深而幽暗。"),
("𩡎",BB,"𩡎 xiū：《字彙補》香幽切音休，香氣也；以香之幽微定落點。"),
("䫜",BB,"䫜 āo：从頁，《玉篇》頭凹也、《集韻》大首深目皃；以頭面之深凹定落點。"),
("𪋎",BB,"𪋎 yōu：《玉篇》古文麀字，母鹿；無角所以不顯，正取幽之隱而不顯。"),
("𥠃",BB,"𥠃 jiū：《字彙》禾初生也、《集韻》稵禾生也或从幽；禾初生細微。"),
("𩘈",BB,"𩘈 yōu：《集韻》於虯切音幽，風聲；以風聲之幽微定落點。"),
]
cl=[{"id":f"bq-{i:03d}","node":"hanzi-yinyuan","topic_id":K,"title":f"{ch}（字卡）","statement":st,
     "boundary":b,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"}
    for i,(ch,b,st) in enumerate(rows,1)]
json.dump({"schema_version":1,"intent":"字卡387𢆶幽2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡387𢆶幽.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡387𢆶幽.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    files=sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)
    b=os.path.basename(files[-1])[:-5]
    st=json.loads(run("bundle-status",b,"--format","json")); h=st["bundles"][0]["content_hash"]
    print(run("bundle-approve",b,"--apply","--content-hash",h)[:40].replace("\n"," "))
    print(run("bundle-apply",b,"--apply","--content-hash",h)[:40].replace("\n"," "))
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))