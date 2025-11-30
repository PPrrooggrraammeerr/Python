
# coding: UTF-8

# ocr_tesseract.py

# O script ocr_tesseract.py tem como objetivo abrir um site, localizar um texto específico usando OCR e clicar automaticamente nele.

import os
import time
import webbrowser
import pyautogui
import pytesseract
from PIL import ImageGrab

webbrowser.open ('https://ftp.sunet.se/')

user_profile = os.getlogin ()

pytesseract.pytesseract.tesseract_cmd = f'C:\\Users\\{user_profile}\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

time.sleep (7.5)

screenshot = ImageGrab.grab ()

ocr_data = pytesseract.image_to_data (screenshot, output_type=pytesseract.Output.DICT)

text_find = False

for count, text in enumerate (ocr_data ['text']):
    
    if 'Public/' in text.strip ().lower ():
        
        text_find = True
        
        x, y, w, h = (ocr_data ['left'] [count], ocr_data ['top'] [count], ocr_data ['width'] [count], ocr_data ['height'] [count])
        
        pyautogui.click (x + w // 2, y + h // 1)
        break

