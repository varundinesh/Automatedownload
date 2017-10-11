from PyPDF2 import PdfFileWriter, PdfFileReader
reader=PdfFileReader(r"C:\\Users\\Varun\\Downloads\\maths\\final with dark bar.pdf","r")
#reader.getNumPages()
'''page=reader.getPage(0)
print(page.cropBox.getLowerLeft())
print(page.cropBox.getUpperLeft())
print(page.cropBox.getUpperRight())
print(page.cropBox.getLowerRight())'''

writer=PdfFileWriter()
for i in range(reader.getNumPages()):
    page=reader.getPage(i)
    page.cropBox.setLowerLeft((0,32))
    page.cropBox.setLowerRight((613, 32))
    writer.addPage(page)
    outstream=open(r"C:\\Users\\Varun\\Downloads\\maths\\withoutbar.pdf","wb")
    writer.write(outstream)
    outstream.close()
