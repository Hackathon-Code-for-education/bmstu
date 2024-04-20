import pytesseract
import cv2
# import transformers
# import matplotlib.pyplot as plt
# from PIL import Image

image = cv2.imread("stud3.png")
# print(image)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
string = pytesseract.image_to_string(image,  lang='rus')
print(string)