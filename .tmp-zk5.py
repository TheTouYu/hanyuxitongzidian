import json,subprocess,os,re,io
B="源自《系統漢語》卷六十「妥」部（第349部）；字卡五步规程。"
items=[
("zk-023","娞本義：从女妥聲，安好；通作綏","娞（něi/suī）从女、妥聲，屬轉注。《集韻》「㛱娞，姸也，或从委」；suī 讀「安也，通作綏」。女之安者為娞，加糸則為綏，皆取妥之「安」義。"),
("zk-024","綏本義：从糸从妥，車中把也，執以安身","綏（suī/suí）从糸从妥，屬轉注。《說文》「車中把也。从糸从妥。息遺切」，徐鍇「升車必正立，執綏所以安也」，指登車時用以把手的繩索；《玉篇》「止也、安也」，《廣雅》「撫也、舒也」。取妥之安義，以糸定其物。"),
("zk-025","餒本義：从食妥聲，饑也，魚敗亦曰餧","餒（něi）从食、妥聲，屬轉注，聲旁取妥之「柔弱委頹」。《廣韻》「餧，饑也，一曰魚敗曰餧，餒同」：飢則弱，魚敗則軟，皆委頹之狀。同取弱敗者：脮（肉）魚敗、㞂（尢）風疾、俀（人）弱。"),
("zk-026","㞂本義：从尢妥聲，委㞂，行病不能行","㞂（tuǐ）从尢、妥聲，屬轉注，聲旁取柔弱委頹。《廣韻》「委㞂，行病」，《集韻》「𡰂㞂，風疾，或作𡯵㾼」，指中風癱瘓、不能行走。同取委弱不行者：俀（人）、㱣（歹）、餒（食）。"),
("zk-027","荽本義：从艸妥聲，芫荽，指其莖葉柔軟","荽（suī）从艸、妥聲，屬轉注，聲旁取柔弱。《玉篇》「荾，胡荾，香菜；荽、䒘並同上」，芫荽俗稱香菜，「指其莖葉軟之意」；《集韻》「葰，《說文》𧅁屬，可以香口，或作荾、荽」。同取柔弱者：桵（木）木理白疏、娞（女）。"),
("zk-028","鵎本義：从鳥妥聲，鳥名，屬借聲與訛字","鵎（tuǒ/yàn）从鳥、妥聲，聲旁僅借音不取義。《集韻》「鳥名」；yàn 讀《正字通》「鴳字之譌」，鴳即冠雀（《廣韻》「鶬鴳也」）。此條屬借聲兼形近訛字，不作比況。"),
]
draft={"schema_version":1,"intent":"字卡妥部又六条入库 2026-10-22","risk":"low","claims":[]}
for cid,title,stmt in items:
    draft["claims"].append({"id":cid,"node":"hanzi-yinyuan","topic_id":"topic-zika-shizi",
      "title":title,"statement":stmt,"boundary":B,"permission":"public",
      "fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"})
fn="intake/20261022-字卡第五批.json"
io.open(fn,"w",encoding="utf-8",newline="\n").write(json.dumps(draft,ensure_ascii=False,indent=1))
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
def run(*a):
    p=subprocess.run([r"D:\系统汉字\tools\pkc.cmd",*a],cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return p.stdout+p.stderr
out=run("knowledge-plan","capture","--file",fn,"--format","json")
pid=re.search(r'pln_[0-9a-f]+',out); print("PLAN",pid.group(0) if pid else out[-300:]); pid=pid.group(0)
fin=run("knowledge-plan","finalize",pid,"--format","json")
b=re.search(r'bnd_[0-9a-f]+',fin); print("BUNDLE",b.group(0) if b else fin[-300:]); b=b.group(0)
h=re.search(r'"content_hash":\s*"([0-9a-f]{64})"',run("bundle-status",b,"--format","json")).group(1)
print("HASH",h)
run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
print("done")