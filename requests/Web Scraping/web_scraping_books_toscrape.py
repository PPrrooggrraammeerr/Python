
# coding: UTF-8

# webscraping_books_toscrape.py

from bs4 import BeautifulSoup
import requests

page = requests.get ('https://books.toscrape.com/')

website = BeautifulSoup (page.content, 'html.parser')

products = website.find_all ('article', attrs = {'class': 'product_pod'})

title_books = [i.find ('h3') for i in products]

titles_complete = [x.find ('a').get ('title', '') for x in names_books]

for title_complete in titles_complete:

    print (title_complete)