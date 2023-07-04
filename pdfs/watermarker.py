import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter

template = PyPDF2.PdfFileReader(open("super.pdf", "rb"))
wtr = PyPDF2.PdfFileReader(open("wtr.pdf", "rb"))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(wtr.getPage(0))
    output.addPage(page)

    with open("watermarked_output.pdf", "wb") as file:
        output.write(file)











