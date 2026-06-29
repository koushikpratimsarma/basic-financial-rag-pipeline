# docling_parser.py

import time
from docling.document_converter import DocumentConverter

pdf_path = "data/nnvda_2026_q1_10q.pdf"

start = time.time()

converter = DocumentConverter()

result = converter.convert(pdf_path)

text = result.document.export_to_markdown()

latency = time.time() - start

print("=" * 50)
print("Parser: Docling")
print("Characters:", len(text))
print("Latency:", round(latency, 2), "sec")
print("=" * 50)

with open("docling_output.md", "w", encoding="utf-8") as f:
    f.write(text)