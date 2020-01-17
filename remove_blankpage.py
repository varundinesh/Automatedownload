import copy, sys
from PyPDF2 import PdfFileReader,PdfFileMerger,PdfFileWriter
#path to the pdf file containing blank pages that needs to be removed
path=r"C:\\Users\\Varun\\Downloads\\issue4\\merged_full.pdf"

input = PdfFileReader(path)
writer = PdfFileWriter()
for i in range(0,input.getNumPages()):
    p = input.getPage(i)
    text = p.extractText()
    if (len(text) > 10):
        writer.addPage(p)
        #path where the result file with out blank pages are saved
        outstream = open(r"C:\\Users\\Varun\\Downloads\\issue4\\mergedlast.pdf", "wb")
        writer.write(outstream)
        outstream.close()

