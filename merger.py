#!/usr/bin/env python
# Make PyPDF2 is installed: sudo easy_install PyPDF2
import sys
import os
from PyPDF2 import PdfFileMerger, PdfFileReader

merger = PdfFileMerger()

# Get the folder of the first file and that's where the merged PDF will go
dirname = os.path.dirname(sys.argv[1])

for f in sys.argv[1:]:
    filename = os.path.basename(f)
    print("Appending " + filename + "...")

    # Append each page to the merger
    print(open(f, 'rb'))
    merger.append(PdfFileReader(open(f, 'rb')))
    
    # Close the file to prevent duplicate pages from being appended
    open(f).close()

# Write all the appends to a new file
merger.write(dirname + "/merged.pdf")
