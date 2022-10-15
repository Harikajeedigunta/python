mport os
from pyPDF import pdfFileMerger
data=os.listdir()
for file in data:
    if file.endswith(".pdf"):
        merger.append(file)
merger.write("output.pdf")
merger.close()
