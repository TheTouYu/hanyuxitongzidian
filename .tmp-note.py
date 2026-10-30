import json,sys,os
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
C=r"D:\系统汉字\web\public\cards"
notes={
"谷":"今亦借作「榖」之简化（同音借用，非本字）：谷本山谷水道，榖本穀物，二字各有所从，不得合为一卡。",
"干":"今亦借作「乾」「幹」之简化（同音借用，非本字）：干本树杈猎具（干戈），乾为干燥、幹为枝干，字根各异。",
"系":"今亦借作「係」「繫」之简化（同音借用，非本字）：系本丝相连，係为束缚、繫为系结，各有本义。",
"复":"今亦借作「復」「複」「覆」之简化（同音借用，非本字）：复本从𠁁从夂（鍑器），復为返回、複为夹衣、覆为反覆。",
"只":"今亦借作「祇」「隻」「衹」之简化（同音借用，非本字）：只本语气词，隻为鸟一枚，祇为适足。",
"云":"今亦借作「雲」之简化（同音借用）：云本云气回转（象云纹），雲加雨为云彩，后云行而雲废，然二字各有从。",
}
n=0
for ch,txt in notes.items():
    p=os.path.join(C,ch+".json")
    if not os.path.exists(p): continue
    d=json.load(open(p,encoding="utf-8"))
    secs=d.get("sections",[])
    if any(isinstance(s,dict) and s.get("key")=="jiezi" for s in secs): continue
    secs.append({"key":"jiezi","label":"借字说明","text":txt,"cites":[]})
    d["sections"]=secs; json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("noted",n)