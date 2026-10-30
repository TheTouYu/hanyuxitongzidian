import io
p=r"memory\CURRENT.md"
t=open(p,encoding="utf-8").read()
line="\n- 2026-10-23 部属订正：心部误归 20 字改回所属部（7 字 bundle bnd_15eb8669ef3f40927f722c589d、13 字 bnd_8fc6babdcb5dfdf8dacc98a94d），慍改归 282 囗部𥁕支（bnd_694128653b990927f0a7070c8c），昷义依原稿订正为「与囚同源、封闭保暖」（提交 3780a59a、f73c7ad5）。判部只用「条目行＋字族衍義组」双证。\n"
if "部属订正" not in t: open(p,"w",encoding="utf-8").write(t.rstrip()+"\n"+line)
print("ok")