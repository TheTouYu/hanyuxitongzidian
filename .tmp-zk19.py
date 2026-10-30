import json,subprocess,os,re,io
B="源自《系統漢語》卷六十一「犀（屖）」部之「充部」（第358部）；字卡五步规程。"
rows=[
("zk-161","充本義：从𠫓从儿，人上倒子，實即允；辯證本珫之初文","充（𠑽𠘺，chōng）从𠫓（倒子）从儿，會意，實即「允」——讓人騎在肩上，多為帶孩子出行（《玉篇》「行也」）。轉義：人上肩人→長、高（《說文》「長也，高也」）；充滿、富足、填塞、完備；借別人顯高→假冒（冒充、充當）。辯證：漢印金文「允」上从「」，與冕所从同，當指冠冕，為「珫」之初文——冠冕兩側當耳之玉（瑱，《詩》「充耳琇瑩」）；故充之高、晃蕩、填塞諸義或本屬珫。"),
("zk-162","統本義：从糸充聲，紀也，絲之頭緒","統（tǒng）从糸、充聲，轉注。《說文》「紀也。从糸充聲，他綜切」，絲的頭緒；《釋名》「統，緒也，主緒人世，類相繼如統緒也」；《集韻》「攝理」統領。"),
("zk-163","橦本義：从木充聲，木橦也","𣑁（䡴橦衝，chòng）从木、充聲，轉注。《集韻》「木㮔也」；《字彙》「㮔，木銃也」；橦《集韻》「木名，華可作布」「木一截也」。"),
("zk-164","茺本義：从艸充聲，茺蔚即益母草","茺（chōng）从艸、充聲，轉注，取高。《玉篇》「茺蔚，卽益母也」，益母草，莖如芝麻、層疊累花，故稱「九重樓」。"),
("zk-165","銃本義：从金充聲，銎也，斧受柄孔→火銃","銃（𥒝，chòng）从金、充聲，轉注，取填塞。《玉篇》「銎也」；《集韻》「斧穿也」，斧頭上受柄之孔；又指打眼器具（釺）；後指管形火器（《篇海》「火銃」）。"),
("zk-166","𪎽本義：从黃充聲，黃色；纊塞耳","𪎽（chōng）从黃、充聲，轉注，取填塞。《玉篇》「黃色」；《大戴禮》「𪎽纊塞耳，掩聽也」——以黃色絲綿塞耳，正「充耳」之制。"),
("zk-167","𡊿本義：从土充聲，坍塌丟臉","𡊿（chǒng）从土、充聲，轉注，取塌陷填塞。《字海》「坍𡊿，又作坍寵」，難為情、丟臉。"),
("zk-168","𪗯本義：从齒充省聲，與齗同，牙齦","𪗯（齗，yín）从齒、充省聲，轉注。《字彙補》「與齗同」，牙齦。"),
("zk-169","𩒘本義：从頁充聲，充也（訛字）","𩒘（chǒng）从頁、充聲，轉注（存疑條）。《玉篇》「充也」；《正字通》「訛字」。"),
("zk-170","𥬱本義：从竹充聲，竹尖也","𥬱（chòng）从竹、充聲，轉注。《集韻》「竹尖也」。"),
]
draft={"schema_version":1,"intent":"字卡充部10条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第十九批.json"
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