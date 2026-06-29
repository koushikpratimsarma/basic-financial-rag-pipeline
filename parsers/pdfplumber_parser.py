# pip install pdfplumber
import pdfplumber
import time

start = time.time()

text = ""
table_count = 0

with pdfplumber.open("data/nvda_2026_q1_10q.pdf") as pdf:
    for page in pdf.pages:
        text += page.extract_text() or ""

        tables = page.extract_tables()
        table_count += len(tables)

latency = time.time() - start

print("="*50)
print("Parser: PDFPlumber")
print("Pages:", len(pdf.pages))
print("Characters:", len(text))
print("Tables:", table_count)
print("Latency:", round(latency,2), "sec")
print("="*50)