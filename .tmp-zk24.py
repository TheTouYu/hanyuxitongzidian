import json,subprocess,os,re,io
B="源自《系統漢語》卷六十二「蛇」部之「也部」（第360部）；字卡五步规程。"
rows=[
("zk-222","施本義：从㫃也聲，旗皃；用也加也設也","施（𠤒，shī）从㫃、也聲，轉注。《說文》「旗皃」，旗幟飄動之狀；《集韻》「惠也、與也」；《正字通》「用也、加也、設也、惠也」。"),
("zk-223","彵本義：从彳也聲，安行；同迤","彵（tuǒ）从彳、也聲，轉注。《玉篇》「安行」；yí 同「迤」逶迤。"),
("zk-224","扡本義：从手也聲，引也、曳也","扡（拖拕𢼏拸移棲，tuō）从手、也聲，轉注，取拖。《集韻》「拕，引也」「曵也」「牽也」；yǐ 加也、離也；chǐ 析也。"),
("zk-225","䪧本義：从音也聲，咸䪧黄帝樂名","䪧（chí）从音、也聲，轉注。《廣韻》「咸䪧，黃帝樂名」；《樂記》作「池」——咸池，黃帝之樂。"),
("zk-226","杝本義：从木也聲，杝落也（籬笆）；同舵","杝（柂舵，lí）从木、也聲，轉注。《說文》「杝，落也，讀若他」籬笆；zhì 析薪（順紋劈開）；yí 椴木；tuò 車名；duò 同舵。原稿配東漢陶制舵船模型圖，證杝即舵。"),
("zk-227","他本義：从人也聲，彼之稱","他（佗馱，tā）从人、也聲，轉注，取他稱。《集韻》「佗，彼之稱，或从也，通作它」；《玉篇》「誰也」；tuó 馱（畜負物）。"),
("zk-228","她本義：从女也聲，蜀謂母曰姐；女性第三人稱","她（姐毑媎，jiě/tā）从女、也聲，轉注。jiě《集韻》「蜀謂母曰姐，淮南謂之社，古作毑，或作她」；tā 女性第三人稱（後起）。"),
("zk-229","貤本義：从貝也聲，重次弟物也","貤（yì）从貝、也聲，轉注。《說文》「重次弟物也，从貝也聲，以豉切」次第重迭之物；《廣雅》「益也」增加；yí 轉移、販賣。"),
("zk-230","地本義：从土也聲，元氣初分，重濁陰為地","地（墬，dì）从土、也聲，轉注。《說文》「元氣初分，輕清陽為天，重濁陰為地，萬物所陳𠛱也」；《白虎通》「地者，易也，養萬物懷任交易變化也」；《釋名》「底也，其體底下，載萬物也」；de 助詞。"),
("zk-231","崺本義：从山也聲，峛崺山卑長","崺（yǐ）从山、也聲，轉注。《玉篇》「峛崺，山卑長也，或作邐迤」；《廣韻》「峛崺，沙丘狀」。"),
]
draft={"schema_version":1,"intent":"字卡也部余10条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in rows:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":title,"statement":stmt,
      "boundary":B,"permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第二十四批.json"
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