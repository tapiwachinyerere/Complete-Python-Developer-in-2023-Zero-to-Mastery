from PyPDF2 import PdfFileReader, PdfFileWriter

def watermark_pdf(watermark, file, new_file):
    stamp = PdfFileReader(f'{watermark}')
    reader = PdfFileReader(f'{file}')
    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
        page = reader.getPage(i)
        page.mergePage(stamp.getPage(0))
        writer.addPage(page)

    with open(f'{new_file}', 'wb') as nf:
        writer.write(nf)

watermark_pdf('wtr.pdf', 'super.pdf', 'super_w.pdf')