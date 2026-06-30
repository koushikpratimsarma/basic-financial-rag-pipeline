# pip install markitdown
from markitdown import MarkItDown
import time

pdf_path = "data/nvda_2026_q1_10q.pdf"

start = time.time()

md = MarkItDown()
result = md.convert(pdf_path)

text = result.text_content

latency = time.time() - start

print("=" * 50)
print("Parser: MarkItDown")
print("Characters:", len(text))
print("Latency:", round(latency, 2), "sec")
print("=" * 50)

with open("markitdown_output.md", "w", encoding="utf-8") as f:
    f.write(text)