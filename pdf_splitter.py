from PyPDF2 import PdfReader, PdfWriter

# Load the PDF
input_pdf_path = "yourPDF.pdf" # Here you put the full path to your PDF file.
reader = PdfReader(input_pdf_path)

# Total pages and split specifications
total_pages = len(reader.pages)
first_pdf_pages = 82
subsequent_pdf_pages = 84

# Define the split logic
i = 0  # Page position counter
part = 1  # Part number

# First part with 82 pages
writer = PdfWriter()
for page_num in range(i, i + first_pdf_pages):
    writer.add_page(reader.pages[page_num])
output_pdf_path = f"part_{part}.pdf" # Here you put the full path to save the created PDFs.
with open(output_pdf_path, "wb") as output_pdf:
    writer.write(output_pdf)

print(f"Part {part} with {first_pdf_pages} pages saved to: {output_pdf_path}")
part += 1
i += first_pdf_pages  # Update counter for the next section

# Subsequent parts with 84 pages
while i < total_pages:
    writer = PdfWriter()
    end_page = min(i + subsequent_pdf_pages, total_pages)
    for page_num in range(i, end_page):
        writer.add_page(reader.pages[page_num])

    output_pdf_path = f"part_{part}.pdf" # Here you put the full path to save the created PDFs.
    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Part {part} with {end_page - i} pages saved to: {output_pdf_path}")
    part += 1
    i += subsequent_pdf_pages  # Move counter to the next 84 pages

print("PDF successfully split!")
