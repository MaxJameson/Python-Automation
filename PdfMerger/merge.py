import PyPDF2
from sys import argv
import os

# creates a pdf merger
merger = PyPDF2.PdfMerger()

# loops through input file arguments
for file in argv:

    # checks if file is pdf
    if file.endswith(".pdf"):
        
        # appends current document to new pdf
        merger.append(file)
        
    # saves new pdf
    merger.write("NewDoc.pdf")