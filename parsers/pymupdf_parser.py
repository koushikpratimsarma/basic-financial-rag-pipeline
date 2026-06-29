# pip install pymupdf
import fitz
import time

pdf_path = "data/nvda_2026_q1_10q.pdf"

start = time.time()

doc = fitz.open(pdf_path)

text = ""

for page in doc:
    text += page.get_text()

latency = time.time() - start

print("="*50)
print("Parser: PyMuPDF")
print("Pages:", doc.page_count)
print("Characters:", len(text))
print("Latency:", round(latency, 2), "sec")
print("="*50)

with open("pymupdf_output.txt", "w", encoding="utf-8") as f:
    f.write(text)