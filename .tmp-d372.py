import json,glob,os
ids=["遬","涑","𪋝","娕","𩱫","𥹵","殐","觫","𣫎","㑛","𧫣"]
base={"schema_version":1,"intent":"字卡372束部11字 2026-10-22",
 "risk":"medium","claims":[]}
n=0
for ch in ids:
    c=json.load(open(rf"web\public\cards\{ch}.json",encoding="utf-8"))
    text="\n\n".join(f"【{s['label']}】{s['text']}" for s in c["sections"])
    n+=1
    base["claims"].append({
      "id":f"zk-372-{n:02d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":f"{ch}（{c['pinyin']}）：束部字卡五步释义",
      "statement":text,
      "boundary":f"字卡释字（第372部「束部」）；依《系統漢語》卷六十三「索」原文五步规程成卡，故声旁取「束」的捆缚收缩一面。",
      "permission":"public","fact_classes":["evidence_scope"],
      "duplicate_resolution":"create_distinct_with_boundary"})
json.dump(base,open(r"intake\20261022-字卡372束部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("claims",len(base["claims"]))