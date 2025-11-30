
# coding: UTF-8

# web_scraping_extract_files_pdf_in_uri_informed.py

# O script web_scraping_extract_files_pdf_in_uri_informed.py é um programa simples projetado para extrair e baixar todos os arquivos PDF vinculados a uma página da web específica. Ele usa as bibliotecas requests e BeautifulSoup para buscar e analisar a página da web, respectivamente.

import requests, os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

os.system ('clear')

def extract (pdf, folder):

    all = requests.get (pdf)
    devolution = BeautifulSoup (all.content, 'html.parser')

    for url in devolution.find_all ('a', href=True):

        absolute = urljoin (pdf, url ['href'])

        if absolute.endswith ('.pdf'):

            filename = os.path.join (folder, os.path.basename (absolute))

            try:

                with open (filename, 'wb') as file:

                    response = requests.get (absolute)
                    file.write (response.content)
                    print (f"Download done: {os.path.basename (absolute)}")

            except KeyboardInterrupt:

                os.system ('clear')
                exit ()

link = input ('Type the link (URL): ')
destination = input ('Type the destination path: ')

os.system ('clear')

extract (link, destination)
