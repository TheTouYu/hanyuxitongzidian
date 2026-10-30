import json,subprocess,os,re,io
B="源自《系統漢語》卷六十一「犀（屖）」部之「囟部」（第354部）；字卡五步规程。"
rows=[
("zk-079","囟本義：象小兒腦門未合，音源義音同犀","囟（䏪䪿顖，xìn）象小兒腦門未完全合攏之形；《說文》「頭會，匘蓋也，象形，息進切」。音源：借音字——小兒蓄髮成獨角狀以護囟門，金文「犀」腹中標「囟」表音，故義音同犀。字族三路：細小、凹進、形近幺𣬉白之訛。"),
("zk-080","𠈈本義：从人囟聲，小皃","𠈈（𢇌佌，cǐ）从人、囟聲，轉注，取囟門細小一面。《說文》「小皃。从人囟聲，《詩》𠈈𠈈彼有屋，斯氏切」；《集韻》「或作𢇌、佌」。"),
("zk-081","細本義：从糸囟聲，微也","細（𥿳，xì）从糸、囟聲，轉注，取囟門細白。《說文》「微也。从糸囟聲。穌計切」，細小。"),
("zk-082","䪿本義：从頁囟聲，頂門也","䪿（xìn/shěng）从頁、囟聲，轉注，為囟之異體。《集韻》「囟，古作䪿」；《玉篇》「頂門也」。"),
("zk-083","𦤟本義：从肉囟聲，腋也，腋氣病","𦤟（xìn）从肉、囟聲，轉注，取囟門凹陷之狀。《類篇》「腋也」；《集韻》「思晉切，音信，腋氣病」，腋窩如囟，指狐臭。"),
("zk-084","𣳦本義：从水囟聲，细水，取沟如囟门","𣳦（硇，xì/náo）从水、囟聲，轉注。《說文》「水，出汝南新郪，入潁，从水囟聲，穌計切」，即細水（今茨河、刺河），取「溝如囟門」之意；náo《篇海》「𣳦沙，藥名，亦作硇」。"),
("zk-085","硇本義：从石囟省聲，硇沙，藥石多孔","硇（náo）从石、囟省聲，轉注，取囟門凹孔之狀。《玉篇》「硇沙，藥」；《集韻》「𠬦沙，藥石，或作𣲿、𥑩、䃩」——氯化銨天然產物，有孔、味辛鹹。"),
("zk-086","䛜本義：古文訊字，形近幺之訛","䛜（𠱖，xùn）从言、囟聲之形，實為形近訛字。《正字通》「古文訊字」；甲骨文象人被繩系而訊問之形，不从囟，疑為「幺」之訛。"),
("zk-087","凶本義：象囟門未合，引申凶險與擾動","凶（兇㐫）：象小兒囟門未合形，本同囟；甲骨文作兇，下从人更明確。轉義：囟門是要害，幼兒孱弱→凶險災禍（《玉篇》「短折也、惡也、咎也」）；腦門未合隨心跳湧動→擾動（《說文》「兇，擾恐也，从人在凶下」）。辯證：《說文》「象地穿交陷其中」之陷阱說與凶險義雖合，然無湧動之意，析形不確。"),
("zk-088","㚃本義：从凶从壺，壹㚃，氤氲不得泄","㚃（yūn）从凶从壺，會意兼聲，取囟門湧動一面。《說文》「壹㚃也。从凶从壺，不得泄，凶也，《易》天地壹㚃，於雲切」，氤氲；《集韻》「㚃鬰，不得泄也」；《正字通》「元氣交密貌，通作縕」。"),
("zk-089","忷本義：从心凶聲，擾恐也","忷（兇恟，xiōng）从心、凶聲，轉注，取擾動。《集韻》「兇，《說文》擾恐也，引《春秋傳》曹人兇懼，或作恟、忷」，憂恐。"),
("zk-090","訩本義：从言凶聲，訟也、眾言喧嘩","訩（𧧗詾，xiōng）从言、凶聲，轉注，取喧擾。《集韻》「詾，《詩傳》訟也，一曰盈也，一曰眾言，或作訩、𧧗」，爭辯、喧嘩紛擾；《正字通》「禍亂也」。"),
("zk-091","酗本義：从酉凶聲，醉怒","酗（䣴䣱，xù）从酉、凶聲，轉注，取酒後擾動。《廣韻》「醉怒，亦作䣱」；《六書故》「醉而亂也」。"),
]
draft={"schema_version":1,"intent":"字卡囟部13条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第十二批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
pid=re.search(r'pln_[0-9a-f]+',run("knowledge-plan","capture","--file",fn,"--format","json")).group(0); print("PLAN",pid)
b=re.search(r'bnd_[0-9a-f]+',run("knowledge-plan","finalize",pid,"--format","json")).group(0); print("BUNDLE",b)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1); print("HASH",h)
run("bundle-approve",b,"--apply","--content-hash",h)
print('"applied": true' in run("bundle-apply",b,"--apply","--content-hash",h))