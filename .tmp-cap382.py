import json, subprocess, os, re
ROOT=r"D:\系统汉字"; PY=os.path.join(ROOT,".runtime","venv","Scripts","python.exe")
PKC=[PY, os.path.join(ROOT,"tools","pkc_tmpfix.py")]
ENV=os.environ.copy(); ENV["PATH"]=os.path.join(ROOT,".runtime","mingit","cmd")+os.pathsep+ENV.get("PATH","")
def run(a):
    p=subprocess.run(PKC+a,cwd=ROOT,capture_output=True,text=True,encoding="utf-8",env=ENV); return p.returncode,p.stdout+p.stderr
BEN="占部部头从卜从口，外加「冎」（牛肩胛骨）：口象骨卜所钻之孔，卜象灼出之裂纹，合为骨卜；引申窥察推测、据有、贴近。音源本卜声，义音同「聶」。"
rows=[("占","zhān","占象骨卜视兆而问（《說文》「視兆問也，職廉切」）；引申窥察、推测、验；去声「据有」（占據）。","卜、兆、據","灼骨观纹，取「贴近察看」一面。"),
("貼","tiē","貼（贴）从貝占聲，附益、贴近、补贴；《六書故》「附益也」。","貝、附、近","贝附于物，取「贴近」一面。"),
("店","diàn","店从广占聲，置货鬻物之所，店肆；一说出「坫」。","广、肆、置","货聚于屋，取「据有」一面。"),
("砧","zhēn","砧从石占聲，捣衣、切物之石（同「碪」），枮为其或体。","石、捶、碪","石承物而受击，取「贴承」一面。"),
("坫","diàn","坫从土占聲，《說文》「屏也」；反爵之坫、堂隅之坫，以土为之。","土、屏、堂","土台据地，取「据」一面。"),
("阽","diàn","阽从阜占聲，《說文》「壁危也」，临危、阽危。","阜、危、壁","临壁将坠，取「贴近」一面。"),
("黏","nián","黏从黍占聲，相著、胶附（同「粘」），黏连。","黍、著、粘","米汁相附，取「贴附」一面。"),
("鮎","nián","鮎（鲇）从魚占聲，鱼名，体滑多黏液，无鳞。","魚、滑、粘","体表黏滑，取「黏」一面。"),
("毡","zhān","毡（氈）从毛占聲，毳毛压成之席，毡毯。","毛、席、壓","毛相贴而成片，取「黏合」一面。"),
("佔","zhàn","佔从人占聲，占有、占据（同「占」去声）。","人、據、有","人据其地，取「据有」一面。")]
claims=[]; cards=[]
for i,(ch,py,body,heng,sm) in enumerate(rows,1):
    secs=[{"key":"bengen","label":"字根本義","text":BEN,"cites":[ch]},
      {"key":"zigen","label":"字根","text":f"{ch}（{py}）属占部。"+body,"cites":[ch]},
      {"key":"xingpang","label":"形旁與聲旁","text":"形旁定类，声旁「占」取比喻义——象灼骨而贴近窥其兆纹一样。","cites":[ch]},
      {"key":"hengxiang","label":"横向比較","text":f"以「{ch}」为落点：{heng}；同一贴近据有之象，形符各定落点。","cites":[ch]},
      {"key":"shengmu","label":"聲母義","text":sm,"cites":[ch]}]
    cards.append({"char":ch,"pinyin":py,"bus":["占部"],"sections":secs,
      "sources":["《系統漢語》卷六十三「索」第382部「占部」","說文解字","廣韻","集韻"]})
    text="\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id":f"zk-382-{i:02d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":f"{ch}（{py}）占部字卡：{heng.split('、')[0]}之占","statement":text,
      "boundary":f"字卡释字，第382部「占部」；{ch}依原稿该条训释属窥察、据有、贴近三支之一。",
      "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
for c in cards:
    json.dump(c,open(os.path.join(ROOT,"web","public","cards",c["char"]+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cards",len(claims))
draft={"schema_version":1,"intent":"字卡382占部10字 2026-10-23","risk":"medium","claims":claims}
path=os.path.join(ROOT,"intake","20261023-字卡382占.json")
json.dump(draft,open(path,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
rc,out=run(["knowledge-plan","capture","--file",path,"--format","json"]); print("capture rc",rc)
m=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',out); b=re.search(r'"bundle_id":\s*"(bnd_[0-9a-f]+)"',out)
if not(m and b): print(out[-900:]); raise SystemExit(1)
h,bid=m.group(1),b.group(1); print("bundle",bid,"hash",h)
for s in (["bundle-approve",bid,"--content-hash",h,"--apply"],["bundle-apply",bid,"--content-hash",h,"--apply"]):
    r,o=run(s); print(s[0],r,'"applied": true' in o)
r,o=run(["rebuild"]); print("rebuild",r)