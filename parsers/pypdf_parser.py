# pip install pypdf
from pypdf import PdfReader
import time

start = time.time()

reader = PdfReader("data/nnvda_2026_q1_10q.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()

latency = time.time() - start

print("="*50)
print("Parser: PyPDF")
print("Pages:", len(reader.pages))
print("Characters:", len(text))
print("Latency:", round(latency,2), "sec")
print("="*50)

with open("pypdf_output.txt","w",encoding="utf-8") as f:
    f.write(text)