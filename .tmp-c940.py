import sys,json,glob,re,subprocess,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
ROOT=r"D:\系统汉字"
zero={"㠯":8,"𦣞":12,"一":14,"斦":15,"意":22,"睪":25,"弋":26,"夷":27,"彝":30,"異":33,"我":36,"厄":38,"業":52,"余":54,"魚":55,"禺":57,"㫃":58,"攸":59,"予":60,"于":68,"羽":72,"雨":73,"爻":103,"夭":108,"堯":111}
G=[("zh","凿总","凿"),("ch","刺持","刺"),("sh","失收","收"),("g","隔估","隔"),("k","口控","控"),("h","豁活","豁"),("j","聚决","决"),("q","亲缺","缺"),("x","续消","消"),("b","闭剥","闭"),("p","拼辟","辟"),("f","附分","分"),("m","蒙末","末"),("d","囤动","动"),("t","涂突","突"),("n","纳弄","弄"),("r","柔锐","锐"),("l","拢离","离"),("z","凿总","凿"),("c","刺持","刺"),("s","失收","收")]
nz=ns=np=0; fixed=0
for fp in glob.glob(ROOT+r"\web\public\cards\*.json"):
    try: d=json.load(open(fp,encoding="utf-8"))
    except Exception: continue
    ch=d.get("char",""); b=d.get("bus")
    num=None
    if isinstance(b,list) and b:
        if isinstance(b[0],dict): num=b[0].get("num")
        elif isinstance(b[0],int): num=b[0]
    if num is None: num=0
    sm=[s for s in d.get("sections",[]) if s.get("key")=="shengmu"]
    if not sm: continue
    sm=sm[0]
    if not sm["text"].startswith("聲母義：本部未列"): continue
    if ch in zero or num in zero.values():
        sm["text"]=f"聲母義：零聲母——本部屬緒論「零聲母諸部」（第{num}部），無擬態聲母義可系，義靠義類與字形。"; nz+=1
    else:
        py_=d.get("pinyin","") or ""
        done=False
        if py_:
            for pre,a,bb in G:
                if py_.startswith(pre):
                    sm["text"]=f"聲母義：聲母 {pre}（擬態「{a}」），取「{bb}」一面；本部未列 02z 表，按緒論推。"; ns+=1; done=True; break
        if not done:
            sm["text"]="聲母義：零聲母（今讀），本部未列 02z；待回中古反切核定。"; np+=1
    json.dump(d,open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("零声母",nz,"按声母推",ns,"余",np)
ENV=dict(os.environ); ENV["PATH"]=ROOT+r"\.runtime\mingit\cmd;"+ENV["PATH"]
subprocess.run([ROOT+r"\tools\git.cmd","add","web/public/cards"],cwd=ROOT,capture_output=True,env=ENV)
r=subprocess.run([ROOT+r"\tools\git.cmd","commit","-m","cards: 声母义按25零声母部与声母推补"],cwd=ROOT,capture_output=True,env=ENV)
print((r.stdout+r.stderr).decode("utf-8","replace")[:80])