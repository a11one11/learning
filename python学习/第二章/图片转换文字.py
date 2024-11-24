import easyocr
easyocr_reader =easyocr.Reader(['ch_sim','en'])
print(easyocr_reader.readtext(ocr.png))