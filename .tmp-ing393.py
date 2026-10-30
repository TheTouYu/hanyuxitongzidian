import json,subprocess,os,glob
BK="源自《系統漢語》第388部「季部」；字卡五步规程。"
BJ="源自《系統漢語》第389部「己部」；字卡五步规程。"
D=[
("痵",BK,"季部字族取禾穗「起伏不定」一面。痵从疒季聲，《說文》「氣不定也」（其季切），謂氣喘起伏不定；《廣韻》「病中恐也」。疒定其類為病，季示其氣如穗之上下，故氣不定曰痵。"),
("悸",BK,"悸从心季聲，《說文》「心動也」（其季切），心慌而躍；《廣雅》「怒也」。心之動如禾穗遇風而搖，一上一下不可止，是季部「起伏不定」在心神一面的落點。"),
("㳵",BK,"㳵从水季聲，《集韻》「居悸切，音季」，水名。水之流亦起伏成波，故以水定其落點；此字僅存水名一義，形符但標類屬。"),
("㻑",BK,"㻑从玉季聲，《集韻》「居悸切，音季」，玉名；《正字通》謂「㻑、㻒、㻓、𤥼、𤥽並俗字，音義皆訛誤，宐刪」。原稿兩說並存，故只記玉名而不強解取義。"),
("鯚",BK,"鯚从魚季聲，《正字通》「魚銳喙細鱗，俗呼鯚魚」，即鱖魚（桂魚、桂花魚、胖鱖）。體側扁、背隆起、棕黃有斑，斑塊錯落如穗之起伏；以魚定其落點。"),
("記",BJ,"己部字族取磚石「壘疊接續」一面。記从言己聲，《說文》「疏也」（居吏切），一事既畢、次事相續而書之，故為記載；《玉篇》「錄也、識也」，又記住、記號、記事之文。"),
("紀",BJ,"紀从糸己聲，《說文》「絲別也」（居擬切），謂絲縷各有頭緒、前後相續而不亂；引申綱紀、條理，又十二年為一紀。己本象磚縫相續，加糸則絲緒相續，是其正落點。"),
("杞",BJ,"杞从木己聲，《說文》「枸杞也」（墟里切）；《廣韻》春名天精子、夏名枸杞葉、秋名卻老枝、冬名地骨根。又杞柳（紅皮柳），枝條韌可編箱筐——枝條相接而編，正己之「接續」在木一面的落點。"),
("屺",BJ,"屺从山己聲，《說文》「山無草木也」（墟里切），《詩》「陟彼屺兮」；《集韻》或作峐。己象磚石壘疊，山無草木則岩石裸露堆疊，故以山定其落點。"),
("圮",BJ,"圮从土己聲，《廣韻》「岸毀，又覆也」。己為壘疊之形，壘極而傾則為圮——同一「累疊」之義反轉而成崩塌，故圮是己部的反面落點，以土定其類。"),
]
cl=[{"id":f"bt3-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{d[0]}（字卡）",
     "statement":d[2],"boundary":d[1],"permission":"public","fact_classes":["evidence_scope"],
     "duplicate_resolution":"create_distinct_with_boundary"} for i,d in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡389己部二版2026-10-23","risk":"low","claims":cl},
          open(r"intake\20261023-字卡389己部.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
env=dict(os.environ); env["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+env["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=env)
    return (r.stdout or "")+(r.stderr or "")
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡389己部.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    b=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",b,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",b,"--apply","--content-hash",h); run("bundle-apply",b,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",b,"err",v.get("errors"))
else: print(out[-500:])