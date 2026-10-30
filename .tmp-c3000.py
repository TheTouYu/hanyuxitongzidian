import sys
sys.stdout.reconfigure(encoding="utf-8",errors="replace")
from docx import Document
d=Document(r"D:\字谱智能体\卷四  弋.docx"); p=d.paragraphs[119]
for r in p.runs:
    t=r.text.strip()
    if t: print("T:",t[:40])
    if r._element.findall('.//{http://schemas.openxmlformats.org/officeDocument/2006/relationships}blip') or r._element.findall('.//{urn:schemas-microsoft-com:vml}imagedata'): print("IMG")