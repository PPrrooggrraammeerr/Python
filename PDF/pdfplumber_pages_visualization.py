
# coding: UTF-8

# pdfplumber_pages_visualization.py

import os
import pdfplumber

get_cwd = os.getcwd ()
user_profile = os.getlogin ()

pdf_path = f'{get_cwd}\\file.pdf'

text = ''

with pdfplumber.open (pdf_path) as pdf:
    
    for page in pdf.pages:

        text += page.extract_text ()

print (text)
