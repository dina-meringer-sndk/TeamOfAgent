# <!-- Powered by FVTeamOfAgents Core -->
from docx import Document
from docx.shared import Pt

def create_docx_from_md(md_text, docx_path):
    doc = Document()
    for line in md_text.split('\n'):
        if line.startswith('# '):
            doc.add_heading(line[2:], level=1)
        elif line.startswith('## '):
            doc.add_heading(line[3:], level=2)
        elif line.startswith('### '):
            doc.add_heading(line[4:], level=3)
        else:
            doc.add_paragraph(line)
    doc.save(docx_path)

def read_docx(docx_path):
    doc = Document(docx_path)
    return '\n'.join([p.text for p in doc.paragraphs])

if __name__ == "__main__":
    # Convert the summary markdown to docx
    with open(r"C:\team of agents\agents_factory\factory_agent_summary.md", "r", encoding="utf-8") as f:
        md_text = f.read()
    create_docx_from_md(md_text, r"C:\team of agents\agents_factory\factory_agent_summary.docx")
