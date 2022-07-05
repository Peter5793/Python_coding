from PyPDF2 import PdfFileReader
from pathlib import Path
# create file reader object
pdf = PdfFileReader('2021-10-05_Roadmap_all_countries.pdf')
# get the pages
#
page_1_object = pdf.getPage(0)
#print(page_1_object)
# extract the texts

page_1_text = page_1_object.extractText()
#print(page_1_text)

with Path('all_countries.txt').open(mode = 'w') as output_file:
    text = ''
    for page in pdf.pages:
        text += page.extractText()
    output_file.write(text)
