import json, subprocess, os, re
ROOT=r"D:\系统汉字"; PY=os.path.join(ROOT,".runtime","venv","Scripts","python.exe")
PKC=[PY, os.path.join(ROOT,"tools","pkc_tmpfix.py")]
ENV=os.environ.copy(); ENV["PATH"]=os.path.join(ROOT,".runtime","mingit","cmd")+os.pathsep+ENV.get("PATH","")
def run(a):
    p=subprocess.run(PKC+a,cwd=ROOT,capture_output=True,text=True,encoding="utf-8",env=ENV); return p.returncode,p.stdout+p.stderr
BEN="㚔部部头象桎梏之夹，本义拘押控制；㚔与𡴘同源，楷化并为「幸」，其族一支取执持拘系，一支取「锁定而不可动」所生的僵直、侥幸。"
rows=[("縶","zhí","縶从糸執聲，《廣韻》「繄馬」，絆住馬脚；《類篇》「繫也」，拘囚。","糸、絆、繫","绳系马足，取「系住」一面。"),
("贄","zhì","贄《玉篇》「執玉帛也」，攜帶禮物相見（同摯）。","貝、禮、執","执礼相见，取「执持」一面。"),
("鷙","zhì","鷙《說文》「擊殺鳥也」，善於搏殺的猛禽。","鳥、擊、猛","鹰隼执爪而击，取「执持」一面。"),
("謺","zhé","謺《說文》「謺讘也」，附耳小語；《廣韻》「拾人語也」。","言、小語、讘","附耳相执而语，取「贴近」一面。"),
("䠟","dié","䠟《說文》「䠟足也」，絆住脚；《集韻》「小步」。","足、絆、步","足被绊，取「拘」一面。"),
("䙝","dié","䙝《說文》「重衣也」，重叠之衣。","衣、重、叠","衣重叠而拘身，取「拘束」一面。"),
("漐","zhì","漐《集韻》「汗出貌」，《正字通》「漐漐，小雨不輟」，黏滯之意。","水、汗、滯","黏滞不行，取「止」一面。"),
("𩅀","diàn","𩅀《說文》「寒也，或曰早霜」；又「小濕也」。","雨、霜、寒","霜结而止，取「拘」一面。")]
claims=[]; cards=[]
for i,(ch,py,body,heng,sm) in enumerate(rows,1):
    secs=[{"key":"bengen","label":"字根本義","text":BEN,"cites":[ch]},
      {"key":"zigen","label":"字根","text":f"{ch}（{py}）属㚔（幸）部。"+body,"cites":[ch]},
      {"key":"xingpang","label":"形旁與聲旁","text":"形旁定类，声旁「㚔/執」取比喻义——象被桎梏夹住、动不得一样。","cites":[ch]},
      {"key":"hengxiang","label":"横向比較","text":f"以「{ch}」为落点：{heng}；同一夹持拘系之象，形符各定落点。","cites":[ch]},
      {"key":"shengmu","label":"聲母義","text":sm,"cites":[ch]}]
    cards.append({"char":ch,"pinyin":py,"bus":["㚔部"],"sections":secs,
      "sources":["《系統漢語》卷六十三「索」第379部「㚔部」","說文解字","廣韻","集韻","玉篇"]})
    text="\n\n".join(f"【{s['label']}】{s['text']}" for s in secs)
    claims.append({"id":f"zk-379b-{i:02d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":f"{ch}（{py}）㚔部字卡：{heng.split('、')[0]}之拘","statement":text,
      "boundary":f"字卡释字，第379部「㚔部」；{ch}依原稿该条训释属拘押执持或僵直一系。",
      "permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
for c in cards:
    json.dump(c,open(os.path.join(ROOT,"web","public","cards",c["char"]+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cards",len(claims))
draft={"schema_version":1,"intent":"字卡379㚔部余9字 2026-10-23b","risk":"medium","claims":claims}
path=os.path.join(ROOT,"intake","20261023-字卡379㚔乙b.json")
json.dump(draft,open(path,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
rc,out=run(["knowledge-plan","capture","--file",path,"--format","json"]); print("capture rc",rc)
m=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',out); b=re.search(r'"bundle_id":\s*"(bnd_[0-9a-f]+)"',out)
if not(m and b): print(out[-1000:]); raise SystemExit(1)
h,bid=m.group(1),b.group(1); print("bundle",bid,"hash",h)
for s in (["bundle-approve",bid,"--content-hash",h,"--apply"],["bundle-apply",bid,"--content-hash",h,"--apply"]):
    r,o=run(s); print(s[0],r,'"applied": true' in o)
r,o=run(["rebuild"]); print("rebuild",r)
