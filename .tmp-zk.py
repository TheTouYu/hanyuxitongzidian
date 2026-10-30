import json,subprocess,os,re,io
B="源自《系統漢語》卷六十「𦟀」部、卷六十「冎」部；字卡五步规程。"
claims=[
 dict(id="zk-001",title="𦟀本義：象兩耳長長的騾子形，指騾子，為驘之初文",
  statement="𦟀（luó）為第346部部頭。本義「象兩耳長長的騾子形，指騾子」，《正字通》引《考工記》「𦝠卽臝之省」，即驘（騾）之初文，《說文》「驢父馬母，从馬𦝠聲」。轉義三路：能馱載→負載盈餘（分化為贏）、雜交難育→羸弱（分化為羸）、毛色比馬淺→裸露（分化為裸）。辯證：本字少用、多作聲旁，本義所指模糊，《說文》或曰嘼名、象形。",
  topic=True),
 dict(id="zk-002",title="羸本義：从羊𣎆聲，瘦弱的羊",
  statement="羸（léi）从羊、𣎆聲，形旁羊定其類為羊，聲旁𦟀所取為騾「雜交難育」的削瘦一面；《說文》「瘦也」，注「羊主給膳，以瘦為病，故从羊」，《玉篇》「弱也、病也、痩也、劣也」。屬轉注字。同取「削」者：𡰠（尢）膝中病、蠃（虫）腰細之蟲。"),
 dict(id="zk-003",title="蠃本義：从虫𦝠聲，取騾之背負為義",
  statement="蠃（luǒ）从虫、𦝠聲，屬轉注。部內辯證明言「蠃之从𦝠，只取背負為義」，故其義為背負之蟲：蝸牛負殼而行、蜾蠃負螟蛉歸巢。《說文》「蜾蠃也，一曰虒蝓」；luó 讀為螺、蚌屬；guǒ 讀為蠃蘭（車名）。同取背負者：蝸（虫）蝸牛、螺（虫）旋殼、蠡（虫）蚌與瓢。"),
 dict(id="zk-004",title="冎本義：象三節相連的動物腿骨形，為骨之初文",
  statement="冎（guǎ）為第347部部頭。本義「甲骨文象三節相連的動物腿骨頭形，代指動物的骨頭」，本「骨」字初文，《說文》「肉之覈也，从冎有肉」。部內另條「甲骨文象動物肩胛骨形，與冎所指本同」。字形自甲骨一期三節相扣，至戰國上部訛作「吅」、下部作「月」，趨於聲化。"),
 dict(id="zk-005",title="骨本義：从冎有肉，肉之覈也，屬象意字",
  statement="骨（gǔ）＝冎（骨節）＋肉（月），兩部件皆表義而無專表聲者，故為象意字（非轉注）。《說文》「肉之覈也，从冎有肉」。同取骨節之形者：咼（口）骨節外突如口戾、骷（骨）枯骨、骾（骨）骨鯁在喉。"),
 dict(id="zk-006",title="蝸本義：从虫咼聲，取咼口戾不正之凹而旋",
  statement="蝸（wō）从虫、咼聲，屬轉注。咼从口从冎，口戾不正；聲旁所取為「歪斜而凹」，故蝸義為殼螺旋而中凹、負殼而行之蟲，《說文》「蝸蠃也，从虫咼聲」。同取凹而斜者：渦（水）回旋成凹、窩（穴）凹處、鍋（金）凹而能盛、媧（女）凹凸相合、禍（示）曲折不順。"),
]
draft={"schema_version":1,"intent":"字卡首字六条入库 2026-10-22","risk":"low","claims":[]}
for i,c in enumerate(claims):
    cl={"id":c["id"],"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
        "title":c["title"],"statement":c["statement"],"boundary":B,
        "permission":"public","fact_classes":["evidence_scope"],
        "duplicate_resolution":"create_distinct_with_boundary"}
    if c.get("topic"):
        cl.update({"topic_path":"knowledge/hanzi-yinyuan/02y-zika.md","topic_title":"字卡（释字五步）",
                   "topic_summary":"按释字五步规程逐字成稿的字卡条目：字根本義、形旁聲旁、横向比較、聲母義。",
                   "topic_keywords":["字卡","释字","五步"]})
    draft["claims"].append(cl)
fn="intake/20261022-字卡首批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
out=run("knowledge-plan","capture","--file",fn,"--format","json")
m=re.search(r'pln_[0-9a-f]+',out); print("PLAN",m.group(0) if m else out[-500:])
if not m: raise SystemExit(1)
pid=m.group(0)
fin=run("knowledge-plan","finalize",pid,"--format","json")
b=re.search(r'bnd_[0-9a-f]+',fin); print("BUNDLE",b.group(0) if b else fin[-400:])
if b:
    st=run("bundle-status",b.group(0),"--format","json")
    h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',st); print("HASH",h.group(1) if h else "?")
    if h:
        print(run("bundle-approve",b.group(0),"--apply","--content-hash",h.group(1))[-160:])
        print(run("bundle-apply",b.group(0),"--apply","--content-hash",h.group(1))[-160:])