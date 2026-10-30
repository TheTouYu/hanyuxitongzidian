import json,subprocess,os,glob
ENV=dict(os.environ); ENV["PATH"]=r"D:\系统汉字\.runtime\mingit\cmd;"+ENV["PATH"]
PY=r"D:\系统汉字\.runtime\venv\Scripts\python.exe"; SH=r"D:\系统汉字\tools\pkc_tmpfix.py"
def run(*a):
    r=subprocess.run([PY,SH]+list(a),cwd=r"D:\系统汉字",capture_output=True,text=True,encoding="utf-8",env=ENV)
    return (r.stdout or "")+(r.stderr or "")
FX="【第529部「相部」】相＝从目从木，指觀木、察看木材質（戴侗《六書故》「相，度才也。工師用木，必相視其長短曲直」）；轉義省視、形貌；由觀木引申共、交互、輔助教導。音源借音，義同「向」（徜徉＝相羊）。字族分「交互相對輔助」與「霜系」兩組。"
N="字形：古文字字形库未收。"
D=[("相","xiāng",FX,"从目从木：观木度材；引申省视、形貌、共与交互、辅助教导。","x「续消」取「续」：目視而續。"),
("想","xiǎng",FX,"从心相聲：冀思也（《說文》），物未至而意之。","x取续消：心向而思。"),
("箱","xiāng",FX,"从竹相聲：大車牝服（《說文》），車內容物處，引申箱籠。","x取续消：車箱而續。"),
("廂","xiāng",FX,"从广相聲：廊也（《說文》），堂屋東西序、正房兩側之屋。","x取续消：廊側而續。"),
("湘","xiāng",FX,"从水相聲：湘江（《說文》），疑取憑河道放木排之義。","x取续消：水長而續。"),
("霜","shuāng",FX,"从雨相聲：霜（《說文》「喪也，成物者」），物遇霜而喪。","sh「失收」取「收」：氣收而凝。"),
("孀","shuāng",FX,"从女霜聲：寡婦（《玉篇》），如霜之孤冷。","sh取失收：孤而收。"),
("灀","shuāng",FX,"从水霜聲：水名，又水寒之意。","sh取失收：水寒而收。"),
("鸘","shuāng",FX,"从鳥霜聲：鸘鳥（鷫鸘），雁屬。","sh取失收：鳥孤而收。"),
("驦","shuāng",FX,"从馬霜聲：驦馬（驌驦），良馬名。","sh取失收：馬駿而收。"),
("葙","xiāng",FX,"从艸相聲：青葙，草名，子黑光亮。","x取续消：草實而續。"),
("緗","xiāng",FX,"从糸相聲：帛淺黃色（《說文》「帛淺黃色也」）。","x取续消：絲染而續。")]
for ch,p,F0,xp,sm in D:
    sec=[{"key":"bengen","label":"字根本义","text":F0,"cites":[]},{"key":"zigen","label":"字形","text":N,"cites":[]},
         {"key":"xingpang","label":"形旁声旁","text":xp,"cites":[]},
         {"key":"hengxiang","label":"横向对照","text":"相系諧聲字分兩面：交互相對輔助（想／箱／廂／湘／葙／緗）與霜系（霜／孀／灀／鸘／驦）；只列同族字。","cites":[]},
         {"key":"shengmu","label":"声母义","text":sm,"cites":[]}]
    json.dump({"char":ch,"pinyin":p,"bus":[{"num":529,"name":"相"}],"sections":sec},open(rf"web\public\cards\{ch}.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
cl=[{"id":f"lxiang4-{i:03d}","node":"hanzi-yinyuan","topic_id":"topic-zika-shizi","title":f"{ch}（字卡·{p}）","statement":f"{ch}（{p}）＝{xp}",
 "boundary":"源自《系統漢語》第529部「相部」（卷八十八 昜）；字卡五步规程。","permission":"public","fact_classes":["evidence_scope"],"duplicate_resolution":"create_distinct_with_boundary"} for i,(ch,p,F0,xp,sm) in enumerate(D,1)]
json.dump({"schema_version":1,"intent":"字卡529a2026-10-23","risk":"low","claims":cl},open(r"intake\20261023-字卡529a.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
out=run("knowledge-plan","capture","--file",r"intake\20261023-字卡529a.json","--format","json")
print("dup:", "PLAN_DUPLICATE" in out)
if "PLAN_DUPLICATE" not in out:
    bd=os.path.basename(sorted(glob.glob(r"data\knowledge\bundles\bnd_*.json"),key=os.path.getmtime)[-1])[:-5]
    h=json.loads(run("bundle-status",bd,"--format","json"))["bundles"][0]["content_hash"]
    run("bundle-approve",bd,"--apply","--content-hash",h); run("bundle-apply",bd,"--apply","--content-hash",h)
    run("rebuild"); v=json.loads(run("validate","--format","json")); print("bundle",bd,"err",v.get("errors"))