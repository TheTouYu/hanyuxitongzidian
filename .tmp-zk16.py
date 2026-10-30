import json,subprocess,os,re,io
B="源自《系統漢語》卷六十一「犀（屖）」部之「囪部」（第355部）；字卡五步规程。"
rows=[
("zk-128","煙本義：从火垔聲，火氣也","煙（𡨾烟，yān）从火、垔聲，轉注，屬煙狀升騰一路。《說文》「火氣也。从火垔聲，烏前切」，古文从因、籀文从宀。"),
("zk-129","禋本義：从示垔聲，潔祀也，焚柴祭天","禋（𡫻，yīn）从示、垔聲，轉注。《說文》「潔祀也，一曰精意以享為禋，从示垔聲，於眞切」；《玉篇》「敬也」；《集韻》「祀天也」——焚燒祭品、以煙祭天。"),
("zk-130","緸本義：从糸垔聲，搖動皃","緸（yīn）从糸、垔聲，轉注，取煙之搖曳。《集韻》「緸𡨚，揺動皃」。"),
("zk-131","𣱐本義：从氐垔聲，臥也","𣱐（yìn/zhì）从氐、垔聲，轉注，取煙氣下沉偃臥之狀。《說文》「臥也。从氐垔聲，於進切」；《集韻》「仆也」；zhì《廣韻》「赴也」。"),
("zk-132","黫本義：从黑垔聲，黑也","黫（𪐘黰，yān）从黑、垔聲，轉注，取煙色黑。《集韻》「黰，黒也，或作黫、𪐘」。"),
("zk-133","𦎣本義：从羊垔聲，群羊相染，一曰黑羊","𦎣（yān）从羊、垔聲，轉注。《說文》「群羊相𦎸也，一曰黑羊，从羊垔聲，烏間切」；《廣雅》「黑也」——成群羊轉相傳染羊瘟，或指黑羊。"),
("zk-134","甄本義：从瓦垔聲，匋也，製陶轉輪","甄（鄄，zhēn）从瓦、垔聲，轉注。《說文》「匋也。从瓦垔聲，居延切」，燒製陶器；《廣雅》「窯也」，《博雅》「堗下謂之甄」指製陶轉輪；又「表也、明也、察也」。"),
("zk-135","薽本義：从艸甄聲，豕首（天名精）","薽（zhēn）从艸、甄聲，轉注，取煙氣濃重之味。《說文》「豕首也。从艸甄聲，側鄰切」；《爾雅》「茢薽，豕首」，郭注「地菘、蝦蟆藍、蟾蜍蘭」，天名精，菊科藥草有臭氣。"),
("zk-136","陻本義：从阜垔聲，塞也","陻（yīn）从阜、垔聲，轉注，與堙同。《玉篇》「塞也」，堵塞。"),
("zk-137","㖶本義：从口垔聲，同咽","㖶（咽，yān/yè/yīn）从口、垔聲，轉注。《玉篇》「同咽」；《集韻》「㖶然，語聲」；yè 同噎；yīn「諲，敬也，或从口」。"),
("zk-138","籈本義：从竹垔聲，敔板止樂","籈（zhēn/jiān）从竹、垔聲，轉注。《正韻》「割木長尺，以鼓敔，所以止樂也」——古代敲敔用的木板，節制音樂，故有堵義；jiān《廣韻》「竹器」。"),
("zk-139","裀本義：从衣垔聲，衣身也，內衣、褥","裀（𧛑，yīn）从衣、垔聲，轉注。《玉篇》「衣身也」；《博雅》「複襂謂之裀」夾衣；《韻會》「通茵」褥子；《字彙》「近身衣也」內衣。"),
]
draft={"schema_version":1,"intent":"字卡囪部尾12条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第十六批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
pid=re.search(r'pln_[0-9a-f]+',run("knowledge-plan","capture","--file",fn,"--format","json")).group(0); print("PLAN",pid)
b=re.search(r'bnd_[0-9a-f]+',run("knowledge-plan","finalize",pid,"--format","json")).group(0); print("BUNDLE",b)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1); print("HASH",h)
run("bundle-approve",b,"--apply","--content-hash",h)
print("applied", '"applied": true' in run("bundle-apply",b,"--apply","--content-hash",h))