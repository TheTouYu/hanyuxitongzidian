import json,subprocess,os,re,io
B="源自《系統漢語》卷六十二「蛇」部之「夕部」（第366部）；字卡五步规程。"
rows=[
("zk-316","夕本義：象彎月形，指月亮，與月同源","夕（xī）象彎月形，本義月亮，與月同源（《玉篇》「太隂之精也，夜見光謂之月」）；轉義夜晚（《說文》「莫也，从月半見」）、傾斜（《廣雅》「衺也」）、墓穴（穸）。音源：月因形借缺、夕因時借亦。"),
("zk-317","穸本義：从穴夕聲，窀穸（埋葬、墓穴）","穸（xī）从穴、夕聲，轉注。《說文》「窀穸也」埋葬；《字彙》「墓穴幽堂」；《廣韻》「夜也」。"),
("zk-318","飧本義：从夕食，餔也（晚飯）","飧（sūn）从夕从食，象意。晚飯（《說文》「餔也」）；《玉篇》「水和飯也」；《釋名》「飧，散也，投水于中自解散也」。"),
("zk-319","汐本義：从水夕聲，夜間海潮","汐（xī）从水、夕聲，轉注。《康典》「海濤早曰潮，夕曰汐」。"),
("zk-320","蕵本義：从艸飧聲，酸模（須蕵蕪）","蕵（sūn）从艸、飧聲，轉注。《爾雅》「須蕵蕪」，郭注「似羊蹄，葉細」——酸模，嫩莖可食、全草入藥；疑古人以其為晚餐，酸以助消化。"),
("zk-321","名本義：从口从夕，自命也（稱謂）","名（míng）从口从夕，象意：夜晚昏暗互不相見，自報姓名（《說文》「自命也，夕者冥也，冥不相見，故以口自名」）；轉義名稱、旌表（銘）、辨明、大而成人。音源：義音同冥。"),
("zk-322","酩本義：从酉名聲，酩酊（醉甚）","酩（mǐng）从酉、名聲，轉注。《說文新附》「酩酊，醉也」；《集韻》「醉甚，或作佲、𠋶」。"),
("zk-323","茗本義：从艸名聲，荼芽（茶葉）","茗（míng）从艸、名聲，轉注。《說文》「荼芽也」；《爾雅注》「荼晚取者為茗，一名荈」——茶葉；茶多飲如醉，故从名、義音如酩。"),
("zk-324","眳本義：从目名聲，目小／目暗","眳（míng）从目、名聲，轉注。《集韻》「目小也，一曰眳睛不恱也」；《類篇》「目暗也」。"),
("zk-325","㫥本義：从日名聲，日暗（俗冥字）","㫥（mǐng）从日、名聲，轉注。《集韻》「日暗也」；《正字通》「俗冥字」。"),
]
draft={"schema_version":1,"intent":"字卡夕部首10条入库 2026-10-23","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261023-字卡第三十三批.json"
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