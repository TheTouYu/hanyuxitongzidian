import json,subprocess,os,re,io
B="源自《系統漢語》卷六十一「犀（屖）」部之「山部」（第356部）；字卡五步规程。"
rows=[
("zk-140","山本義：象群峰聳立，指山嶺；音源山囪可通","山：象群峰聳立形，指山嶺（《集韻》「土髙有石曰山」）。轉義：山下大上小、雲氣蒸騰，故《說文》「宣也，宣氣散，生萬物，有石而高」；五嶽為山之尊，或專稱五嶽為山；高體大→巨大（山響、山呼）、象山之物（山牆）、山狀紋飾；山人→粗鄙；墳墓亦稱山。音源：借音字——山聳立如囪，故山、囪可通（僊从囪聲，《漢書》作僊）。字族兩路：①山的本義 ②山狀起伏隆起堵塞。"),
("zk-141","屾本義：二山也，山之重文","屾（shēn）＝二山。《說文》「二山也，所臻切」；山本連綿起伏，从二山無實際意義，《正字通》「屾，卽山之重文，音義不殊」。"),
("zk-142","屳本義：人在山上，仙之初文","屳（佡仙，xiān）＝人＋山，會意。《說文》「人在山上。从人从山，呼堅切」，神話中長生不死之人；《釋名》「老而不死曰仙，仙，遷也，遷入山也」。"),
("zk-143","邖本義：从邑山聲，地名","邖（shān）从邑、山聲，轉注。《說文》「地名。从邑山聲，所間切」。"),
("zk-144","旵本義：日光照也","旵（chǎn）从日、山省聲，轉注。《玉篇》「醜減切，日光照也」。"),
("zk-145","訕本義：从言山聲，謗也","訕（姍，shàn）从言、山聲，轉注，取起伏不平。《說文》「𧩂也。从言山聲，所晏切」，譏笑、譭謗；《集韻》「或作姍」。"),
("zk-146","疝本義：从疒山聲，腹痛也，隆起如小山","疝（shàn）从疒、山聲，轉注，取隆起。《說文》「腹痛也。从疒山聲，所妟切」，小腹氣痛、陰囊脹大；《釋名》「疝，詵也，氣詵詵然，上入而痛也」——組織隆起如小山。"),
("zk-147","汕本義：从水山聲，魚游水皃；抄網","汕（shàn）从水、山聲，轉注。《說文》「魚游水皃。从水山聲，《詩》蒸然汕汕，所妟切」；或指抄網類捕魚具，《爾雅》「罺謂之汕」。"),
("zk-148","舢本義：从舟山聲，舢板","舢（shān）从舟、山聲，轉注。舢板，近海江河上用槳劃的小船。"),
("zk-149","秈本義：从禾山聲，秈稻","秈（𦱑䄽，xiān）从禾、山聲，轉注。《集韻》引《方言》「江南呼稉為秈」，秈稻，植株高、米粒細長、脹性大、早熟少黏。"),
("zk-150","閊本義：从門山聲，堵塞積壓","閊（shān）从門、山聲，轉注，取山塞之狀。堵、塞；積壓、積存。"),
]
draft={"schema_version":1,"intent":"字卡山部11条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第十七批.json"
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