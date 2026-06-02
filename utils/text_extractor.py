import fitz
from docx import Document


# -----------------------------
# PDF Text Extraction
# -----------------------------
def extract_text_from_pdf(uploaded_file):

    text = ""

    pdf_document = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    for page in pdf_document:
        text += page.get_text()

    return text


# -----------------------------
# DOCX Text Extraction
# -----------------------------
def extract_text_from_docx(uploaded_file):

    doc = Document(uploaded_file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text