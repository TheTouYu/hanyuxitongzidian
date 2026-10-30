import json, subprocess, os, re
ROOT=r"D:\系统汉字"; PY=os.path.join(ROOT,".runtime","venv","Scripts","python.exe")
PKC=[PY, os.path.join(ROOT,"tools","pkc_tmpfix.py")]
ENV=os.environ.copy(); ENV["PATH"]=os.path.join(ROOT,".runtime","mingit","cmd")+os.pathsep+ENV.get("PATH","")
def run(a):
    p=subprocess.run(PKC+a,cwd=ROOT,capture_output=True,text=True,encoding="utf-8",env=ENV); return p.returncode,p.stdout+p.stderr
BEN="劦部部头象三人并耒而耕，取并排同时用力之象；脅（肋）一支由「肋骨并列如耒之成排」而来，故其族多取夹持、翕动、逼迫。"
rows=[("珕","lì","珕从玉劦聲（《說文》「蜃屬」，《禮》「士珕琫而珧珌」），蚌蛤之属，古以贝壳饰刀鞘。","玉、蜃、飾","壳纹层叠如耒成排，取「并列」一面。"),
("栛","lì","栛从木劦聲，《玉篇》「果似枇杷子」，《廣韻》「小槤，木名」。","木、果、槤","果实成串并生，取「并列」一面。"),
("荔","lì","荔从艸劦聲（《說文》「艸也，似蒲而小，根可作㕞」），即马蔺，根须长硬可制刷；又「茘支」荔枝。","艸、根、耒","根须成排如耒，取「并列」一面。"),
("脅","xié","脅从肉劦聲（《說文》「兩𦜶也」），肋骨、两膀；引申挟持逼迫、恐惧、翕动。","肉、肋、夾","肋骨成排夹身，取「并列夹持」一面。"),
("愶","xié","愶从心脅聲，《廣韻》「以威力相恐也」，威胁；亦训胆怯。","心、恐、怯","被挟而心惧，取「逼迫」一面。"),
("熁","xié","熁从火脅聲，《廣韻》「火氣熁上」，《集韻》「火迫也、火乾也」。","火、迫、乾","火气逼上，取「迫」一面。"),
("㙝","xié","㙝从土脅聲，《集韻》「隄也」，《玉篇》「隄水也」，堤岸。","土、隄、水","土成排而束水，取「并列夹」一面。"),
("𣣲","xié","𣣲从欠脅聲（《說文》「翕氣也」），合气、屏气、抑制呼吸不出声。","欠、翕、屏","肋翕而气收，取「翕动」一面。"),
("嗋","xié","嗋从口脅聲，《集韻》「合也、吸也」，合口吸气。","口、合、吸","口合而吸，取「翕」一面。"),
("𣹩","xié","𣹩从水脅聲，《廣韻》「水流」，《集韻》「水流貌」，水纹如肋。","水、流、紋","波成排如肋，取「并列」一面。")]
claims=[]; cards=[]
for i,(ch,py,body,heng,sm) in enumerate(rows,1):
    secs=[{"key":"bengen","label":"字根本義","text":BEN,"cites":[ch]},
      {"key":"zigen","label":"字根","text":f"{ch}（{py}）属劦部。"+body,"cites":[ch]},
      {"key":"xingpang","label":"形旁與聲旁","text":"形旁定类，声旁「劦/脅」取比喻义——象肋骨成排、并力夹持一样。","cites":[ch]},
      {"key":"hengxiang","label":"横向比較","text":f"以「{ch}」为落点：{heng}；同一成排并力之象，形符各定落点。","cites":[ch]},
      {"key":"shengmu","label":"聲母義","text":sm,"cites":[ch]}]
    cards.append({"char":ch,"pinyin":py,"bus":["劦部"],"sections":secs,
      "sources":["《系統漢語》卷六十三「索」第380部「劦部」","說文解字","廣韻","集韻","玉篇"]})
    text="\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id":f"zk-380b-{i:02d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":f"{ch}（{py}）劦部字卡：{heng.split('、')[0]}之列","statement":text,
      "boundary":f"字卡释字，第380部「劦部」；{ch}依原稿该条训释属并列夹持一系。",
      "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
for c in cards:
    json.dump(c,open(os.path.join(ROOT,"web","public","cards",c["char"]+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cards",len(claims))
draft={"schema_version":1,"intent":"字卡380劦部胁系10字 2026-10-23","risk":"medium","claims":claims}
path=os.path.join(ROOT,"intake","20261023-字卡380劦乙.json")
json.dump(draft,open(path,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
rc,out=run(["knowledge-plan","capture","--file",path,"--format","json"]); print("capture rc",rc)
m=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',out); b=re.search(r'"bundle_id":\s*"(bnd_[0-9a-f]+)"',out)
if not(m and b): print(out[-1000:]); raise SystemExit(1)
h,bid=m.group(1),b.group(1); print("bundle",bid,"hash",h)
for s in (["bundle-approve",bid,"--content-hash",h,"--apply"],["bundle-apply",bid,"--content-hash",h,"--apply"]):
    r,o=run(s); print(s[0],r,'"applied": true' in o)
r,o=run(["rebuild"]); print("rebuild",r)