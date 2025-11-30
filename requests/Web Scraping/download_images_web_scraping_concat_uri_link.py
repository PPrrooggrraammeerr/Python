
# coding: UTF-8

# download_images_web_scraping_concat_uri_link.py

import mysql.connector
import requests
import shutil

mysql_my_db = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'catalogo_bi'
)

cursor = mysql_my_db.cursor ()

cursor.execute ('SELECT imagem_url FROM dashboards')

results = cursor.fetchall ()

uri_link = 'https://catalogo-bi-production.up.railway.app/'

for result in results:
    
    images = []

    images.append (result[0])

    for image in images:

        uri_link_image = uri_link + image
        
        request = requests.get (uri_link_image)
        
        if request.status_code == 200:
            
            with open (f'images\\{image}', 'wb') as file:
                
                file.write (request.content)

