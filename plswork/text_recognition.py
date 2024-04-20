import pytesseract
import cv2
# import matplotlib.pyplot as plt
# from PIL import Image

image = cv2.imread("stud1.jpg")
# print(image)
pytesseract.pytesseract.tesseract_cmd = r".\.venv\Lib\site-packages\pytesseract"
string = pytesseract.image_to_string(image)
print(string)