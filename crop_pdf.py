#Python program to crop the pdf to different sizes.
from PyPDF2 import PdfFileWriter, PdfFileReader
#providing the path to the pdf
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
    #selecting the cordinate to begin the crop.
    page.cropBox.setLowerLeft((0,32))
    page.cropBox.setLowerRight((613, 32))
    writer.addPage(page)
    #saving the final croped pdf to the directory.
    outstream=open(r"C:\\Users\\Varun\\Downloads\\maths\\withoutbar.pdf","wb")
    writer.write(outstream)
    outstream.close()
