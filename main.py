import pdfplumber


def load_pdf_with_tables(file_path):
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            print(f"\n--- Page {i+1} ---")
            print(page.extract_text())        # text
            tables = page.extract_tables()    # tables as lists
            for table in tables:
                print(table)

load_pdf_with_tables("PDF.pdf")