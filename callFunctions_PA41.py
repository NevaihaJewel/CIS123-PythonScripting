print("nevada3921")

import requests
from bs4 import BeautifulSoup

def readwebpage():
    import urllib.request
    page = urllib.request.urlopen('https://quotes.toscrape.com/page/2/')
    return page

def parsedata():
    page = readwebpage()
    soup = BeautifulSoup(page, 'html.parser')
    quotes = soup.find_all(class_="quote")
    return quotes

def outputdata():
    quotes = parsedata()
    for quote in quotes:
        print(quote.find(class_='text').get_text())
        print(quote.find(class_='author').get_text())



