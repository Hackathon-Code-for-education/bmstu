import pytesseract
import cv2
def text_recognition(img):
    image = cv2.imread(img)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    string = pytesseract.image_to_string(image,  lang='rus').lower()
    words = ["студ", "stud", "декан", "уннвир", "уннвер"]
    for i in words:
        if i in string:
            return True
    return False

print(text_recognition("passport1.png"))