import pdfplumber
import io

# Check that this name is spelled exactly as 'extract_text'
def extract_text(file_bytes):
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
            return text.strip()
    except Exception as e:
        print(f"Extraction Error: {e}")
        return ""