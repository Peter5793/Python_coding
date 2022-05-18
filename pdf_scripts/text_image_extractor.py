import fitz
file = fitz.open('2021-10-05_Roadmap_all_countries.pdf') 
# ------------------------------
# extract text
for pageNumber, page in enumerate(file.pages(), start = 1):
    text = page.getText()
    txt = open(f'report_page_{pageNumber}.txt','a')
    txt.writelines(text)
    txt.close()
#--------------------------------
# extract image
for pageNumber, page in enumerate(file.pages(), start = 1):
    for imgnumber, img in enumerate(page.getImageList(), start = 1):
        xref = img[0]
        pix = fitz.Pixmap(file, xref)
        if pix.n >4:
            pix = fitz.Pixmap(fitz.csRGB, pix)

    pix.writePNG(f'image_page{pageNumber}_{imgnumber}.png')