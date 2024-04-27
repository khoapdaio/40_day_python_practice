#Day 37

# !pip install pypdf -q

from pypdf import PdfReader # Read PDF, extract images
from pypdf import PdfWriter # Merge PDFs, compress PDF

# Read PDF
file_path = '/content/drive/MyDrive/Colab Notebooks//Day37/day-37.pdf'
reader = PdfReader(file_path)

# Number of pages
num_pages = len(reader.pages)
num_pages

# Get page 1
page_1 = reader.pages[0]
page_1_txt = page_1.extract_text()
page_1_txt

# Get all pages
pages_txt = ""
for i in range (num_pages):
  page = reader.pages[i]
  pages_txt += page.extract_text() + "\n"
pages_txt

# Extract images
count = 0
for page in reader.pages:
  for img_file_obj in page.images:
    with open(str(count) + img_file_obj.name, 'wb') as fp:
      fp.write(img_file_obj.data)
      count += 1

# Merge PDFs
lst_pdf_path = ['/content/drive/MyDrive/Colab Notebooks/Day37/2207.02696.pdf',
                '/content/drive/MyDrive/Colab Notebooks/Day37/2209.02976.pdf',
                '/content/drive/MyDrive/Colab Notebooks/Day37/2402.13616.pdf']

merger = PdfWriter()
for pdf in lst_pdf_path:
  merger.append(pdf)

merger.write('/content/drive/MyDrive/Colab Notebooks/Day37/merged-yolov-679.pdf')
merger.close()

# Compress PDF
writer = PdfWriter(clone_from = '/content/drive/MyDrive/Colab Notebooks/Day37/day-37.pdf')

for page in writer.pages:
  page.compress_content_streams(level = 8)

with open('out.pdf','wb') as f:
  writer.write(f)

# Check the size
import os
file_size = os.path.getsize('/content/drive/MyDrive/Colab Notebooks/Day37/day-37.pdf')/(1024*1024)
print(f'Day-37_pypdf_yolov9.pdf size: {file_size}')

file_out = os.path.getsize('out.pdf')/(1024*1024)
print(f'out.pdf size: {file_out}')