# -*- coding: utf-8 -*-
import io,sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
p=r"D:\系统汉字\prompts\exegesis.md"
t=io.open(p,encoding="utf-8").read()
note="\n## 取字头看原稿、不看知识库合并文本\n\n- 原稿 docx 的每个字头都是**独立段落**（加粗、单独分行），一条一身；知识库（`knowledge/**/*.md`）在录入时把多字并成一段，字头边界丢失，不能据以切条。\n- 因此：查某字有无正条、取它的释义，一律回原稿 docx 按段落切；字族行（`X：…` 或 `X（异体）：…`）只给字头清单，释义要另找该字自己的段落（可能不在本部段落内，必须全卷搜）。\n- 判据：段落以「字（异体）拼音《說文》…」开头，且与上一段落独立；同段内不含第二个字头。\n"
if "取字头看原稿" not in t:
    t=t.rstrip()+"\n"+note
    io.open(p,"w",encoding="utf-8",newline="\n").write(t); print("appended")
else: print("exists")