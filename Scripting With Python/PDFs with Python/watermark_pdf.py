from PyPDF2 import PdfFileReader, PdfFileWriter

def watermark_pdf(watermark, file, new_file):
    """
    Adds a watermark to each page of the specified PDF file.

    Args:
    - watermark (str): The file path of the PDF containing the watermark.
    - file (str): The file path of the PDF to be watermarked.
    - new_file (str): The file path where the resulting watermarked PDF will be saved.

    Returns:
    - None

    Note:
    - The function overlays the watermark PDF on each page of the input PDF file and saves the result as a new PDF.
    """
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