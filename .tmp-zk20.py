import json,subprocess,os,re,io,glob
B="源自《系統漢語》卷六十二「蛇」部之「它部」（第359部）；字卡五步规程。"
H="部頭它象蛇形，指蛇（《說文》「虫也，从虫而長，象寃曲垂尾形」）；轉義邪惡、第三人稱、婀娜、拖拉；音源為眼鏡蛇吐信之聲；字族三衍義：①蛇爬行→拖拉負荷逶迤 ②蛇盤繞→迴旋堆疊團塊 ③蛇神態→吐信咬人窺視。"
rows=[
("zk-171","它本義：象蛇形，指蛇；轉義邪惡、他稱","它（虫，tā/shé）象蛇形，指蛇；辯證虫、它本一字，今「虫」係「蟲」之簡化。轉義：邪惡（《玉篇》「非也、異也」）、第三人稱（《正字通》「與佗、他同」）；蜿蜒→婀娜（yí）、拖拉（tuō）。音源：眼鏡蛇吐信聲。"),
("zk-172","蛇本義：虫它，虵屬","蛇（shé）从虫、它聲，轉注（它即本字）。《集韻》「虺屬。或作蛇、虵」；委蛇＝委曲自得；tuǒ 尺蠖；chí 毆蛇地名。"),
("zk-173","佗本義：从人它聲，負何也","佗（拖扡拕，tuó）从人、它聲，轉注，取拖。tā 彼之稱；tuō 引也（拖）；《史記》橐佗＝駱駝。"),
("zk-174","跎本義：从足它聲，蹉跎失足","跎（tuó）从足、它聲，轉注。《說文》「蹉跎也」；《楚辭》注「蹉跎，失足」，浪費時光。"),
("zk-175","拕本義：从手它聲，曳也","拕（tuō）从手、它聲，轉注。《說文》「曳也。从手它聲，托何切」，拖、牽拉。"),
("zk-176","沱本義：从水它聲，江別流，可停船水灣","沱（池沲，tuó）从水、它聲，轉注。《說文》「江別流也」；《正字通》「涕垂貌」；《集韻》「滂沱，大雨」。"),
("zk-177","鮀本義：从魚它聲，鯰也","鮀（tuó）从魚、它聲，轉注。《說文》「鯰也」；《本草圖經》形似守宮而大、長丈餘；《正字通》引《爾雅》「鯊鮀」吹沙小魚；漢典指揚子鰐。"),
("zk-178","駝本義：从馬它聲，駱駝；背僂負物","駝（tuó）从馬、它聲，轉注。《玉篇》「駱駝也」；《正字通》「背僂也」「凡以畜負物曰駝」——駝峰蜿蜒而能負物如蛇。"),
("zk-179","舵本義：从舟它聲，正船木","舵（䑨柂杕，duò）从舟、它聲，轉注。《集韻》「柁，正船木」；《釋名》「舟尾曰柂。柂，拖也，後見拖曳也，且弼正船使順流不他戾也」——擺動如蛇而正船。"),
("zk-180","鴕本義：从鳥它聲，鴕鳥","鴕（tuó）从鳥、它聲，轉注。《正字通》「鴕，大鳥，駝蹄」；因鳥族作「鴕」——頸長似蛇、體型如駝。"),
("zk-181","酡本義：从酉它聲，飲而赭色著面","酡（𨠑，tuó）从酉、它聲，轉注。《集韻》「飲而赭色著面」；duò「將醉謂之酡」——本指醉而走路搖晃如蛇，後專指臉紅。"),
("zk-182","陀本義：从阜它聲，陂陀不平","陀（坨岮阤陊陁，tuó）从阜、它聲，轉注。《玉篇》「陂陀，險阻也」；《廣韻》「不平之皃」；duò 毀壞崩落（《博雅》「阤，壞也」）。"),
("zk-183","䙾本義：从見它聲，司人也，伺機","䙾（𧠉𧠜施，shī）从見、它聲，轉注。《說文》「司人也。从見它聲，讀若馳，式支切」；《集韻》「䙾䙾，面柔」；通作「施」。"),
]
draft={"schema_version":1,"intent":"字卡它部13条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第二十批.json"
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