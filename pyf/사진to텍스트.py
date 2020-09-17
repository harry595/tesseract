try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import cv2
from tkinter import messagebox

path="./original"
file_list=os.listdir(path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

for i in file_list:
    image=cv2.imread(path+"/"+i)
    text2=pytesseract.image_to_string(image,lang='kor')
    f = open("./change/"+i+".txt", 'w')
    f.write(text2)

messagebox.showinfo("변환 완료", "COMPLETE!!!")

#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Image.open(path+"/"+i)
