import PyPDF2
import re

class PDFProcessor:
    def extract_sections(self, pdf_path):
        sections = {}
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())

            pattern = re.compile(r"(\d+(?:\.\d+)*\s+.+?)(?=\n\d+(?:\.\d+)*\s+|\Z)", re.DOTALL)
            for match in pattern.finditer(text):
                heading, content = match.group().split('\n', 1)
                sections[heading.strip()] = content.strip()

        return sections
