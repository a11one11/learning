# import easyocr
# easyocr_reader =easyocr.Reader(['ch_sim','en'])#ch_sim，是简体中文模型
# print(easyocr_reader.readtext("ocr.png"))
import easyocr
easyocr_reader =easyocr.Reader(['ch_sim','en'])
result = easyocr_reader.readtext("ocr.png")
print([one[1] for one in result])
