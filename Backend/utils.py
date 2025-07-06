import fitz  # PyMuPDF
import re

def clean_text(text):
    # Remove extra newlines, question markers, and formatting noise
    text = re.sub(r'\n+', ' ', text)               # Replace multiple newlines with space
    text = re.sub(r'\s{2,}', ' ', text)            # Remove extra spaces
    text = re.sub(r'\(a\)|\(b\)|\(c\)|\(d\)', '', text, flags=re.IGNORECASE)  # Option markers
    text = re.sub(r'Q\d+[\.:)]?', '', text)        # Remove Q1, Q2, Q3 etc.
    text = re.sub(r'Page \d+ of \d+', '', text)    # Remove footers
    return text.strip()

def load_document(file):
    text = ""
    if file.name.endswith(".pdf"):
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
    elif file.name.endswith(".txt"):
        text = file.read().decode("utf-8")
    else:
        text = "Unsupported file format."
    
    cleaned_text = clean_text(text)
    return cleaned_text