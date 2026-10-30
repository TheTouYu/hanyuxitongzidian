import json,subprocess,os,glob
B="源自《系統漢語》第386部「㡭部」；字卡五步规程。"
K="topic-zika-shizi"
rows=[
("𢷖","𢷖 duǎn／zhuǎn：从手，《廣韻》轉籰也、《集韻》轉也（一曰轉篗），收絲之器與動作，取「絲之連」。"),
("繼","繼 jì：从糸㡭，《說文》續也（古詣切），《玉篇》紹繼也、《爾雅》係繼也；系結，①接續組之正。"),
("蠿","蠿 zhuō：从䖵𢇍聲（𢇍古絕字，側八切），蠿蟊即作網蛛蟊；蜘蛛吐絲結網故从𢇍，取「繼」義。"),
("䠪","䠪 duàn／tuǎn：从足斷省聲，《說文》踐處也（徒管切），足跡，即腳印相續之意；《玉篇》行速也。"),
("𡣦","𡣦 jì：从女繼省聲，《漢典》對母親的俗稱；血脈相繼者為母。"),
("檵","檵 jì：从木繼省聲，《說文》枸杞也（古詣切），一曰堅木；枝條柔韌細長，砍柴時多作捆縛用，亦稱檵花紙末花。"),
("斷","斷 duàn：从斤从𢇍，𢇍古文絕，《說文》截也（徒玩切）；加斤即用斧砍斷，②截斷組之正。"),
("𩠹","𩠹 tuán：从𩠐从斷（大丸切），或从刀專聲，截斷；甲金文作以刀砍頭形，《廣韻》斷首。"),
("籪","籪 duàn：从竹斷聲，插在水裡捕魚蟹的竹柵欄，多以竹葦編成；以柵斷水道而取魚。"),
("䜝","䜝 tuǎn：从言，《集韻》𧨩䜝言惑，言不定；言語斷而不續。"),
("𠤉","𠤉 jué：《字彙補》古文絕字，記其為絕之古文。"),
("𢣎","𢣎 tuǎn：从心，《集韻》悿𢣎心惛；心緒斷而惛。"),
("𧓓","𧓓 jì：从虫繼省聲，《玉篇》𧓓蝧，蝧為蜂屬，約指細腰蜂——腰細如斷了一般，正見繼絕同形之理。"),
]
cl=[{"id":f"bp-{i:03d}","node":"hanzi-yinyuan","topic_id":K,"title":f"{ch}（字卡）","statement":st,
     "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"}
    for i,(ch,st) in enumerate(rows,1)]
json.dump({"schema_version":1,"intent":"字卡386㡭部2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡386㡭部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡386㡭部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    files=sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)
    b=os.path.basename(files[-1])[:-5]
    st=json.loads(run("bundle-status",b,"--format","json")); h=st["bundles"][0]["content_hash"]
    print(run("bundle-approve",b,"--apply","--content-hash",h)[:50].replace("\n"," "))
    print(run("bundle-apply",b,"--apply","--content-hash",h)[:50].replace("\n"," "))
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))